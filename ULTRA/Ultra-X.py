#Copyright 2021-2022 BLACK_MAMBA Bot
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from BLACK_MAMBA import ALIVE_NAME, StartTime
from BLACK_MAMBA.utils import admin_cmd
from BLACK_MAMBA import bot
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from BLACK_MAMBA.helpers.functions import get_readable_time
import time
import os
import datetime
#importing finished
from BLACK_MAMBA import botnickname 
BOT = str(botnickname) if botnickname else "BLACK_MAMBA вσт"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "BLACK_MAMBA вσу"
tim = get_readable_time((time.time() - StartTime))
#pic 👇
PIC = os.environ.get("ALIVE_PIC")
#op 
uptime = tim
#time = date + time okay
TIME = time.asctime(time.localtime())
#my name 👇
BLACK_MAMBA = "[BLACK_MAMBA](https://t.me/BLACK_MAMBA_SUPPORT)"
#my bots repo 👇
REPO = "[BLACK_MAMBA вσт](https://github.com/SUKHPAL443/BLACK_MAMBA)"
#grpup👇NAME = "[{MAATER}](tg://user?id={X})"
#yrr isko apne bot me aply krne se pehle mere se pooch lena ok
#aur aage add kruga abhi busy okay 🤔
global ghanti
X = bot.uid
MASTER = f"[{NAME}](tg://user?id={X})"
GROUP = "[SUPPORT GROUP](https://t.me/BLACK_MAMBA_SUPPORT)"
#itna test h aur aage krte h
#test successful raha ab aage 
ALIVE = "BLACK_MAMBA вσт ιѕ ση 🔥 ƒιяє 🔥" 
OP = " нєℓℓσ мαѕтєя му ηαмє ιѕ BLACK_MAMBA вσт ι αм тнє вєѕт υѕєявσт 💝"
EMOJI = "🔥"
