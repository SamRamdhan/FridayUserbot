"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd




@borg.on(admin_cmd(pattern=r"(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 10)

    input_str = event.pattern_match.group(1)

    if input_str == "fakboi":

        await event.edit(input_str)

        animation_chars = [
        
            "`Hai kamu`",
            "`Akan kuberikan semua sisa kasih sayang yang aku punya`",
            "`Proses mentransfer\n\n\n\nTunggu sebentar\n\nMemulai... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mentransfer\n\n\nTunggu sebentar\nJangan pergi\n\nSedang proses...\n\nPersentase... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mentransfer\n\n\nTunggu sebentar\nJangan pergi\n\nSedang proses...\n\nPersentase... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Mentransfer\n\n\nTunggu sebentar\nJangan pergi\n\nSedang proses...\n\nPersentase... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mentransfer\n\n\nTunggu sebentar\nJangan pergi\n\nSedang proses...\n\nPersentase... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mentransfer\n\n\nTunggu sebentar\nJangan pergi\n\nSedang proses...\n\nPersentase... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mentransfer\n\n\nTunggu sebentar\nJangan pergi\n\nSebentar lagi...\n\nPersentase... 84%\n█████████████████████▒▒▒▒ `",
            "`Mentransfer\n\n\nSedang memuat\nTunggu sebentar\n\nSelesai...\n\nPersentase... 100%\n█████████████████████████ `",
            "`Proses transfer sukses dilakukan\n\n\nSekarang semua kasih sayangku telah menjadi milikmu semuanya\nSemoga cukup untuk bisa membuatmu menjadi milikku\n\nDan semoga mampu membuatmu bahagia\n\nI Love You` 🤗"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])

@borg.on(admin_cmd(pattern=r"(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "sqh":

        await event.edit(input_str)

        animation_chars = [
        
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult: No Virus Found...`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])


@borg.on(admin_cmd(pattern=r"(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "vquickheal":

        await event.edit(input_str)

        animation_chars = [
        
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult:⚠️Virus Found⚠️\nMore Info: Torzan, Spyware, Adware`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
