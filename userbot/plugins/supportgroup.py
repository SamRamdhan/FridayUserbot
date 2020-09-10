"""Emoji
Available Commands:
.support
Credits to noone
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("gabut"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "support":
    await event.edit("Kegabutan")
    animation_chars = [
            "Asal Coret",
            "[Ruang Aksara](https://t.me/AsalCoret)"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
