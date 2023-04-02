from pandas import DataFrame
from logs import Log
import pm4py

class LogFactory:

    def create(source: DataFrame) -> Log:
        start_activities = pm4py.get_start_activities(source)
        end_activities = pm4py.get_end_activities(source)
        process_tree = pm4py.discover_process_tree_inductive(source)
        bpmn_model = pm4py.convert_to_bpmn(process_tree)
        events = pm4py.get_event_attribute_values(source, attribute='concept:name')

        return Log(
            start_activities=start_activities, 
            end_activities=end_activities,
            process_tree=process_tree,
            model=bpmn_model,
            source=source,
            events=events
            )

