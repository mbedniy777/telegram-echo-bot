import telebot
from telebot.types import Message
import settings

bot = telebot.TeleBot(token=settings.BOT_TOKEN)


@bot.message_handler()
def echo_handler(message: Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=message.text
    )


bot.infinity_polling()
