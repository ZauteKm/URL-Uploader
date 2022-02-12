#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Zaute Km

from pyrogram import Client, filters
from config import Config
from database.database import db


@Client.on_message(filters.private & filters.command('total'))
async def sts(c, m):
    if m.from_user.id != Config.AUTH_USERS:
        return 
    total_users = await db.total_users_count()
    await m.reply_text(text=f"Total user(s) {total_users}", quote=True)
