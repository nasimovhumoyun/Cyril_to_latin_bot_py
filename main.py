from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import new_bot as nb
print("Bot started...")
def start(update,context):
    update.message.reply_text('Assalomu alaykum {} men Kiril-Latin botman'.format(update.message.from_user.first_name))

def help_command(update, context):
    update.message.reply_text('Yordamni Google dan olishingiz mumkin')
def handle_message(update,context):
    text = str(update.message.text)
    response = nb.sample_responses(text)
    update.message.reply_text(response)


def main():
    updater = Updater(token='1879962235:AAEE39IXSobStD5esvBgmZQsFJ8GLgyjdXM',use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    updater.start_polling()
    updater.idle()
main()




