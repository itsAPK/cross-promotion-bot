from pyrogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove
from bot import PROMOTION_NAME
from bot.database.models.channel_db import get_all_channel

def start_markup():
    add_channel=InlineKeyboardButton('➕ Add Channel',callback_data='add_channel')
    my_channel=InlineKeyboardButton('🏷 My Channels',callback_data='my_channel')
    share=InlineKeyboardButton('🌐 Share Bot',switch_inline_query=' provides you the best cross promotion services! Add your channel and Participate in Promotions Join Now {}'.format(PROMOTION_NAME))
    helpn=InlineKeyboardButton('🆘 Help',callback_data='help')
    
    #share=InlineKeyboardButton('🌐 Share Bot',switch_inline_query=' provides you the best cross promotion services! Add your channel and Participate in Promotions Join Now {}'.format(Config.PROMOTION_NAME))
    markup=InlineKeyboardMarkup(
        [
            [add_channel],[my_channel],[share,helpn]
        ]
)
    return markup

def channel_markup():
    remove_channel=InlineKeyboardButton('🗑 Remove Channel',callback_data='remove_channel')
    markup=InlineKeyboardMarkup([[remove_channel]])
    return markup

def back_markup():
    cancel = KeyboardButton('🚫 Cancel')
    markup = ReplyKeyboardMarkup([[cancel]], resize_keyboard=True)
    return markup

def empty_markup():
    return ReplyKeyboardRemove()

def remove_channel_markup(chat_id):
    return InlineKeyboardMarkup([[InlineKeyboardButton(x.channel_name,callback_data=str(x.channel_id)),] for x in get_all_channel(chat_id)])

def admin_markup():
    announce=InlineKeyboardButton('📢 Announcement',callback_data='announce')
    mail=InlineKeyboardButton('📤 Mailing',callback_data='mail')
    ban=InlineKeyboardButton('🚫 Ban Channel',callback_data='ban')
    unban=InlineKeyboardButton('📍 Unban Channel',callback_data='unban')
    update_subs=InlineKeyboardButton('🔄 Update Subscribers',callback_data='update_subs')
    show_channel=InlineKeyboardButton('ℹ️ Channel Info',callback_data='show_channel')
    manage=InlineKeyboardButton('📊 Statistics',callback_data='stats')
    manage_list=InlineKeyboardButton('☑️ Manage List',callback_data='list')
    create_post=InlineKeyboardButton('📝 Create Post',callback_data='create_post')
    preview_list=InlineKeyboardButton('⏮ Preview List',callback_data='preview')
    send_promo=InlineKeyboardButton('✔️ Send Promo',callback_data='send_promo')
    dlt_promo=InlineKeyboardButton('✖️ Delete Promo',callback_data='dlt_promo')
    task=InlineKeyboardButton('⚙️ Settings',callback_data='settings')
    add_admin=InlineKeyboardButton('🛠 Add Admin',callback_data='add_admin') #TODO : Settings markup
    sendpaidpromo=InlineKeyboardButton('💲Send Paid Promo',callback_data='mypapr')
    deletepaidpromo=InlineKeyboardButton('💲Delete Paid Promo',callback_data='deltpr')
    markup=InlineKeyboardMarkup([[add_admin],[mail,announce],[ban,unban],[update_subs],[show_channel,manage_list],[manage,create_post],[preview_list,task],[send_promo,dlt_promo],[sendpaidpromo,deletepaidpromo]])
    return markup