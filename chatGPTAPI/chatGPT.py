import openai
from chatGPTAPI import Prompt
from .promptEnum import PromptEnum


class ChatGPT:

    def __init__(self):
        self.key = self.readKey()

    def askGPT(self, question: str):
        openai.api_key = self.key
        prompt = Prompt("gpt-3.5-turbo", 0.6, 2048, PromptEnum.CHAT, question)
        return self.createResponse(prompt)
        

    def createResponse(self, prompt: Prompt):
        if prompt.type == PromptEnum.COMPLETION:
            return openai.Completion.create(
                engine=prompt.getEngine(),
                prompt=prompt.getPrompt(),
                temperature=prompt.getTemperature(),
                max_tokens=prompt.getMaxToken()
            )['choices'][0]
        elif prompt.type == PromptEnum.CHAT:
            message = {'role': 'user', 'content': prompt.getPrompt()}
            return openai.ChatCompletion.create(
                model=prompt.getEngine(),
                temperature=prompt.getTemperature(),
                max_tokens=prompt.getMaxToken(),
                messages=[message]
            )['choices'][0]['message']['content']

    def readKey(self):
        f = open(".env", "r")
        key = f.read()
        f.close()
        return key
