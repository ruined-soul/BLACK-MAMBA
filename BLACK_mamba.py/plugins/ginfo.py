"""
(((((((((((((((((((((((@TIMEX_OF_CLOCK)))))))))))))))))))))))))))
"""
from telethon.errors.rpcerrorlist import YouBlockedUserError

from BLACK_MAMBA import CMD_HELP
from BLACK_MAMBA.utils import admin_cmd
from BLACK_MAMBA import MASTER
BLACK_MAMBA = MASTER
PROBOY = "@tgscanrobot"
# MADE BY TIMEX_OF_CLOCK 🔥🔥

@borg.on(admin_cmd("ginfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    TIMEX_OF_CLOCK = event.pattern_match.group(1)
    if "@" in TIMEX_OF_CLOCK:
        async with borg.conversation(PROBOY) as conv:
            try:
                
                await event.edit(f"ωαιт ¢нє¢кιηg тнє ∂єтαιℓѕ σƒ тнιѕ ρєяѕση ѕтαятє∂ ву {BLACK_MAMBA}")
                await conv.send_message("/start")
                await conv.get_response() #made by TIMEX_OF_CLOCK
                await conv.send_message(f"{TIMEX_OF_CLOCK}")
                TEAMX = await conv.get_response()
                TEAMX = TEAMX.message
                if TEAMX.startsawith("This human"):
                  return await event.edit("no details Found")
                await borg.send_message(event.chat_id, TEAMX)
                await event.delete() #made by TIMEX_OF_CLOCK
            except YouBlockedUserError:
                await event.edit("Error: @tgscanrobot unblock and retry!")
    elif TIMEX_OF_CLOCK == "":
        OP = await event.get_reply_message()
        PRO = OP.sender.id 
        async with borg.conversation(PROBOY) as conv:
            try: #made by TIMEX_OF_CLOCK 🔥
              #made by TIMEX_OF_CLOCK 
                await event.edit(f"тнιѕ υѕєя ∂єтαιℓѕ ¢нє¢кιηg ву {BLACK_MAMBA}")
                await conv.send_message("/start")
                await conv.get_response() #made by TIMEX_OF_CLOCK
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                TEAMX = TEAMX.message
                if TEAMX.startswith("This human"):
                  return await event.edit("no details Found")
                await borg.send_message(event.chat_id, TEAMX)
                await event.delete()
            except YouBlockedUserError: #made by TIMEX_OF_CLOCK
                await event.edit("Error: unblock @tgscanrobot and try again!")
    else:
        async with borg.conversation(PROBOY) as conv:
            try: #made by TIMEX_OF_CLOCK 🔥
                
                await event.edit(f"тнιѕ υѕєя ∂єтαιℓѕ ¢нє¢кιηg ву {BLACK_MAMBA}") 
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                TEAMX = TEAMX.message
                if TEAMX.startswith("This human"):
                  return await event.edit("no details found")
                await borg.send_message(event.chat_id, TEAMX)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock  @tgscanrobot `and try again!")
from .. import HELP
HELP(NAME = "ginfo", HELP = ".ginfo <tag or username>", FUCK=True, debug=False, amazing = None)
# try
