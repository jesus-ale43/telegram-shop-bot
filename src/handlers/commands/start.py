from telegram import Update
from telegram.ext import CallbackContext

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_markdown("Hello World!")