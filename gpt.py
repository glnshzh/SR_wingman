import openai

openai.api_keys=["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",
                 "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",
                 "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",
                 "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",
                 "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",
                 "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",
                 "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",
                 "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",
                 "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"]
test_api_keys=["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"]
out_api_keys=["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",]


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
print(gpt.getChat(message="为什么冯俊康是神？",api_key=openai.api_keys[8]))
