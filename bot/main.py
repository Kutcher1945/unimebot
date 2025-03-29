import logging
from aiogram import Bot, Dispatcher, executor
from bot.config import BOT_TOKEN
from bot.handlers import handle_faq

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Register command and message handlers
# dp.register_message_handler(handle_start, commands=["start"])
# dp.register_message_handler(handle_help, commands=["help"])
# dp.register_message_handler(handle_questions, commands=["questions"])
dp.register_message_handler(handle_faq)  # Mistral handles all other input

if __name__ == "__main__":
    print("🚀 Bot is running with Mistral integration...")
    executor.start_polling(dp, skip_updates=True)
