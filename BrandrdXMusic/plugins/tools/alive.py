import asyncio

from BrandrdXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import SUPPORT_CHANNEL, SUPPORT_CHAT

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/e999c40cb700e7c684b75.mp4",
        caption=f"Hey {message.from_user.mention}\nI'm a telegram streaming bot with some useful features.\n\n❐ Stream Audio and Video on Voice Chat Group.\n❐ Support YouTube, Spotify, Resso, AppleMusic, SoundCloud, etc.\n❐ Totally free.",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="Updates", url=f"https://t.me/{SUPPORT_CHANNEL}"
            ),
            InlineKeyboardButton(
                text="Support", url=f"https://t.me/{SUPPORT_CHAT}"
            ),
        ],
                [
            InlineKeyboardButton(
                text="😎 Owner", url=f"https://t.me/EasyWinter"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "Close", callback_data="close"
                    )
                ],
            ]
        )
    )
