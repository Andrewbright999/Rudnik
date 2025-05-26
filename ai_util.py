from mistralai import Mistral
import asyncio

api_key = "WQHTa6fnffGjy4XJF5F9nxOk6HuVZd29"  # НУЖНО ЗАМЕНИТЬ НА СВОЙ АПИ КЛЮЧ В ФОРМАТЕ: api_key = "ххххххххх"
model = "mistral-small-latest"

client = Mistral(api_key=api_key)


promt = """
Тебе отправят сообщение, ты должен определить носит ли оно в себе характер мошшенийнечества или нелегальности
Если в сообщении сказано про высокий заработок или легкий заработок (от 4000р.-5000р. в день или 50$+/день) или более 100+тыс. рублей в месяц, или без указания суммы, 
или предлагается набор в команду для заработка, или в сообщении явно иил скрыто продаются запрещенные вещества, как наркотики или люди
Учти что сообщение может быть написано английскими буквами. но русской транскрибацией
Если сообщение относится к одному из видов выше, то отправь только "SPAM" без комментариев, если нет то "POHUY" 
"""


async def check_spam(promt, content):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": promt,
            },
            {
                "role": "user",
                "content": str(content),
            },
        ]
    )

    return chat_response.choices[0].message.content
