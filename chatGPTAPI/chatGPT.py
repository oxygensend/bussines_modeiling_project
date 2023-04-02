import openai
from chatGPTAPI import Prompt


class chatGPT:

    def __init__(self):
        self.key = self.readKey()

    def askGPT(self):
        openai.api_key = self.key
        prompt = Prompt("text-curie-001", 0.6, 150)
        response = self.createResponse(prompt)
        return print(response.choices[0].text)

    def createResponse(self, prompt):
        return openai.Completion.create(
            engine=prompt.getEngine(),
            prompt=prompt.getPrompt(),
            temperature=prompt.getTemperature(),
            max_tokens=prompt.getMaxToken()
        )

    def readKey(self):
        f = open(".env", "r")
        key = f.read()
        f.close()
        return key
