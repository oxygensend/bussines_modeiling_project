from logs import LogMenu
from chatGPTAPI import ChatGPT
from my_json.JsonParser import JsonParser

if __name__ == "__main__":
   
    try:
        logMenu = LogMenu()
        log = logMenu.run()
        my_json = JsonParser()
        chat = ChatGPT()
        question = "If I have a process with the following activities: " + str(log.events) + " Can you suggest how the subprocesses could be grouped based on the provided activities. I would really like the result to be only in json format, without unnecessary text, please [{name: \"Name of subprocess\", \"actions\": []},...]?"
        string = chat.askGPT(question)
        outputAsDict = my_json.transformGPT3Output(string)
        print(outputAsDict)
    except Exception as e:
        print(e)

