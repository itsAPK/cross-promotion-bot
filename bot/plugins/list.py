from pyrogram import filters,Client
import csv
from bot.bot import Bot
from pyrogram.types import Message
import traceback,time
from bot.database.models.user_db import get_admin
from bot.utils.markup import admin_markup,list_markup
from bot import LOGGER,LOG_CHANNEL,SUDO_USERS
from bot.database.models.user_db import get_all_user_data,total_users
from  bot.database.models.channel_db import (total_banned_channel,
                                            total_channel,
                                            get_channel,
                                            get_banned_channel_list,
                                            
                                            get_user_channel_count)


@Bot.on_callback_query(filters.regex('^list$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def list_handler(bot:Client,message:Message):
    await bot.send_message(message.message.chat.id,"☑️ Choose Required List",reply_markup=list_markup())
    
@Bot.on_callback_query(filters.regex('^ban_list$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def ban_list_handler(bot:Client,message:Message):
    channel_count=total_banned_channel()
    text=""
    ban_channels=get_banned_channel_list()
    for channel in ban_channels:
            text+=str(channel)+'\n'
            data=f'Total Banned Channels : {channel_count}\n\n{text}'
            await bot.send_message(message.message.chat.id,data)
            
@Bot.on_callback_query(filters.regex('^user_list$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def user_list_handler(bot:Client,message:Message):        
    users=get_all_user_data()
    with open("users.csv","w",encoding='UTF-8') as f:
            writer = csv.writer(f,delimiter=",",lineterminator="\n")
            writer.writerow(['id','name','username','joined date','no. of registed channels'])
            for user in users:
                channel=get_user_channel_count(user.chat_id)
                if user.username:
                    username= '@'+user.username
                else:
                    continue
                if user.first_name:
                    first_name= user.first_name
                else:
                    first_name= ""
                if user.last_name:
                    last_name= user.last_name
                else:
                    last_name= ""
                name= (first_name + ' ' + last_name).strip()
                writer.writerow([user.chat_id,name,username,user.date,channel]) 
    await bot.send_document(message.from_user.id,'users.csv',caption=f'Total Users : {total_users()}')
                
@Bot.on_callback_query(filters.regex('^channel_list$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def channel_list_handler(bot:Client,message:Message):   
    channels=get_channel()
    with open("channels.csv","w",encoding='UTF-8') as f:
            writer = csv.writer(f,delimiter=",",lineterminator="\n")
            writer.writerow(['channel id','name','subscribers','description','admin id','admin username','channel link'])
            for channel in channels:
                writer.writerow([channel.channel_id,channel.channel_name,channel.subscribers,channel.description,channel.chat_id,channel.admin_username,channel.invite_link]) 
    await bot.send_document(message.from_user.id,'channels.csv',caption=f'Total Users : {total_channel()}')