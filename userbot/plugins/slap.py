"""
SLAP Plugin For Userbot
usage:- .slap in reply to any message, or u gonna slap urself.

"""

import sys
from telethon import events, functions
from uniborg.util import admin_cmd
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from userbot import ALIVE_NAME

SLAP_TEMPLATES = [
    "{user1} {hits} {user2} memakai {item}.",
    "{user1} {hits} {user2} dengan keras menggunakan {item}.",
    "{user1} {hits} {user2} menggunakan {item}.",
    "{user1} {throws} sebuah {item} ke wajah {user2}.",
    "{user1} mengambil {item} kemudian {throws} ke {user2} hingga terkapar.",
    "{user1} melempar {item} ke {user2} hingga sekarat.",
    "{user1} memfitnah {user2} telah mencuri {item}.",
    "{user1} berdiri dibelakang {user2} kemudian {hits} menggunakan {item}.",
    "{user1} meraih sebuah {item} lalu {hits} {user2} dengan keras.",
    "{user1} membanting {user2} ke lantai kemudian {throws} sebuah {item} dengan keras.",
    "{user1} mendorong dengan keras {user2} ke jurang penyesalan paling dalam."
]

ITEMS = [
    "majalah bobo",
    "sendal swallow",
    "helm gojek",
    "TV tabung",
    "HP nokia jadul",
    "batu bata",
    "panci panas",
    "tameng Brimob",
    "pentungan hansip",
    "powerbank",
    "sepatu laras",
    "spion kopaja",
    "patung Hitler",
    "ranting pohon",
    "semvak firaun",
    "roda becak",
    "velg NMAX",
    "tromol ninja",
    "stang motor supra",
    "galon AQUA",
    "botol marjan",
    "ransel Tentara",
    "sepatu Polisi",
    "tumpukan batako",
    "wajan gosong",
    "sepeda lipat",
    "mesin las",
    "ban truk",
    "gesper Kopassus",
]

THROW = [
    "memukulkan",
    "melemparkan",
    "menamparkan",
    "memukulkan",
]

HIT = [
    "memukul",
    "menggeplak",
    "menampol",
    "menampar",
    "menghantam",
]

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "FridayUserbot"

@borg.on(admin_cmd(pattern="slapp ?(.*)", allow_sudo=True))
async def who(event):
    if event.fwd_from:
        return
    replied_user = await get_user(event)
    caption = await slap(replied_user, event)
    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    try:
        await event.edit(caption)

    except:
        await event.edit("`Makhluk halus gabisa dislap!!`")

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`Ga bisa ngeslap Hantu!!`")
            return None

    return replied_user

async def slap(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username
    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)
    item = random.choice(ITEMS)
    hit = random.choice(HIT)
    throw = random.choice(THROW)

    caption = temp.format(user1=DEFAULTUSER, user2=slapped, item=item, hits=hit, throws=throw)

    return caption
