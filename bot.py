import Constants as keys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import responses as R

print("Bot started...")

def start(update, context):
    update.message.reply_text("Hello there! Welcome to the Distant AI bot. Type /help to see a list of commands")

def help(update, context):
    update.message.reply_text("""Available Commands :-
/commands - To get available commands
/docs - To get our docs
/contact - To get our contact email
/support - To reach out to our support team""")

def commands(update, context):
    update.message.reply_text("""Type these commands as text :-
contract? - get our contract addresses
website? - get available sites links
socials? - get twitter handles
    """)
    
def docs(update, context):
    update.message.reply_text("Check our docs at docs.distant.finance")

def contact(update, context):
    update.message.reply_text("Send us an email at business@distant.finance")

def support(update, context):
    update.message.reply_text("Please send us an email with your issue at support@distant.finance")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)

def handle_message(update, context):
    text = str(update.message.text).lower()
    our_response = R.responses(text)

    update.message.reply_text(our_response)


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    disp = updater.dispatcher

    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("help", help))
    disp.add_handler(CommandHandler("commands", commands))
    disp.add_handler(CommandHandler("docs", docs))
    disp.add_handler(CommandHandler("contact", contact))
    disp.add_handler(CommandHandler("support", support))
    disp.add_handler(MessageHandler(Filters.text, handle_message))  
    disp.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands
    disp.add_handler(MessageHandler(Filters.text, unknown_text)) # Filters out unknown messages.

    updater.start_polling()
    updater.idle()


main()