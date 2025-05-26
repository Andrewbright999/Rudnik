from typing import Union
import logging
import asyncio, logging, sys, datetime

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message,  FSInputFile

# from config import TG_TOKEN, GROUP_ID, ADMIN_LIST
from users import UserList, pikle_path
from ai_util import check_spam


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

TG_TOKEN = '6730177900:AAE4ZTKKD7mw0Nn0nGXUnNtSqArv64mCfA0'

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()
user_list = UserList()

class GroupIdFilter(BaseFilter):  # [1]
    def __init__(self, group_id: Union[str , list , int]): # [2]
        self.group_id = group_id

    async def __call__(self, message: Message) -> bool:  # [3]
        if isinstance(self.group_id, str):
            print(message.chat.id)
            return message.chat.id == self.group_id
        else:
            return message.chat.id in self.group_id
        
        
# dp.message.filter(
#     GroupIdFilter(group_id=[GROUP_ID, ADMIN_LIST])
# )

async def get_save(): 
    pikle = FSInputFile(path=pikle_path, filename=f"save {datetime.datetime.now()}.pickle")
    return pikle


@dp.message(Command("save")) 
async def cmd_start(message: Message):
    file = await get_save(message)
    await message.answer_document(document=file, caption=f"Сохренение от {datetime.datetime.now()}\nКол-во чел: {len(user_list)}")
    

@dp.message()
async def message_with_text(message: Message):
    spam = await check_spam(message.text)
    if spam == "SPAM":
        await message.delete()
    else:
        user_list.check_user(message.from_user.username)
        if message.text == "@all":
            msg = user_list.get_all_list()
            msg_text:str = " ".join(msg)
            while len(msg) > 4000:
                msgs = msg.split(msg.find(" ", 4000, 4090))
                for i in msgs:
                    m = await message.answer(i)
                    await m.edit_text(text="@all")
            else:
                msg = await message.answer(msg_text)
                await msg.edit_text(text="@all")
        
        
        
async def main() -> None:
    # dp.include_routers()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
    