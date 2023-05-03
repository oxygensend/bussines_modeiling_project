from logs import LogMenu
from logs import LogService

if __name__ == "__main__":
   
    try:
        logMenu = LogMenu()
        log = logMenu.run()
        logService = LogService(log)

        logService.find_subprocess()
        print(log.subprocesses)
        new = logService.replace_activities_with_subprocess() 


        # print(log.process_tree)
        # print(log.subprocesses)
        # print(logService.find_subprocess())

        # logService.view_whole_log_process_petri()
        # logService.view_process_tree(log)
        # logService.view_process_tree(new)
        logService.view_process_bmpn(new)
        logService.view_process_bmpn(log)

    except Exception as e:
        print(e)

