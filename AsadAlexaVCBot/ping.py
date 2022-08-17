# code by Asad Ali Owner Off Jankari Ki Duniya Youtube Channel


import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from time import time
from datetime import datetime

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Week", 60 * 60 * 24 * 7),
    ("Day", 60 * 60 * 24),
    ("Hour", 60 * 60),
    ("Min", 60),
    ("Sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(contact_filter & filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("`...`")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(f"`{delta_ping * 1000:.3f} ms` \n**Uptime ⏳** - `{uptime}`")


@Client.on_message(contact_filter & filters.command(["restart"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.reply("`Restarting...`")
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@Client.on_message(contact_filter & filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    HELP = f"**🛠 ʜᴇʟᴘ ᴍᴇɴᴜ 🛠** \n\n**ᴀɴʏᴏɴᴇ ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ɪғ ɢʀᴏᴜᴘ ᴍᴏᴅᴇ sᴇᴛ ᴛᴏ ᴛʀᴜᴇ**\n**ᴛᴏ ᴘʟᴀʏ ᴀᴜᴅɪᴏ sᴏɴɢ** {HNDLR}play\n** ᴛᴏ ᴘʟᴀʏ ᴠɪᴅᴇᴏ sᴏɴɢ** {HNDLR}vplay\n**ғᴏʀ ʀᴀᴅɪᴏ ʟɪᴠᴇ sᴛʀᴇᴀᴍɪɴɢ** {HNDLR}stream (**ғᴏʀ ʀᴅɪᴏ ʟɪɴᴋs**) \n**ғᴏʀ ʟɪᴠᴇ ʟɪɴᴋs** {HNDLR}vstream (ғᴏʀ .m3u8 / ʟɪᴠᴇ ʟɪɴᴋs) \n\n**SUDO SOMMANDS** (**ʏᴏᴜ ᴄᴀɴ ʀᴜɴ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ɪғ ʏᴏᴜ ᴀʀᴇ ɪɴ ᴍʏ ᴄᴏɴᴛᴀᴄᴛ ʟɪsᴛ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ** @Dr_Asad_Ali **ғᴏʀ ʙᴇᴄᴏᴍɪɴɢ sᴜᴅᴏ**): \n**ғᴏʀ ɢᴇᴛᴛɪɴɢ ᴘɪɴɢ** {HNDLR}ping \n**sᴋɪᴘ ᴛʜᴇ sᴏɴɢ** {HNDLR}skip \n**ᴛᴏ ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴏɴɢ** {HNDLR}pause ᴀɴᴅ **ᴛᴏ ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴏɴɢ **{HNDLR}resume \n**ᴛᴏ sᴛᴏᴘ ᴛʜᴇ sᴏɴɢ** {HNDLR}stop / **ᴛᴏ ᴇɴᴅ ᴛᴏ sᴏɴɢ** {HNDLR}end \n**ғᴏʀ ʜᴇʟᴘ ᴍᴇɴᴜ** {HNDLR}help \n**ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ** {HNDLR}repo \n**ᴛᴏ ʀᴇsᴛᴀʀᴛ ʙᴏᴛ** {HNDLR}restart"
    await m.reply(HELP)


@Client.on_message(contact_filter & filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    REPO = f"**🛠 IF YOU WANT REPO 🛠** \n\n**ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴍʏ** [ᴏɴᴡᴇʀ](t.me/Dr_Asad_Ali)\n**ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ᴘʀᴏᴊᴇᴄᴛ ᴛʜᴇ ɢɪᴠᴇ ᴍᴇ ʜᴇᴀʀᴛ ᴀɴᴅ ᴊᴏɪɴ** [ʜᴇᴀʀᴛ](t.me/Give_Me_Heart) [ᴜᴘᴅᴀᴛᴇs](t.me/AsadSupport) [ᴊᴏɪɴ](t.me/Shayri_Music_Lovers)"
    await m.reply(REPO)
