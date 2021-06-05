from pyrogram import filters,Client
from bot.bot import Bot
from pyrogram.types import Message
import traceback,time
from bot.database.models.user_db import get_admin,get_all,delete_user   
from bot.database.models.channel_db import total_channel                                                                                        
from bot.utils.markup import admin_markup,back_markup,empty_markup,announce_markup
from bot import LOGGER,LOG_CHANNEL,SUDO_USERS,SUPPORT_GROUP,SUPPORT_CHANNEL

@Bot.on_callback_query(filters.regex('^announce$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def announcement_handler(bot:Client,message:Message):
    await bot.send_message(message.from_user.id, "✅ Choose Announcement Category",reply_markup=announce_markup())
    
    
@Bot.on_callback_query(filters.regex('^close_reg$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def close_reg_handler(bot:Client,message:Message):
    data=f"""
🔰Registration has been closed

- List will be out soon.
- Stay tuned!

<b>Total Channel Registered :</b> {total_channel()}
"""

    await bot.send_message(SUPPORT_GROUP,data)
    LOGGER.info(f"Close Registration Message sent to @{SUPPORT_GROUP}")

    
@Bot.on_callback_query(filters.regex('^open_reg$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def open_reg_handler(bot:Client,message:Message):
    me=await bot.get_me()
    data=f"""
🔰 Registration Started 🔰

➖ Participation Method
1. <a href='https://t.me/{me.username}'>Click Here To Participate</a>
2. Click on start
3. Click ‘My Channels’ to check your registred channels
4. New members, this is one time registration. You don't need to register your channel for next promo
5. Old members, we will update Channel subs count via bot. Do not worry about subscribers count."

✅ List Rules
- 2 Hours Top
- 2 Days in Channel
- 24 Hours to Share
————————————
⚠️ List Type Promotion'
    """
    
    await bot.send_message(SUPPORT_GROUP,data)
    user_message=f""" 
ℹ️ Admin notification

✅ Registration has been started

<b>List Rules</b>
1. 2 Hours on 🔝 In channel 
2. 2 Days in Channel
3. 24 Hours To Share

<a href='https://t.me/{me.username}'>Click Here To Participate</a>"""
    users=get_all()
    for user in users:
        try:
            await bot.send_message(user,user_message)
            LOGGER.info(f"Open Registration Message sent to {user}")
        except Exception as e:
            LOGGER.info(f"Open Registration message not sent to {user} ({e})")
            delete_user(user)
    await bot.send_message(message.message.chat.id,'☑️Done!')
    LOGGER.info(f"Open Registration Message send to all")
    
@Bot.on_callback_query(filters.regex('^list_out$')& (filters.user(get_admin()) | filters.user(SUDO_USERS)))
async def list_out_handler(bot:Client,message:Message):
    user_message=f"""
ℹ️ Admin notification

✅ List is out @{SUPPORT_CHANNEL}

List Rules
1. 2 Hours on 🔝 In channel 
2. 2 Days in Channel 
3. 24 Hours To Share"""
    users=get_all()
    for user in users:
        try:
            await bot.send_message(user,user_message)
            LOGGER.info(f"List out Message sent to {user}")
        except Exception as e:
            LOGGER.info(f"List out message not sent to {user} ({e})")
            delete_user(user)
    await bot.send_message(message.message.chat.id,'☑️Done!')
    LOGGER.info(f"Message send to all")