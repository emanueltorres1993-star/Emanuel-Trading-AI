from telegram import Bot
import asyncio
from config import TELEGRAM_TOKEN, CHAT_ID

async def main():
    bot = Bot(token=TELEGRAM_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="🤖 Emanuel Trading AI\n\n✅ El bot está conectado correctamente."
    )

asyncio.run(main())
