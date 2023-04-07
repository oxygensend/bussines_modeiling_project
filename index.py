from logs import LogMenu
from logs import LogService

if __name__ == "__main__":
   
    try:
        logMenu = LogMenu()
        log = logMenu.run()
        logService = LogService(log)

        logService.find_subprocess()
        new = logService.replace_activities_with_subprocess()
        # print(logService.find_subprocess())
        # logService.view_whole_log_process()
        logService.view_process_tree(new)
        logService.view_process_bmpn(new)

    except Exception as e:
        print(e)

