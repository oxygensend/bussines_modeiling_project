from chatGPTAPI import ChatGPT
from my_json.JsonParser import JsonParser
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization


class LogService:
    def __init__(self, log):
        self.my_json = JsonParser()
        self.chat = ChatGPT()
        self.log = log

    def findSubprocess(self):
        question = "If I have a process with the following activities: " + str(
            self.log.events) + "Can you suggest how the subprocess could be grouped based on the provided activities. " \
                               "I " \
                               "would really like the result to be only in json format, without unnecessary text, " \
                               "please [{name: \"Name of subprocess\", \"actions\": []},...]? "
        string = self.chat.askGPT(question)
        outputAsDict = self.my_json.transformGPT3Output(string)
        return outputAsDict

    def viewLogWholeProcess(self):
        LOG = self.log.source.loc[:,['time:timestamp','case:concept:name','concept:name']]
        dfg = dfg_discovery.apply(LOG)

        gviz = dfg_visualization.apply(dfg, log=LOG, variant=dfg_visualization.Variants.FREQUENCY)
        dfg_visualization.view(gviz)

