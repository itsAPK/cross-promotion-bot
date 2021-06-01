from pyrogram import filters,Client
from pyrogram.types import Message
import traceback,time
from bot import LOGGER,LOG_CHANNEL,SUDO_USERS,SUPPORT_GROUP
from bot.bot import Bot
from bot.database.models.channel_db import is_user_not_added_channel,Channel
from bot.utils.markup import channel_markup,start_markup
from bot.database import session

@Bot.on_callback_query(filters.regex('^my_channel$'))
async def my_channel_handler(bot : Client,message : Message):
    line='_________________________________________________________'
    data=" "
    if not is_user_not_added_channel(message.message.chat.id):
        await bot.send_message(message.message.chat.id,"⚠️ **You haven't registered any channel with our bot yet Or Channels might have been removed or banned**",parse_mode='md',reply_markup=start_markup())
    else:
        channels=session.query(Channel).filter(Channel.chat_id==message.message.chat.id).all()
        total=session.query(Channel).filter(Channel.chat_id==message.message.chat.id)
        for channel in channels:
                data+=line+'\nChannel Id :'+ str(channel.channel_id)+'\nChannel Name :'+channel.channel_name+'\nSubscribers :' +str(channel.subscribers)+'\n\n' 
        await bot.send_message(message.message.chat.id,f'**Total Channels :{total.count()}**\n\n{data}',parse_mode='md',reply_markup=channel_markup())
    