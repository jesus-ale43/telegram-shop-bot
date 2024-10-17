from dotenv import load_dotenv
import os

load_dotenv()

import logging

from telegram import BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)


from handlers.commands import *


logging.basicConfig(
    format="(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def post_init(application: Application) -> None:
    await application.bot.set_my_commands(
        [
            BotCommand("start", "Bot Start."),
        ]
    )


def main() -> None:
    application = (
        Application.builder().token(os.getenv("BOT_TOKEN")).post_init(post_init).build()
    )

    application.add_handler(CommandHandler("start", start_command))

    application.run_polling()


if __name__ == "__main__":
    main()
