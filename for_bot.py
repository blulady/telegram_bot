from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import environ

env = environ.Env()
environ.Env.read_env()
SECRET_KEY = env('SECRET_KEY')

updater = Updater(SECRET_KEY, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to my first attempt bot")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("Just testing it out")


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.google.com/gmail/about/")


def linkedin_url(update: Update, context: CallbackContext) :
    update.message.reply_text("https://www.linkedin.com/in/sarahsanger/")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(f"Sorry I can't recognise you, you said '{update.message.text}")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(f"Sorry '{update.message.text}'")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('LinkedIn', linkedin_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))

updater.start_polling()
