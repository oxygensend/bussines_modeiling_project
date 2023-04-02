import pandas as pd
from pm4py.objects.conversion.log import converter as log_converter
import pm4py

path = 'data/running-example.csv'  # Enter path to the csv file
data = pd.read_csv(path, sep=",")
cols = ['ocel:eid', 'ocel:timestamp', 'ocel:activity', 'weight', 'price', 'ocel:type:items'
    , 'ocel:type:products', 'ocel:type:customers', 'ocel:type:orders', 'ocel:type:packages'
        ]
data.columns = cols
data['time:timestamp'] = pd.to_datetime(data['ocel:timestamp'])
data['case:concept:name'] = data['ocel:eid'].astype(str)
data['concept:name'] = data['ocel:activity']
log = log_converter.apply(data, variant=log_converter.Variants.TO_EVENT_LOG)

print(pm4py.openai.suggest_clusters(log, api_key="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"
                                    , openai_model="gpt-3.5-turbo"))
