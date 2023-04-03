from logs import LogMenu
from logs import LogService

if __name__ == "__main__":
   
    try:
        logMenu = LogMenu()
        log = logMenu.run()
        logService = LogService(log)
        logService.viewLogWholeProcess()
        res = logService.findSubprocess()
        print(res)
    except Exception as e:
        print(e)

