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

import openai


class moj_ziomo_Chat():
    def __init__(self):
        self.key = self.readKey()

    def askGPT(self, text):
        openai.api_key = self.key
        response = openai.Completion.create(
            engine="text-curie-001",  # text-curie-001 is latest version of gpt-3
            prompt=text,
            temperature=0.6,
            max_tokens=150,
        )
        return print(response.choices[0].text)

    def readKey(self):
        f = open(".env", "r")
        key = f.read()
        f.close()
        return key




def main():
    while True:
        print('GPT: Ask me a question\n')
        myQn = input()
        chat = moj_ziomo_Chat()
        chat.askGPT(myQn)


main()