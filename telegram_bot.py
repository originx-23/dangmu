import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from config_manager import config
from shared_data import messages  # Import the shared messages list

# Telegram message handler functions
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('欢迎使用桌面弹幕机器人！发送任意消息以查看弹幕效果。')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        message_text = update.message.text
        messages.append(message_text)
        print(f"Received message: {message_text}")  # Print received message
        print(f"Messages queue: {messages}")        # Print current message queue
    else:
        print("No message received.")

async def run_telegram_bot():
    # Create Application object with the bot token
    application = ApplicationBuilder().token(config['telegram']['bot_token']).build()

    # Add command handler for the /start command
    application.add_handler(CommandHandler('start', start))

    # Add message handler for text messages that are not commands
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    await application.run_polling()
