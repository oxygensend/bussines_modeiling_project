from logs import LogMenu


if __name__ == "__main__":
   
    try:
        logMenu = LogMenu()
        log = logMenu.run()
        print(log.source, log.process_tree)
    except Exception as e:
        print(e)

