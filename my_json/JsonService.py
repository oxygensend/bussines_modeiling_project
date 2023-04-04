import json


class JsonService:

    @staticmethod
    def transform_gpt3_output(string: str) -> dict:
        """ Transform gpt3 output to list of dictionaries"""
        string.replace("]", "").replace("[", "")
        y = json.loads(string)
        dct = {}
        for res in y:
            dct[res['name']] = res['actions']
        return dct


    @staticmethod
    def find_key_by_value(d: dict, search_term: str) -> str|None:
        result = None
        for key, values in d.items():
            for value in values:
                if search_term in value:
                    result = key
                    break
        return result
