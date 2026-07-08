from telegram import Bot

class TelegramAlerts:

    def __init__(self, token, chat_id):
        self.bot = Bot(token=token)
        self.chat_id = chat_id

    async def send_alert(self, pair, signal, confidence):
        message = f"""
🤖 Emanuel Trading AI

📊 Activo: {pair}
📈 Señal: {signal}
⭐ Confianza: {confidence}%

⏰ Temporalidad: M5
        """

        await self.bot.send_message(
            chat_id=self.chat_id,
            text=message
        )
