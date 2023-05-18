from logs import LogMenu
from logs import LogService

if __name__ == "__main__":
   
    try:
        logMenu = LogMenu()
        log = logMenu.run()
        logService = LogService(log)

        logService.find_subprocess()
        new = logService.replace_activities_with_subprocess() 

        logService.print_subrpocesses()
        logService.view_subprocess()
        logService.view_process_bmpn(new)
        logService.view_process_bmpn(log)

    except Exception as e:
        print(e)

