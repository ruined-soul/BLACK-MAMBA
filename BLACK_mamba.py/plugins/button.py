
# COPYRIGHT (C) 2021-2022 BY TIMEX_OF_CLOCK
# MADE BY TIMEX_OF_CLOCK
from telethon import Button, events
from ..utils import admin_cmd
from ..utils import edit_or_reply, eor
from ..utils import sudo_cmd
from .. import CMD_HELP

@borg.on(admin_cmd(pattern="button (.*)"))
@borg.on(sudo_cmd(pattern="button", allow_sudo=True))
async def Buttons(event):
    await eor(event, "`Mᴀᴋɪɴɢ Yᴏᴜʀ Bᴜᴛᴛᴏɴ ᴡᴇɪᴛ ᴍᴀsᴛᴇʀ !!!`")
    BLACK_MAMBA = Var.TG_BOT_USER_NAME_BF_HER
    pro = event.text[7:]
    pro, boy = pro.split("|")
    f = open("Button.txt", "w") # by TIMEX_OF_CLOCK, PROBOYX
    f.write(f'{pro}\n{boy}')
    f.close()
    BLACK_MAMBA = await bot.inline_query(BLACK_MAMBA, "BUTTON")
    await BLACK_MAMBA[0].click(event.chat_id)
    await event.delete()

@xbot.on(events.InlineQuery(pattern='BUTTON'))
async def file(event):
  f = open("Button.txt")
  ok = f.readlines()[0]
  f.close()
  PROBOYX = open("Button.txt")
  bc = PROBOYX.readlines()[1]
  PROBOYX.close()
  BLACK_MAMBA = event.builder
  TIMEX_OF_CLOCK = [[Button.url(f'{ok}', f'{bc}')]]
  PROBOYXOP = BLACK_MAMBA.article(title='Button by ULTRA X', text=f'{ok}', buttons=TIMEX_OF_CLOCK)
  await event.answer([PROBOYXOP])

CMD_HELP.update
(
  {
    "button": ".button <button name>|<link>\n`.button BLACK_MAMBA|https://t.me/BLACK_MAMBA_SUPPORT`\nmake sure your name and link no have Useless space"
  }
)
