from aiogram import Bot, Dispatcher
from .handlers.handlers import router


async def setup_bot(token: str) -> None:

    bot = Bot(token)
    dp = Dispatcher()

    dp.include_routers(
        router,
    )

    await dp.start_polling(bot, skip_updates=True)