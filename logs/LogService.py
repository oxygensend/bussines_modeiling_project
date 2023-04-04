from chatGPTAPI import ChatGPT
from my_json import JsonService
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization
import pm4py
from logs import Log, LogLoader
import xml.etree.ElementTree as ET
import os


class LogService:

    _chat: ChatGPT
    _log: Log

    def __init__(self, log: Log):
        self._chat = ChatGPT()
        self._log = log

    def find_subprocess(self) -> dict:
        question = "If I have a process with the following activities: " + str(
            self._log.events) + "Can you suggest how the subprocess could be grouped based on the provided activities. " \
                               "I " \
                               "would really like the result to be only in json format, without unnecessary text, " \
                               "please [{name: \"Name of subprocess\", \"actions\": []},...]? "
        string = self._chat.askGPT(question)
        outputAsDict = JsonService.transform_gpt3_output(string)

        self._log.subprocesses = outputAsDict
        return outputAsDict

    def view_whole_log_process(self) -> None:
        self._view_log(self._log)

    def view_transformed_log_process(self) -> None:
        log = self._replace_activities_with_subprocess()
        self._view_log(log)

    def _view_log(self, log: Log) -> None:
        LOG = log.source.loc[:,['time:timestamp','case:concept:name','concept:name']]
        print(LOG)
        dfg = dfg_discovery.apply(LOG)

        gviz = dfg_visualization.apply(dfg, log=LOG, variant=dfg_visualization.Variants.FREQUENCY)
        dfg_visualization.view(gviz)

    def _replace_activities_with_subprocess(self) -> Log:
        # write proccess to temporary file
        pm4py.write_xes(self._log.source, 'temp.xes', 'concept:name')

        tree = ET.parse('temp.xes')
        root = tree.getroot()

        # find all events in the XES file
        for event in root.findall(".//{http://www.xes-standard.org/}event"):

            attribute = event.find(".//{http://www.xes-standard.org/}string[@key='concept:name']")
            name = attribute.get('value')

            subproccess = JsonService.find_key_by_value(self._log.subprocesses, name)
            attribute.set('value', subproccess)

        tree.write('temp.xes')
        proccessed_log = LogLoader.load_xes('temp.xes');
        # os.remove('temp.xes')

        return proccessed_log


        
