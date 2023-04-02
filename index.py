from logs import LogMenu
from chatGPTAPI import chatGPT

if __name__ == "__main__":
   
    try:
        # chat = chatGPT()
        # chat.askGPT()
        logMenu = LogMenu()
        log = logMenu.run()
        print(log.source, log.process_tree)
    except Exception as e:
        print(e)

