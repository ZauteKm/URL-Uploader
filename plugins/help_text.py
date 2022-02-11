#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Zaute Km

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
# the Strings used for this "thing"
from translation import Translation

from pyrogram import Client, filters
from database.database import AddUser
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.forcesub import ForceSub

@Client.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[
                  InlineKeyboardButton('👥 Group', url='https://t.me/JOSPSupport'),
                  InlineKeyboardButton(' Channel 📢', url='https://t.me/JOSProjects')
                  ],[
                  InlineKeyboardButton('🙄 Source', url='https://github.com/ZauteKm/URL-Uploader'),
                  InlineKeyboardButton('Bot Lists 🤖', url='https://t.me/josprojects/221'),
                  InlineKeyboardButton('GitHub 🤪', url='https://github.com/ZauteKm')
                  ],[
                  InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://youtube.com/playlist?list=PLzkiTywVmsSfmhaDdWNZ5PRmmMKGTIxPJ')
            ]]
        ),
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
                  InlineKeyboardButton('👥 Group', url='https://t.me/JOSPSupport'),
                  InlineKeyboardButton(' Channel 📢', url='https://t.me/JOSProjects')
                  ],[
                  InlineKeyboardButton('🙄 Source', url='https://github.com/ZauteKm/URL-Uploader'),
                  InlineKeyboardButton('Bot Lists 🤖', url='https://t.me/josprojects/221'),
                  InlineKeyboardButton('GitHub 🤪', url='https://github.com/ZauteKm')
                  ],[
                  InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://youtube.com/playlist?list=PLzkiTywVmsSfmhaDdWNZ5PRmmMKGTIxPJ')
            ]]
        ),
        reply_to_message_id=update.message_id
    )
