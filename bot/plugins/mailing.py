from pyrogram import filters,Client
from bot.bot import Bot
from pyrogram.types import Message
import traceback,time
from bot.database.models.user_db import get_all,get_admin
from bot.utils.markup import start_markup,admin_markup,back_markup
from bot import LOGGER,LOG_CHANNEL,SUDO_USERS

@Bot.on_callback_query(filters.regex('^mail$') & (filters.user(get_admin() | filters.user(SUDO_USERS))))
async def mail_handler(bot: Client,message: Message):
    mail_message=await bot.ask(message.from_user.id,'Enter the Message',reply_markup=back_markup())
    if mail_message.text=='🚫 Cancel':
        await bot.send_message(message.from_user.id,"Mailing Canceled",reply_markup=admin_markup())
        LOGGER.info("Mailing Cancelled")
    else:
        LOGGER.info("Mailing Started")
        for user in get_all() :
            try:
                await bot.send_message(user,mail_message.text)
                LOGGER.info(f"Mail sending to {user}")
            except Exception as e:
                LOGGER.error(e)
                LOGGER.error(f"Mail not sent to {user}")
                await bot.send_message(message.from_user.id.id,'Aww :( , Something went wrong',reply_markup=admin_markup())
                await bot.send_message(LOG_CHANNEL,f'\n<code>{traceback.format_exc()}</code>\n\nTime : {time.ctime()} UTC',parse_mode='html')
                
        await bot.send_message(message.from_user.id,'☑️Mailing finished!',reply_markup=admin_markup())
        LOGGER.info('Mailing finished!')