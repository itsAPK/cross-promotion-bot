from pyrogram import filters,Client
from pyrogram.types import Message
import traceback,time
from bot import LOGGER,LOG_CHANNEL,SUDO_USERS,SUPPORT_GROUP
from bot.bot import Bot
from bot.database.models.channel_db import is_channel_ban,is_channel_exist,channel_data
from bot.utils.markup import start_markup,back_markup,empty_markup
from bot.utils.is_admin import is_bot_admin
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired,ChannelPrivate

@Bot.on_callback_query(filters.regex('^add_channel$'))
async def add_channel(bot : Client ,message : Message):
    channel=await bot.ask(message.message.chat.id,"✅ <b>Make the bot admin and Forward the message from Channel</b>",reply_markup=back_markup())
    if channel.text=='🚫 Cancel':
        await bot.send_message(message.message.chat.id,"🚫 <b> Cancelled </b>",reply_markup=empty_markup())
    else:
        try:
            chat_id=message.from_user.id
            channel_id=channel.forward_from_chat.id
            channel_name=channel.forward_from_chat.title
            if is_channel_ban(channel_id):
                    await bot.send_message(channel.from_user.id,"Aww :( , This channel banned.")
                
                    return

            if is_channel_exist(channel_id):
                await bot.send_message(channel.from_user.id,"Aww :( , Channel already exists.")
                
                return

            if await is_bot_admin(bot,channel.forward_from_chat.id) is True:
                subscribers=await bot.get_chat_members_count(channel_id)
                #TODO :  SUBSCRIBERS LIMIT
                description=await bot.ask(message.from_user.id,"<b>✅ Send description(max 5 words and 2 emojis)</b>")
                admin_username=message.from_user.username
                invite_link=await bot.export_chat_invite_link(channel_id)
                channel_data(chat_id,channel_id,channel_name,subscribers,admin_username,description.text,invite_link)
                details=f'✅ <b>Channel Submitted Sucessfully</b>\n\nChannel ID : {channel_id}\nChannel name :{channel_name}\nSubscribers : {subscribers}\nDescription : {description.text}'         
                await bot.send_message(message.message.chat.id,details,reply_markup=empty_markup())
                send_group_message=f'✅ <b>New Channel Submited!<b>\n\nChannel ID : {channel_id}\nChannel name :{channel_name}\nSubscribers : {subscribers}\nDescription : {description.text}\nSubmitted By : @{admin_username}'
                await bot.send_message(SUPPORT_GROUP,send_group_message)
                LOGGER.info(f"Channel Added {channel_name}")
            else:
                await bot.send_message(channel.chat.id,"<b> ❌ Bot is not admin</b>",reply_markup=empty_markup())
        
        except (ChannelPrivate,ChatAdminRequired)  as e:
                    LOGGER.error(e)
                    await bot.send_message(LOG_CHANNEL,f'\n<code>{traceback.format_exc()}</code>\n\nTime : {time.ctime()} UTC',parse_mode='html')
                    await bot.send_message(message.message.chat.id,"<b>❌ Bot is not admin</b>",reply_markup=empty_markup())
                

        except Exception as e:
                LOGGER.error(e)
                await bot.send_message(LOG_CHANNEL,f'\n<code>{traceback.format_exc()}</code>\n\nTime : {time.ctime()} UTC',parse_mode='html')
                await bot.send_message(message.message.chat.id,"<b>❌ Invalid action</b>",reply_markup=empty_markup())