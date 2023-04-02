import json


class JsonParser:
    def transformGPT3Output(self, string: str):
        """ Transform gpt3 output to list of dictionaries"""
        string.replace("]", "").replace("[", "")
        y = json.loads(string)
        dct = {}
        for res in y:
            dct[res['name']] = res['actions']
        return dct
