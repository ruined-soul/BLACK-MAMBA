# @TIMEX_OF_CLOCK
# RUINED_SOUL

"""
Available Commands:
- Click gift as soon as fast as possible
Command:- .game ....
- Second game is a xogame
Command:- .xogame ....
"""

from telethon import events
import asyncio
from BLACK_MAMBA import CMD_HELP
from BLACK_MAMBA.utils import admin_cmd, sudo_cmd, edit_or_reply
from var import Var


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.2
    animation_ttl = range(0, 14)
    input_str = event.pattern_match.group(1)
    if input_str == "game":
        await event.edit(input_str)
        animation_chars = [
       
            "**Welcome To BLACK_MAMBA Repo Game**",
            "**Click The Gift As Fast As Possible**",
            "**Game Starts in 3...**",
            "**Game Starts in 2..**",
            "**Game Starts in 1.**",    
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆[🎁](https://github.com/SUKHPAL443/BLACK_MAMBA)🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆[🎁](https://github.com/SUKHPAL443/BLACK_MAMBA)🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇[🎁](https://github.com/ULTRA-OP/ULTRA-X)🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆[🎁](https://github.com/SUKHPAL443/BLACK_MAMBA)🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n[🎁](https://github.com/SUKHPAL443/BLACK_MAMBA)🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇[🎁](https://github.com/SUKHPAL443/BLACK_MAMBA)\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇\n🎇🎆🎇🎆🎇🎆🎇",
            "**Game Over !.!.!.!**"
 ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 14])


from BLACK_MAMBA.utils import admin_cmd, sudo_cmd, edit_or_reply
from var import Var

@borg.on(admin_cmd(pattern="xogame$"))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob) 
    await tap[0].click(event.chat_id)
    await event.delete()
    
CMD_HELP.update
(
  {
    "BLACK_MAMBA-games": "**Plugin : **`games`\
    \n\n**Syntax : **`.xogame and .game`\
    \n**Function : **games h play krke Dekho"
  }
)
