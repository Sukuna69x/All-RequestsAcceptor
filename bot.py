import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQFJ9mQAcOb_pbrDY2ll1WAeQDMDEn1HlggUZIfw3BBrV224U0cPlgS8s9NmqBq4Jt0xSs-3UZt3LIBaxAShuSmFHbMsMHwO_AHDDY-7mubNye1ZAkPaKn5Q9-SjPsZo-osTFPVGQM7EzjYzW1-MfUY_3CgzoXwtznLk7tw1qC53pHxss-NdqkNCpByDM8zkhUWCbWnTIWrJUnmhq4Cfinv4tgJhqTXNH0xQHdunECDZF0lFvVxJb0kVRKhjYLcsJ9NvttdzqYuDnqfgZo0bE5SCEz89QN9XmXfDeKVJETLM3bv0q8JScWr0pabMgC4TQFx-isQqTKnRtL3YkWIYN6HwlthVZQAAAAG9uewXAA")        
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







