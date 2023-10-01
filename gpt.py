import openai


class gpt:
    @staticmethod
    def getChat(message: str, api_key, role="user",model="gpt-3.5-turbo"):
        openai.api_key = api_key
        openai.api_base = "https://openaiapicn.top/v1"
        chat_completion = openai.ChatCompletion.create(model=model,
                                                       messages=[{"role": role, "content": message}]
                                                       )
        text = chat_completion
        # print(text["choices"][0]["message"]['content'])
        return text["choices"][0]["message"]['content']

