from bot.bot import setup_bot
import os

# Берем токен из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")

async def main() -> None:
    await setup_bot(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
