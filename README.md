# bussiness_modelling_project

Aplikacja umożliwiająca analizę semantyczną logu z wykorzystaniem modelu językowego LLM (np. GPT-3 przez API) pod kątem określenia podprocesów, anastępnie przetworzenie danych i wyświetlenie modelu głównego oraz podprocesów.


## chatGTPAPI module - handles connection with openAI api

  - *ChatGPT class* - is responsible for comunication with openAI api. Based on settings we are able to connect with chat completion and basic completion.
  - *Prompt class* - responsible for settings and question passed to openAI api
  - *Prompt Enum* - helper enum for prompt type

## my_json module - handles custom dictionary operations
  - *JsonService class* - static service responsible for operations performed on dictionaries
    - transform_gtp3_output - transform  output(subprocesses) generated with ChatGPT class to normalized dictionary `{"subprocess_name": ["action1", ...], ..}`
    - find_key_by_value - check if activity exists in any subprocess, if so returns the name of the subprocess to which it is assigned

## logs module - main module that handles operations on log files and semantic analysis
  .....

