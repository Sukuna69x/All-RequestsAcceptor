import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQFJ9mQAG0YuZDg0TYiiN4vYr9AeGQBig7B2YY7Hg8g3dV-dp9SucRRA5UbeDmbvvnivGr1moAxTDu-Nby1aXHVe7CpXD7P-7F9FYZ4fIHZShjYA3UJke0Lm51o9TsmY5xYHibI5PJv4OnGCT5J3oQ2UsGn-rS-Cjt5J3d69dz1MdCfUIdFaX38lxtvOWu02aLKYa_mWn4f51CeTD_RPFLADfFcROWOvoadiEIAhhkiKJ7A5mzsUus_YKbvhMm4RRGGnYwZLlG3rXk98L0g8qdeaI-JrBz0EjK8jvGG1ixbGbXFM0CKVFtyJ2xITnjY3pr5DRjd36-WYBUS8VwGiWYNhCCeKgAAAAAG9uewXAA")        
User = Client(name="AcceptUser", session_string=SESSION)


@User.on_message(filters.command(["run", "approve"], [".", "/"]))                     
async def approve(client, message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq to accept within seconds 💀
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await msg.delete()


logging.info("Bot Started....")
User.run()







