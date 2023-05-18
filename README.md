# bussiness_modelling_project

An application to semantically analyze the log using the LLM language model (e.g., GPT-3 via API) to identify sub-processes, then process the data and display the main model and sub-processes.

## Docs

### chatGTPAPI module - handles connection with openAI api

  - *ChatGPT class* - is responsible for comunication with openAI api. Based on settings we are able to connect with chat completion and basic completion.
  - *Prompt class* - responsible for settings and question passed to openAI api
  - *Prompt Enum* - helper enum for prompt type

### my_json module - handles custom dictionary operations
  - *JsonService class* - static service responsible for operations performed on dictionaries
    - transform_gtp3_output - transform  output(subprocesses) generated with ChatGPT class to normalized dictionary `{"subprocess_name": ["action1", ...], ..}`
    - find_key_by_value - check if activity exists in any subprocess, if so returns the name of the subprocess to which it is assigned

### logs module - main module that handles operations on log files and semantic analysis
  - *Log class* - class that store information about log
  - *LogFactory class* - class responsible for creating *Log* objects
  - *LogLoader class* - class responsible for loading logs from file into *Log* object
    - load_csv - load csv file
    - load_ocel_csv - load ocel csv file
    - load_xes - load xes file
    - load_ocel - load ocel file
  - *LogMenu class*  - class responsible for parsing argument passed to program
  - *LogService class* - service that stores the logic used to perform the log sementic analysis
    - find_subprocesses - handle communication with open AI and as an output returns transformed dictionary with subprocesses
    - replace_activities_with_subprocess - responsible for replacing activitities with subprocess in source dataframe
    - subprocesses_validation -  responsible for validation whether subprocesses where created properly
    - _validate_process - helper method for subprocesses validation
    - print_subrpocesses - prints subprocesses groups in human readable way
    - view_process_tree - displays process tree diagram
    - view_process_bmpn - displays bpmn diagram
    - view_process_petri - displays petri diagram
 
 ### index.py - it is an executable file

  You can run program like that(depends on file extension):
    -   `python index.py --[csv|xes|ocel_csv|xes] filepath`
## Stack
  - python
  - pandas
  - openAI
  - pm4py
