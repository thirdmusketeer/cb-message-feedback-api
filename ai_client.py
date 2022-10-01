import os
import openai

openai.api_key = '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'
# keywords = 'アイスクリームショップ, フレーバーの選択'


def get_suggestions(keywords):
    res = openai.Completion.create(
        model="ada:ft-personal-2022-08-22-04-18-36",
        prompt=" {0} ->".format(keywords),
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return res['choices']