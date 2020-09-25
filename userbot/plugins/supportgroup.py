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
    animation_interval = 4
    animation_ttl = range(0,3)
    #input_str = event.pattern_match.group(1)
   # if input_str == "support":
    await event.edit("Gabut?")
    animation_chars = [
            "Gabung Sini Aja",
            "[Kerabat Online](https://t.me/KerabatOnline)"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
