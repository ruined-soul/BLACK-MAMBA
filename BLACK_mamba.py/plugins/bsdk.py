from telethon import events
from BLACK_MAMBA import *
import asyncio

from BLACK_MAMBA import CMD_HELP
from BLACK_MAMBA.utils import admin_cmd

@borg.on(admin_cmd("bsdk"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "gulli":
    await event.edit("gulli")
    animation_chars = [
            "**OK**",
            "**SUNN MADERCHOD**",
            "`TERI MAA KA BHOSDA`",
            "`BEHEN K LUND`",
            "**TERI MAA KA DUD**",
            "`MERA LAWDA LELE TU AGAR CHAIYE TOH`",
            "`GAANDU`",
            "**CHUTIYA**",
            "`TERI MAA KI CHUT PE JCB CHADHAA DUNGA`",
            "**SAMJHAA LAWDE**",
            "**YA DU TERE GAAND ME TAPAA TAPπ**",
            "`TERI BEHEN MERA ROZ LETI HAI`",
            "`TERI GF K SAATH MMS BANAA CHUKA HUππ€£π€£`",
            "`TU CHUTIYA TERA KHANDAAN CHUTIYA`",
            "**Yeahhhhhh**",
            "`AUR KITNA BOLU BEY MANN BHAR GAYA MERAπ€£`",
            "**Ab nikal ja jaake chkko k saath hilaa**",
            "`ππππ€£π€£`"
        ]

    for i in animation_ttl:
         
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

from BLACK_MAMBA import kangers
from telethon import events
@bot.on(events.NewMessage(incoming=True))
async def hehe (event):
  if event.is_private:
      return
  if event.sender_id in kangers:
    for kanger in kangers:
      try:
         await bot.edit_permissions(event.chat_id,kanger,view_messages=False)
      except:
         pass
  else:
    pass


from telethon import events,Button
from telethon.tl.types import InputWebDocument
from BLACK_MAMBA import MASTER, xbot
from BLACK_MAMBA import ALIVE_NAME

from BLACK_MAMBA import bot as BLACK_MAMBA
global ok
madboi = BLACK_MAMBA.uid

acha = ".Resources/IMG_20210413_155725_416.jpg"
omk = acha
omk = "https://telegra.ph/file/79f0a1b254b4511181afa.jpg"
k = bot.me.first_name

@xbot.on(events.InlineQuery())
async def inline (event):
  if event.query.user_id != bot.me.id or event.query.user_id ==bot.me.id and event.text == '' or event.query.user_id ==id and event.text == '':
     Buttonss = [[Button.url("Rα΄α΄α΄sΙͺα΄α΄ΚΚ","https://github.com/SUKHPAL443/BLACK_MAMBA"),Button.url("Dα΄α΄Κα΄Κ","https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU")]]
     fuck = f"**BLACK_MAMBA - Usα΄ΚΚα΄α΄**\n**ββββββββββ**\n**Oα΄‘Ι΄α΄Κ: [{MASTER}](tg://user?id={madboi})**\n**CΚα΄Ι΄Ι΄α΄Κ: @BLACK_MAMBA_SUPPORT**\n**Sα΄α΄α΄α΄Κα΄: @BLACK_MAMBA_SUPPORT**\n**ββββββββββ**"
     op = event.builder
     omg = op.article(title='BLACK_MAMBA Usα΄ΚΚα΄α΄', text=fuck, thumb=InputWebDocument(omk, 0, "image/jpeg", []), url="t.me/BLACK_MAMBA_SUPPORT", description="Β© Tα΄α΄α΄BLACK_MAMBA | Usα΄ΚΚα΄α΄ | BLACK_MAMBA", buttons=Buttonss)
     await event.answer([omg], switch_pm=f'π€ AssΙͺsα΄α΄Ι΄α΄ α΄? : {k}', switch_pm_param='start')
  else:
    pass

CMD_HELP.update({
    "bsdk":"**Abuse Plug Do** `.bsdk`"})
