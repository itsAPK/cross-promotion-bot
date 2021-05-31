from pyrogram import filters,Client
from pyrogram.types import Message
import traceback,time
from bot import LOGGER,LOG_CHANNEL,SUDO_USERS,SUPPORT_GROUP
from bot.bot import Bot
from bot.database.models.channel_db import delete_channel
from bot.utils.markup import remove_channel_markup,start_markup

@Bot.on_callback_query(filters.regex('remove_channel'))
async def remove_channel_message(bot : Client, message : Message):
    await bot.edit_message_text(message.from_user.id,message.message.message_id,"Select the channel to remove:",
                                reply_markup=remove_channel_markup(message.from_user.id))
    
@Bot.on_callback_query(filters.regex('[-100-9]'))
async def remove_channel_handler(bot : Client, message : Message):
    try:
        delete_channel(message.data)
        await bot.edit_message_text(message.from_user.id,message.message.message_id,"🗑 Channel Removed Sucessfully",reply_markup=start_markup())
    except Exception:
        await bot.answer_callback_query(message.id,text="⚠️ Channel not exists",show_alert=True)

