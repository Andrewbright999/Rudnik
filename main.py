import logging
import asyncio, logging, sys, datetime

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message,  FSInputFile

from config import TG_TOKEN, GROUP_ID, ADMIN_ID
from users import UserList, pikle_path


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()
user_list = UserList()

class GroupIdFilter(BaseFilter):  # [1]
    def __init__(self, group_id: str | list | int): # [2]
        self.group_id = group_id

    async def __call__(self, message: Message) -> bool:  # [3]
        if isinstance(self.group_id, str):
            print(message.chat.id)
            return message.chat.id == self.group_id
        else:
            return message.chat.id in self.group_id
        
        
# dp.message.filter(
#     GroupIdFilter(group_id=[GROUP_ID, ADMIN_ID])
# )

async def send_save(message: Message): 
    pikle = FSInputFile(path=pikle_path, filename=f"save {datetime.datetime.now()}.pickle")
    await message.bot.send_document(pikle, caption=f"Сохренение от {datetime.datetime.now()}\nКол-во чел: {len(user_list)}")


@dp.message(Command("save")) 
async def cmd_start(message: Message):
    await send_save(message)

@dp.message(F.text=="@all")
async def message_with_text(message: Message):
    user_list.check_user(message.from_user.username)
    if message.text == "@all":
        msg = user_list.get_all_list()
        msg = await message.answer(" ".join(msg))
        await msg.edit_text(text="@all")
        await send_save(message)
        
        
async def main() -> None:
    # dp.include_routers()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
    