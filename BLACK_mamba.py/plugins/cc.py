# Ported by TIMEX_OF_CLOCK
# Original By 
# @THE_B_LACK_HAT
# @danish_00
# Card Generator
##############################
from faker import Faker as dc
from BLACK_MAMBA.utils import admin_cmd as devil_cmd
from BLACK_MAMBA import bot as devil
@devil.on(devil_cmd("cc"))
async def _devil(dark):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    alain = cyber.credit_card_full()
    await dark.edit(f"ℕ𝕒𝕞𝕖:-\n`{killer}`\n\n𝔸𝕕𝕕𝕣𝕖𝕤𝕤:-\n`{kali}`\n\nℂ𝕒𝕣𝕕:-\n`{alain}`")
