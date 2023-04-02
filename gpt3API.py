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
