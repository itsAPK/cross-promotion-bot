from pyrogram import filters,Client
from bot.bot import Bot
from pyrogram.types import Message
import traceback,time
from bot.database.models.user_db import get_admin,total_admin,total_users
from bot.database.models.channel_db import total_banned_channel,total_channel
from bot.utils.markup import admin_markup,back_markup
from bot import LOGGER,LOG_CHANNEL,SUDO_USERS


@Bot.on_callback_query(filters.regex('^stats$') & (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def bot_stats(bot : Client , message : Message):
    stats=f"""<b>Total users :</b> {total_users()}
<b>Total Admins :</b> {total_admin()}
<b>Registerd channels :</b> {total_channel()}
<b>Banned channels :</b> {total_banned_channel()}"""
    LOGGER.info(f"BOT STATISTICS : \n {stats}")
    await bot.send_message(message.message.chat.id,stats)