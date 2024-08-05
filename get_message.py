import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import nest_asyncio

# 应用 nest_asyncio 以允许在运行的事件循环中使用嵌套事件循环
nest_asyncio.apply()

# 使用你的真实机器人 API Token
bot_token = '7453177525:AAECDvPpdZTMzMhsEpXnNgYw94vWqiWlRz0'  # 请在此替换为正确的 Token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Bot is running!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Echo: {update.message.text}")
    print(f"Received message: {update.message.text}")

async def main():
    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
