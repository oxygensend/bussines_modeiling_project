from chatGPTAPI import ChatGPT
from my_json import JsonService
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization
import pm4py
from logs import Log, LogFactory
import xml.etree.ElementTree as ET
import os


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

    def view_whole_log_process_petri(self) -> None:
        self._view_log(self._log)

    def view_transformed_log_process_petri(self) -> None:
        log = self.replace_activities_with_subprocess()
        self._view_log(log)

    def view_process_tree(self, log: Log) -> None:
        pm4py.view_process_tree(log.process_tree)
    
    def view_process_bmpn(self, log: Log) -> None:
        pm4py.view_bpmn(log.model)

    def _view_process_petri(self, log: Log) -> None:
        LOG = log.source.loc[:,['time:timestamp','case:concept:name','concept:name']]
        dfg = dfg_discovery.apply(LOG)

        gviz = dfg_visualization.apply(dfg, log=LOG, variant=dfg_visualization.Variants.FREQUENCY)
        dfg_visualization.view(gviz)

    def replace_activities_with_subprocess(self) -> Log:

        temp =  self._log.source
        for index, row in self._log.source.iterrows():

            subproccess = JsonService.find_key_by_value(self._log.subprocesses, row['concept:name'])
            if subproccess:
                temp.loc[index, 'concept:name'] = subproccess



        return  LogFactory.create(temp)


            

        
