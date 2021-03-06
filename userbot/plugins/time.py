""" It does not do to dwell on dreams and forget to live
Syntax: .getime"""

import asyncio
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd


FONT_FILE_TO_USE = "Fonts/digital.ttf"


@borg.on(admin_cmd("time ?(.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    current_time = datetime.now().strftime("INFORMASI ZONA WAKTU\n\nLOKASI : MAKASSAR, INDONESIA\n   WAKTU : %H:%M:%S \n   TANGGAL: %d.%m.%y \n\nSAM RAMADHAN")
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    reply_msg_id = event.message.id
    if input_str:
        current_time = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    # pylint:disable=E0602
    required_file_name = Config.TMP_DOWNLOAD_DIRECTORY + " " + str(datetime.now()) + ".webp"
    img = Image.new("RGBA", (350, 220), color=(170, 219, 255, 255))
    fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
    drawn_text = ImageDraw.Draw(img)
    drawn_text.text((12, 12), current_time, font=fnt, fill=(0, 0, 255))
    img.save(required_file_name)
    await borg.send_file(  # pylint:disable=E0602
        event.chat_id,
        required_file_name,
        caption="Sam Ramadhan",
        # Courtesy: @ManueI15
        reply_to=reply_msg_id
    )
    os.remove(required_file_name)
    end = datetime.now()
    time_taken_ms = (end - start).seconds
    await event.edit("Membuat stiker dalam {} detik".format(time_taken_ms))
    await asyncio.sleep(5)
    await event.delete()


@borg.on(admin_cmd("gtime (.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    logger.info(input_str)  # pylint:disable=E0602
