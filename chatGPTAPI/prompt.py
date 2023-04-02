class Prompt:

    def __init__(self, engine, temperature, max_tokens, type, prompt):
        self._engine = engine
        self._temperature = temperature
        self._max_tokens = max_tokens
        self._prompt = prompt
        self._type = type

    def createPrompt(self, fillprompt):
        self._prompt = fillprompt

    def getEngine(self):
        return self._engine

    def getTemperature(self):
        return self._temperature

    def getMaxToken(self):
        return self._max_tokens

    def getPrompt(self):
        return self._prompt

    def setEngine(self, engine):
        self._engine = engine

    def setTemperature(self, temp):
        self._temperature = temp

    def setMaxToken(self, max_tokens):
        self._max_tokens = max_tokens

    @property
    def type(self):
        return self._type