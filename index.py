from logs import LogMenu
from logs import LogService

if __name__ == "__main__":
   
    try:
        logMenu = LogMenu()
        log = logMenu.run()
        logService = LogService(log)
        # logService.find_subprocess()
        logService.view_whole_log_process()
        # logService.view_transformed_log_process()
        # res = logService.findSubprocess()
    except Exception as e:
        print(e)

