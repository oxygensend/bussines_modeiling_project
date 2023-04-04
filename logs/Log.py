from pandas import DataFrame
from pm4py import ProcessTree, BPMN

class Log:
    _end_activities: str
    _start_activities: str
    _source: DataFrame
    _process_tree: ProcessTree
    _model: BPMN
    _events: dict
    _variants: dict
    _subprocesses: dict

    def __init__(self, end_activities, start_activities, source, process_tree, model, events, variants):
        self._end_activities = end_activities
        self._start_activities = start_activities
        self._source = source
        self._process_tree = process_tree
        self._model = model
        self._events = events
        self._variants = variants

    @property
    def end_activities(self) -> str:
        return self._end_activities

    @property
    def start_acitvities(self) -> str:
        return self._start_activities
    
    @property
    def source(self) -> DataFrame:
        return self._source
    
    @property
    def process_tree(self) -> ProcessTree:
        return self._process_tree
    
    @property
    def model(self) -> BPMN:
        return self._model

    @property
    def events(self) -> dict:
        return self._events
    
    @property
    def variants(self) -> dict:
        return self._variants
    
    @property
    def subprocesses(self) -> dict:
        return self._subprocesses
    
    @subprocesses.setter
    def subprocesses(self, subprocesses):
        self._subprocesses = subprocesses
