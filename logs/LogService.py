from chatGPTAPI import ChatGPT
from my_json import JsonService
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization
import pm4py
from logs import Log, LogFactory
import pandas as pd
import time
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

class LogService:

    _chat: ChatGPT
    _log: Log

    def __init__(self, log: Log):
        self._chat = ChatGPT()
        self._log = log

    def find_subprocess(self) -> dict:
        # 4-7 eventow i nie wszystkie chcemy grupowac 
        question = "If I have a process with the following tree: " + str(
            self._log.process_tree) + "Can you suggest how the subprocess could be grouped based on the provided activities. In one subpocess there should be from 4 to 7 activities no more no less. Group only activities that are matching, not every sent activity has to relate to subprocess." \
                            "I " \
                            "would really like the result to be only in json format, without unnecessary text, " \
                            "please [{name: \"Name of subprocess\", \"actions\": []},...]? "
        string = self._chat.askGPT(question)
        outputAsDict = JsonService.transform_gpt3_output(string)

        self._log.subprocesses = outputAsDict
        return outputAsDict


    def view_process_tree(self, log: Log) -> None:
        pm4py.view_process_tree(log.process_tree)
    
    def view_process_bmpn(self, log: Log) -> None:
        pm4py.view_bpmn(log.model)

    def view_process_petri(self, log: Log) -> None:
        LOG = log.source.loc[:,['time:timestamp','case:concept:name','concept:name']]
        dfg = dfg_discovery.apply(LOG)

        gviz = dfg_visualization.apply(dfg, log=LOG, variant=dfg_visualization.Variants.FREQUENCY)
        dfg_visualization.view(gviz)

    def replace_activities_with_subprocess(self) -> Log:
        logging.info("started: replace_activities_with_subprocess")
        start = time.time()

        self.subprocesses_validation();
        temp = self._log.source.copy()

        subprocess_map = {}
        for subprocess_name, activities in self._log.subprocesses.items():
            subprocess_map.update({activity: subprocess_name for activity in activities})

        temp['concept:name'] = temp['concept:name'].apply(lambda x: subprocess_map.get(x, x))

        end = time.time()
        logging.info( "finished: replace_activities_with_subprocess in time: %s ", (end - start))

        return LogFactory.create(temp)


    def subprocesses_validation(self):
        subprocess_copy = self._log.subprocesses.copy()
        for key in subprocess_copy.keys():
           x = self._validate_subprocess(self._log.subprocesses[key])
           if x is False:
                del self._log.subprocesses[key]


    def print_subrpocesses(self):
        print("Priniting subprocesses groups")
        for subprocess, activities in self._log.subprocesses.items():
            print("\nSubprocess name: " + subprocess)
            print("Activities: ")
            for activity in activities:
                print(activity)
            
        
    def _validate_subprocess(self, subprocess) -> bool:
        """ subprocess should has atleast 3 activities inside and they should be in relation"""

        if len(subprocess) < 3:
            return False

        filtered = pm4py.filter_directly_follows_relation(self._log.source, [subprocess])
        if isinstance(filtered, pd.DataFrame):
            return True
        elif len(subprocess) > 2: 
            subprocess.pop()
            self._validate_subprocess(subprocess)
        
        return False


        

