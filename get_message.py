from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me a message and I will display it as a danmaku!')


def echo(update: Update, context: CallbackContext) -> None:
    # 将消息传递给弹幕显示模块
    context.bot_data['messages'].append(update.message.text)


def main() -> None:
    # 你的 API Token
    token = 'YOUR_API_TOKEN'

    updater = Updater(token)
    dispatcher = updater.dispatcher

    # 注册命令和消息处理器
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # 初始化消息存储
    dispatcher.bot_data['messages'] = []

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
