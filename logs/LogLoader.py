from pandas import read_csv
import pm4py
from logs import Log, LogFactory

class LogLoader:

    def load_csv(file_path: str) -> Log:
        log = read_csv(file_path, sep=';')
        log = pm4py.format_dataframe(log, case_id='case_id', activity_key='activity', timestamp_key='timestamp')
        return LogFactory.create(log)

    def load_xes(file_path: str) -> Log:
        log = pm4py.read_xes(file_path)
        return LogFactory.create(log)

    def load_ocel(file_path: str) -> Log:
        log = pm4py.read_ocel(file_path)
        return LogFactory.create(log)
