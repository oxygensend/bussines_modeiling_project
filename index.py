from logs import LogMenu
from chatGPTAPI import ChatGPT
import json

if __name__ == "__main__":
   
    try:
        logMenu = LogMenu()
        log = logMenu.run()
        chat = ChatGPT()
        question = "If I have a process with the following activities: " + str(log.events) + " Can you suggest how subprocesses  could be grouped based on provided activities and  return this  ONLY in json format [ {name: 'Subprocess name', 'activities': []},...]?"
        string = chat.askGPT(question)
        print(string)
    except Exception as e:
        print(e)

