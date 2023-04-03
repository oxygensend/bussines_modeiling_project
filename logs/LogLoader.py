import pm4py
from logs import Log, LogFactory
import pandas as pd


class LogLoader:

    def load_csv(file_path: str) -> Log:
        log = pd.read_csv(file_path, sep=';')
        log = pm4py.format_dataframe(log, case_id='case_id', activity_key='activity', timestamp_key='timestamp')
        return LogFactory.create(log)

    def load_ocel_csv(file_path: str) -> Log:
        print("DSa")
        data = pd.read_csv(file_path, sep=",")
        cols = ['ocel:eid', 'ocel:timestamp', 'ocel:activity', 'weight', 'price', 'ocel:type:items'
            , 'ocel:type:products', 'ocel:type:customers', 'ocel:type:orders', 'ocel:type:packages'
                ]
        data.columns = cols
        print(data['ocel:type:orders'])
        data['time:timestamp'] = pd.to_datetime(data['ocel:timestamp'])
        data['case:concept:name'] = data['ocel:type:orders'].astype(str)
        data['concept:name'] = data['ocel:activity']
        data = data.drop(['ocel:activity', 'ocel:type:orders', 'ocel:timestamp'], axis=1)
        return LogFactory.create(data)

    def load_xes(file_path: str) -> Log:
        log = pm4py.read_xes(file_path)
        return LogFactory.create(log)

    def load_ocel(file_path: str) -> Log:
        log = pm4py.read_ocel(file_path)
        return LogFactory.create(log)
