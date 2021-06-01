from sqlalchemy import Column, Integer, String,Date,Text,DateTime
from bot.database import base,session
import datetime
from bot import LOGGER
import threading



class Settings(base):
    __tablename__='settings'
    id=Column(Integer,primary_key=True)
    subs_limit=Column(Integer,default=0)
    list_size=Column(Integer,default=25)

    def __repr__(self):
        return f'{self.id}'

Settings.__table__.create(checkfirst=True)

class Post(base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    emoji=Column(String,default=None)
    set_top=Column(String,default=None)
    set_bottom=Column(String,default=None)
    set_caption=Column(String,default=None)

    def __init__(self,emoji,set_top,set_bottom,set_caption):
        self.emoji=emoji
        self.set_top=set_top
        self.set_bottom=set_bottom
        self.set_caption=set_caption

    def __repr__(self):
        return f'{self.id}'

Post.__table__.create(checkfirst=True)

class Button(base):
    __tablename__ = 'button'
    id = Column(Integer, primary_key=True)
    set_button_name=Column(String)
    set_button_url=Column(String)

    def __init__(self,set_button_name,set_button_url):
        self.set_button_name=set_button_name
        self.set_button_url=set_button_url

    def __repr__(self):
        return f'{self.id}'

Button.__table__.create(checkfirst=True)

LOCK=threading.RLock()

def add_subs_limit(limit):
    with LOCK:
        settings=session.query(Settings).first()
        if settings:
            session.query(Settings).filter(Settings.id==1).update({Settings.subs_limit:int(limit)})
            session.commit()
        else:
            session.add(Settings(subs_limit=int(limit)))
            session.commit()

def add_list_size(size):
    with LOCK:
        settings=session.query(Settings).first()
        if settings:
            session.query(Settings).filter(Settings.id==1).update({Settings.list_size:int(size)})
            session.commit()
        else:
            session.add(Settings(list_size=int(size)))
            session.commit()

def get_settings():
    try:
        return session.query(Settings).first()
    finally:
        session.close()