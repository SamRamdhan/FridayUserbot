"""Emoji

Available Commands:

.ok"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("ok"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "ok":
    await event.edit("ok")
    animation_chars = [
            "OK",
            "BAIKLAH",
            "OK BRO",
            "OK SIS",
            "OK BANG",
            "OK BOSS",
            "OK GAES",
            "OK FANS",
            "IYA OK",
            "HMMMMMM",
            "OKEEEEEEEEEE",
            "MANTAP",
            "OK",
            "Boss",
            "Yeahhhhhh",
            "O",
            "K",
            "Ok Boss! 😎"
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
