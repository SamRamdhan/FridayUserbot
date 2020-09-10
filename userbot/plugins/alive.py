"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/8ad91e47be4fb6027d858.jpg"
pm_caption = "`USERBOT :` **AKTIF**\n\n"
pm_caption += "**PROFIL PENGGUNA**\n"
pm_caption += "**NAMA** : `SAM RAMADHAN`\n`a.k.a :` **SAM**\n"
pm_caption += "**JENIS KELAMIN** : `LAKI-LAKI`\n"
pm_caption += "**DOMISILI** : `MAKASSAR, INDONESIA`\n"
pm_caption += "**UMUR** : `GAADA YANG TAU`\n"
pm_caption += "**HOBBY** : `IBADAH`\n"
pm_caption += f"**USERNAME** : {DEFAULTUSER} \n"
pm_caption += "**GROUP SAYA** : @KerabatOnline\n\n"
pm_caption += "• [Kerabat Online Twitter](https://twitter.com/KerabatOnline)\n"
pm_caption += "• [Kerabat Online Channel](https://t.me/KerabatOnline_Ch)\n"
pm_caption += "• [Kerabat Moments](https://t.me/KerabatMoments)"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)

    
