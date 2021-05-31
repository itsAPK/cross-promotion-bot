from sqlalchemy import Column, Integer, String,Date,Text,DateTime,BigInteger
from sqlalchemy.sql import exists
from bot.database import base,session
import datetime
from bot import LOGGER


class Channel(base):
    __tablename__ = 'channel'
    id = Column(Integer, primary_key=True)
    chat_id=Column(Integer)
    channel_id=Column(BigInteger)
    subscribers=Column(Integer)
    channel_name=Column(String)
    admin_username = Column(String)
    description=Column(String)

    def __init__(self,chat_id,channel_id,subscribers,channel_name,admin_username,description):
        self.chat_id=chat_id
        self.channel_id=channel_id
        self.channel_name=channel_name
        self.subscribers=subscribers
        self.admin_username=admin_username
        self.description=description

    def __repr__(self):
        return '{}'.format(self.description)
    
    
Channel.__table__.create(checkfirst=True)

class Ban(base):
    __tablename__ = 'ban_channel'
    id = Column(Integer, primary_key=True)
    channel_id=Column(BigInteger)

    def __init__(self,channel_id):
        self.channel_id=channel_id

    def __repr__(self):
        
        return f'{self.id}'

Ban.__table__.create(checkfirst=True)
    
def channel_data(chat_id,channel_id,channel_name,subscribers,admin_username,description):
    LOGGER.info(f"New Channel {channel_id} [{channel_name}] by {admin_username}")
    session.add(Channel(chat_id=chat_id,channel_id=int(channel_id),channel_name=channel_name,subscribers=subscribers,admin_username=admin_username,description=description))
    session.commit()

def is_channel_exist(channel_id):
    LOGGER.info(f"Checking Existance of {channel_id}")
    data=session.query(Channel).filter(Channel.channel_id==int(channel_id))
    return session.query(data.exists()).scalar()

def is_channel_ban(channel_id):
    LOGGER.info(f"Checking ban status {channel_id}")
    ban=session.query(Ban).filter(Ban.channel_id==str(channel_id))
    return session.query(ban.exists()).scalar()

def is_user_not_added_channel(chat_id):
    data=session.query(Channel).filter(Channel.chat_id==chat_id)
    print(session.query(data.exists()).scalar())
    return session.query(data.exists()).scalar()


def delete_channel(channel_id):
    LOGGER.info(f'channel removed {channel_id}')
    session.query(Channel).filter(Channel.channel_id==int(channel_id)).delete()
    session.commit()
    
def get_all_channel(chat_id):
    LOGGER.info(f"Getting Channel registed by {chat_id}")
    return session.query(Channel).filter(Channel.chat_id==chat_id).all()


