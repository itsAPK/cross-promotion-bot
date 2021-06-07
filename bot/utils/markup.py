from pyrogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove
from bot import PROMOTION_NAME
from bot.database.models.channel_db import get_all_channel
from bot.database.models.post_db import get_buttons

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
    preview_list=InlineKeyboardButton('⏮ Preview Promo',callback_data='preview')
    send_promo=InlineKeyboardButton('✔️ Send Promo',callback_data='send_promo')
    dlt_promo=InlineKeyboardButton('✖️ Delete Promo',callback_data='delete_promotion')
    task=InlineKeyboardButton('⚙️ Settings',callback_data='settings')
    add_admin=InlineKeyboardButton('🛠 Add Admin',callback_data='add_admin')
    sendpaidpromo=InlineKeyboardButton('💲Send Paid Promo',callback_data='send_paid_promo')
    deletepaidpromo=InlineKeyboardButton('💲Delete Paid Promo',callback_data='delete_paid_promo')
    markup=InlineKeyboardMarkup([[add_admin],[mail,announce],[ban,unban],[update_subs],[show_channel,manage_list],[manage,create_post],[preview_list,task],[send_promo,dlt_promo],[sendpaidpromo,deletepaidpromo]])
    return markup


def settings_markup():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('☑️ Set Subscribers Limit',callback_data='subs_limit')],
            [InlineKeyboardButton('☑️ Set List Size',callback_data='list_size')],
            [InlineKeyboardButton('🔙 Back',callback_data='back')]
        ]
    )
    
def list_markup():
    channel_list=InlineKeyboardButton('🕹 Channel List',callback_data='channel_list')
    ban_list=InlineKeyboardButton('🚫 Ban List',callback_data='ban_list')
    user_list=InlineKeyboardButton('👤 User List',callback_data='user_list')
    back=InlineKeyboardButton('🔙 Back',callback_data='back') 
    markup=InlineKeyboardMarkup([[channel_list,user_list],[ban_list],[back]])
    return markup


def create_post_markup():
    top_sponser=InlineKeyboardButton('⬆️ Set Top Text',callback_data='set_top_text')
    bottom_sponser=InlineKeyboardButton('⬇️ Set Bottom Text',callback_data='set_bottom_text')
    emoji=InlineKeyboardButton('☑️ Set Emoji',callback_data='set_emoji')
    set_button=InlineKeyboardButton('🔘 Set Buttons',callback_data='set_button')
    delete_button=InlineKeyboardButton('🗑 Delete Buttons',callback_data='delete_button')
    set_caption=InlineKeyboardButton('🔖 Set Caption',callback_data='set_caption')
    add_image=InlineKeyboardButton('🖼 Add Image',callback_data='add_image')
    back=InlineKeyboardButton('🔙 Back',callback_data='back')
    markup=InlineKeyboardMarkup([[top_sponser,bottom_sponser],[emoji,set_caption],[set_button,delete_button],[add_image],[back]])
    return markup

def promo_button_markup():
    buttons=get_buttons()
    button=[[InlineKeyboardButton(x.name,url=x.url),] for x in buttons]
    markup=InlineKeyboardMarkup(button)
    return markup  

def preview_list_markup():
    button_promo=InlineKeyboardButton('🔳 Button Promo',callback_data='preview_button_promo')
    classic_promo=InlineKeyboardButton('🏛 Classic Promo',callback_data='preview_classic_promo')
    morden_promo=InlineKeyboardButton('🔰 Standard Promo',callback_data='preview_morden_promo')
    descpromo=InlineKeyboardButton('🎐 Description Promo',callback_data='preview_desc_promo')
    back=InlineKeyboardButton('🔙 Back',callback_data='back')
    markup=InlineKeyboardMarkup([[button_promo,classic_promo],[morden_promo,descpromo],[back]])
    return markup

def announce_markup():
    open_reg=InlineKeyboardButton('📖 Open Registration',callback_data='open_reg')
    close_reg=InlineKeyboardButton('📕 Close Registration',callback_data='close_reg')
    list_out=InlineKeyboardButton('📰 List Out Notification',callback_data='list_out')
    back=InlineKeyboardButton('🔙 Back',callback_data='back')
    markup=InlineKeyboardMarkup([[open_reg,close_reg],[list_out],[back]])
    return markup


def send_promo_markup():
    button_promo=InlineKeyboardButton('🔳 Button Promo',callback_data='send_button_promo')
    classic_promo=InlineKeyboardButton('🏛 Classic Promo',callback_data='send_classic_promo')
    morden_promo=InlineKeyboardButton('🔰 Standard Promo',callback_data='send_standard_promo')
    descpromo=InlineKeyboardButton('🎐 Description Promo',callback_data='send_desc_promo')
    back=InlineKeyboardButton('🔙 Back',callback_data='back')
    markup=InlineKeyboardMarkup([[button_promo,classic_promo],[morden_promo,descpromo],[back]])
    return markup
