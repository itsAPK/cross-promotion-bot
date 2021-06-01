from pyrogram import filters,Client
from bot.bot import Bot
from pyrogram.types import Message
import traceback,time
from bot.database.models.user_db import get_admin
from bot.database.models.channel_db import (delete_channel,
                                            ban_channel,
                                            unban_channel,
                                            is_channel_exist, 
                                            get_channel,
                                            is_channel_banned,
                                            update_subs,
                                            get_channel_by_id)
                           
                                                                                                    
from bot.utils.markup import admin_markup,back_markup,empty_markup
from bot import LOGGER,LOG_CHANNEL,SUDO_USERS
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired,ChannelPrivate

@Bot.on_callback_query(filters.regex('^ban$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def ban_channel_handler(bot:Client,message:Message):
    channel_ban=await bot.ask(message.message.chat.id,'Forward the message from the channel',reply_markup=back_markup())
    try:
        if channel_ban.text=='🚫 Cancel':
            await bot.send_message(message.message.chat.id,"Action Cancled",reply_markup=empty_markup())
        else:

            if not is_channel_exist(channel_ban.forward_from_chat.id):
                    await bot.send_message(message.message.chat.id,"Channel Not exist",reply_markup=empty_markup())
            else:
                channel=get_channel_by_id(int(channel_ban.forward_from_chat.id))
                await bot.send_message(channel.chat_id,"Your channel {} is banned".format(channel.channel_name))
                ban_channel(int(channel_ban.forward_from_chat.id))
                delete_channel(int(channel_ban.forward_from_chat.id))
                
                await bot.send_message(message.message.chat.id,"Channel banned",reply_markup=empty_markup())
    except Exception as e:
        LOGGER.error(e)
        await bot.send_message(LOG_CHANNEL,f'\n<code>{traceback.format_exc()}</code>\n\nTime : {time.ctime()} UTC',parse_mode='html')
        await bot.send_message(message.from_user.id,"Something went worng",reply_markup=empty_markup())
                    
                 
            
@Bot.on_callback_query(filters.regex('^unban$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def unban_channel_handler(bot:Client,message:Message):
    channel_ban=await bot.ask(message.message.chat.id,'Forward the message from the channel',reply_markup=back_markup())
    try :
        if channel_ban.text=='🚫 Cancel':
            await bot.send_message(message.message.chat.id,"Action Cancled",reply_markup=empty_markup())
        else:
            if not is_channel_banned(channel_ban.forward_from_chat.id):
                    await bot.send_message(message.message.chat.id,"Channel not in ban list",reply_markup=empty_markup())
            else:
                    unban_channel(int(channel_ban.forward_from_chat.id))
                    await bot.send_message(message.message.chat.id,"Channel unbanned",reply_markup=empty_markup())
    except Exception as e:
        LOGGER.error(e)
        await bot.send_message(LOG_CHANNEL,f'\n<code>{traceback.format_exc()}</code>\n\nTime : {time.ctime()} UTC',parse_mode='html')
        await bot.send_message(message.from_user.id,"Something went worng",reply_markup=empty_markup())
                    
                    
@Bot.on_callback_query(filters.regex('^update_subs$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def update_subs_handler(bot:Client,message:Message):
    error_list=""
    LOGGER.info("updating members started")
    for channel in get_channel():
        try: 
            LOGGER.info(f"updating memebers {channel}")
            subs=await bot.get_chat_members_count(channel)
            update_subs(channel,subs)
        except (ChannelPrivate,ChatAdminRequired)  as e:
                    LOGGER.error(e)
                    await bot.send_message(LOG_CHANNEL,f'\n<code>{traceback.format_exc()}</code>\n\nTime : {time.ctime()} UTC',parse_mode='html')
                    error_list+=f"🆔 Channel ID : {channel}\n ❓ {e}"
                
    await bot.send_message(message.message.chat.id,f"<b>Error List</b>\n\n{error_list}",)
    await bot.send_message(message.message.chat.id,"✅ Subscribers Updated")
    LOGGER.info("updating members completed")
    
@Bot.on_callback_query(filters.regex('^show_channel$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def show_channel_handler(bot:Client,message:Message):
    channel_info=await bot.ask(message.message.chat.id,'Forward the message from the channel',reply_markup=back_markup())
    try:
        if channel_info.text=='🚫 Cancel':
            await bot.send_message(message.message.chat.id,"Action Cancled",reply_markup=empty_markup())
        else:
            channel=get_channel_by_id(channel_info.forward_from_chat.id)
            data=f"""
🆔 ID : {channel.channel_id}
📛 Name : {channel.channel_name}
📄 Description :{channel.description}
➖ Subscribers : {channel.subscribers}
👨🏼‍💼 Admin : {channel.admin_username}
            """
            await bot.send_message(message.from_user.id,data)
    except Exception as e:
        LOGGER.error(e)
        await bot.send_message(LOG_CHANNEL,f'\n<code>{traceback.format_exc()}</code>\n\nTime : {time.ctime()} UTC',parse_mode='html')
        await bot.send_message(message.from_user.id,"Something went worng",reply_markup=empty_markup())