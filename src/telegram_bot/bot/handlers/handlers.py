from aiogram.types import Message
from aiogram.utils.markdown import hbold


from aiogram import Router

from aiogram.filters.command import Command


router = Router()

@router.message(Command("start"))
async def handle_start(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@router.message()
async def handle_echo(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")