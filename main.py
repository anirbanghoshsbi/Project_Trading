#pip install python-telegram-bot --upgrade
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from behavior_engine import handle_message
from config import TOKEN

async def reply(update, context):
    user_message = update.message.text
    response = handle_message(user_message)
    await update.message.reply_text(response)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()

