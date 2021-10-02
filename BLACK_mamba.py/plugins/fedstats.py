import asyncio
# made by BLACK_MAMBA & KING_COBRA
from telethon.errors.rpcerrorlist import YouBlockedUserError
from BLACK_MAMBA.legend import NAME
from BLACK_MAMBA import CMD_HELP
from BLACK_MAMBA import bot
from BLACK_MAMBA.utils import admin_cmd

bot = "@MissRose_bot"
BLACK_MAMBA = NAME


@borg.on(admin_cmd("fstat ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit(f"**¢нє¢кιηg ƒѕтαт ση σя∂єя σƒ {BLACK_MAMBA}**...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
        user = sysarg
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her fedstat.`"
        )
        return
    else:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + sysarg)
                await asyncio.sleep(3)
                audio = await conv.get_response()
                if "Looks like" in audio.text:
                    await audio.click(0)
                    await asyncio.sleep(2)
                    audio = await conv.get_response()
                    await event.delete()
                    await borg.send_file(
                        event.chat_id,
                        audio,
                        caption=f"**List of feds {user} has been banned in.\n\nƒѕтαт ¢нє¢к ву {DEVIL} 🔥\n\n¢σℓℓє¢тє∂ ву BLACK_MAMBA вσт.**",
                    )
                   
                else:
                    await ok.edit(audio.text + "\n\n **Cʜᴇᴄᴋᴇᴅ ʙʏ BLACK_MAMBA...**")
                
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` **@MissRose_Bot** `and try again!`")



@borg.on(admin_cmd(pattern="fedinfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Extracting information...`")
    sysarg = event.pattern_match.group(1)
    async with borg.conversation(bot) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/fedinfo " + sysarg)
            await asyncio.sleep(2)
            audio = await conv.get_response()
            await ok.edit(audio.text + "\n\nƒє∂ ιηƒσ єχтяα¢тє∂ ву BLACK_MAMBA вσт")
        except YouBlockedUserError:
            await ok.edit("**Error**\n `Unblock` **@MissRose_Bot** `and try again!")


@borg.on(admin_cmd(pattern="myfeds"))
async def myfeds(event):
  BLACK_MAMBA = await event.edit("`Wᴇɪᴛ ᴍᴀsᴛᴇʀ ᴄʜᴇᴄᴋɪɴɢ ʏᴏᴜʀ ᴀʟʟ ғᴇᴅs...``")
  async with borg.conversation(bot) as rose:
    await rose.send_message("/start")
    await rose.get_response()
    await rose.send_message("/myfeds")
    pro = await rose.get_response()
    if "Looks like" in pro.text:
      await pro.click(0)
      await asyncio.sleep(1.5)
      pro = await rose.get_response()
      await borg.send_file(event.chat_id, pro, caption='**Cʜᴇᴄᴋᴇᴅ ʙʏ BLACK_MAMBA ฅ^•ﻌ•^ฅ**')
    else:
      await BLACK_MAMBA.edit(pro.text + "\n\n**Cʜᴇᴄᴋᴇᴅ ʙʏ BLACK_MAMBA ฅ^•ﻌ•^ฅ**")
CMD_HELP.update(
    {
        "fedstuff": ".fstat <username/userid/reply to user>\nUse - To check the persons fedban stat in @MissRose_Bot.\
        \n\n.fedinfo <fedid>\nUse - To see info about the fed."
    }
)