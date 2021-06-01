#-*-coding : utf-8 -*-

from datetime import datetime
from importlib import import_module as imp_mod
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger,DEBUG
from os import environ, mkdir, path
from sys import exit as sysexit
from sys import stdout, version_info
from time import time
from traceback import format_exc
from bot.config import Config
import asyncio



LOG_DATETIME = datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
#LOGDIR ="{}/logs".format(__name__)

#if not path.isdir(LOGDIR):
    #mkdir(LOGDIR)

#LOGFILE ="{}/{}_{}.log".format(LOGDIR,__name__,LOG_DATETIME)

#file_handler = FileHandler(filename=LOGFILE)

stdout_handler = StreamHandler(stdout)

basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=INFO,
    handlers=[stdout_handler],
)

getLogger("pyrogram").setLevel(INFO)
getLogger('sqlalchemy.engine').setLevel(INFO)    

LOGGER = getLogger(__name__)


if version_info[0] < 3 or version_info[1] < 7:
    LOGGER.error(
        (
            "You MUST have a Python Version of at least 3.7!\n"
            "Multiple features depend on this. Bot quitting."
        ),
    )
    sysexit(1) 

STRING_SESSION = Config.STRING_SESSION
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
SUPPORT_GROUP = Config.SUPPORT_GROUP
SUPPORT_CHANNEL = Config.SUPPORT_CHANNEL
LOG_CHANNEL = Config.LOG_CHANNEL
SUDO_USERS=Config.SUDO_USERS
DATABASE_URI=Config.DATABASE_URI
WORKERS = Config.WORKERS
BOT_TOKEN=Config.BOT_TOKEN
PREFIX_HANDLER = Config.PREFIX_HANDLER 
PROMOTION_NAME= Config.PROMOTION_NAME
VERSION = Config.VERSION
UPTIME = time()
BOT_USERNAME = ""
BOT_NAME = ""
BOT_ID = 0

from bot.database import session,base