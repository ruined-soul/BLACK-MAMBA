
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from BLACK_MAMBA import ALIVE_NAME, StartTime, CMD_HELP
#from . import BLACK_MAMBA
from BLACK_MAMBA import BOT, PHOTO, VERSION
from BLACK_MAMBA.utils import admin_cmd, sudo_cmd
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"

        
#make by BLACK_MAMBA bht mehnat lag gayi yrr but banhi gaya 😅 
#so credits ke sath kang krna, nhi to tum jante ho apna bhai DMCA hai 🙂😁
#CREDITGOESTO OWNER OF LEGENDBOT
#modify by madboy482
@borg.on(admin_cmd(pattern=r"awake"))
@bot.on(sudo_cmd(pattern=r"awake", allow_sudo=True))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   global PHOTO
   if PHOTO:
     tag = borg.uid
#     uptm = await BLACK_MAMBA.get_readable_time((time.time() - StartTime))
     ALIVE_MESSAGE= f"**✧✧ {BOT} IS UP AND RUNNING SUCCESSFULLY ✧✧**"
     ALIVE_MESSAGE += "\n\n"
     ALIVE_MESSAGE += "**✥✥ 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 ✥✥**\n\n"
     ALIVE_MESSAGE += "✧ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : `1.19.5`\n\n"
     ALIVE_MESSAGE += f"✧ BLACK_MAMBA 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : `{VERSION}`\n\n"
#     ALIVE_MESSAGE += f"✧ 𝚄𝙿𝚃𝙸𝙼𝙴 : {uptm}\n\n"
     ALIVE_MESSAGE += f"✧ 𝙼𝚈 𝙱𝙾𝚂𝚂 : [{DEFAULTUSER}](tg://user?id={tag})\n\n"
     ALIVE_MESSAGE += "✧ 𝙶𝚁𝙾𝚄𝙿 : [SUPPORT](https://t.me/BLACK_MAMBA_SUPPORT)\n\n"
     ALIVE_MESSAGE += f"✧ [𝙳𝙴𝙿𝙻𝙾𝚈](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2HEROKU) 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 [{BOT}](http://github.com/SUKHPAL443/BLACK_MAMBA) ✧\n"   
     await awake.delete() 
     await borg.send_file(awake.chat_id, PHOTO,caption=ALIVE_MESSAGE)
   elif PHOTO == None:
     PHOTO = "https://telegra.ph/file/76e47f1f4cf7a5b0e5d1a.jpg"
     tag = borg.uid
#     uptm = await BLACK_MAMBA.get_readable_time((time.time() - StartTime))
     ALIVE_MESSAGE= f"**✧✧ {BOT} IS UP AND RUNNING SUCCESSFULLY ✧✧**"
     ALIVE_MESSAGE += "\n\n"
     ALIVE_MESSAGE += "**✥✥ 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 ✥✥**\n\n"
     ALIVE_MESSAGE += "✧ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : `1.19.5`\n\n"
     ALIVE_MESSAGE += f"✧  BLACK_MAMBA 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : `{VERSION}`\n\n"
#     ALIVE_MESSAGE += f"✧ 𝚄𝙿𝚃𝙸𝙼𝙴 : {uptm}\n\n"
     ALIVE_MESSAGE += f"✧ 𝙼𝚈 𝙱𝙾𝚂𝚂 : [{DEFAULTUSER}](tg://user?id={tag})\n\n"
     ALIVE_MESSAGE += "✧ 𝙶𝚁𝙾𝚄𝙿 : [SUPPORT](https://t.me/BLACK_MAMBA_SUPPORT)\n\n"
     ALIVE_MESSAGE += f"✧ [𝙳𝙴𝙿𝙻𝙾𝚈](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU) 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 [{BOT}](http://github.com/SUKHPAL443/BLACK_MAMBA) ✧\n"   
     await awake.delete() 
     await borg.send_file(awake.chat_id, PHOTO,caption=ALIVE_MESSAGE)
   else:
     await awake.edit("Please add right value in ALIVE_PHOTTO var..")

CMD_HELP.update(
    {
        "awake": "Plugin : awake\
    \n\nSyntax : .awake\
    \nFunction : you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)
