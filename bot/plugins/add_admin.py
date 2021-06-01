from pyrogram import filters,Client
from bot.bot import Bot
from pyrogram.types import Message
import traceback,time
from bot.database.models.user_db import get_admin,add_admin
from bot.utils.markup import admin_markup,back_markup,empty_markup
from bot import LOGGER,LOG_CHANNEL,SUDO_USERS


@Bot.on_callback_query(filters.regex('^add_admin$')& filters.user(get_admin()))
async def add_admin_handler(bot:Client,message:Message):
    try:
        add_admins=await bot.ask(message.from_user.id,"Send the telegram user ID of user\nNote : Must be the user of the bot",reply_markup=back_markup())
        if add_admins.text=='🚫 Cancel':
            await bot.send_message(message.from_user.id,'Cancelled',reply_markup=empty_markup())
        else:
            add_admin(int(add_admins.text))
            LOGGER.info(f"{add_admins.text} added as admin by {message.from_user.id}")
            await bot.send_message(message.from_user.id,"Admin Added Sucessfully",reply_markup=empty_markup())
    except Exception as e:
            LOGGER.error(e)
            await bot.send_message(LOG_CHANNEL,f'\n<code>{traceback.format_exc()}</code>\n\nTime : {time.ctime()} UTC',parse_mode='html')
            await bot.send_message(message.from_user.id,'Aww :( , Something went wrong',reply_markup=empty_markup())
    