from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "7594297424:AAHqdIjFo1Al79Ku4BTnj7VTTrZgxUpOlWs"
bot = Bot(TOKEN)

app = Flask(__name__)

dispatcher = Dispatcher(bot, None, use_context=True)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("سلام! بات فعال است.")

def handle_message(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"شما گفتید: {update.message.text}")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    dispatcher.process_update(update)
    return "OK"

if __name__ == "__main__":
    app.run(port=5000)
