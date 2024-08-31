import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQFm0Aip3sPLHXACllLaq4wd-Z2HJcWuZR7ETLffo-_rJdoRZjHip5CxrfJrP-tUAolrKzDV0y7O8Ca6ah7FeVZ0u9nB72SBNf1u68IWPLbvCBEgI0s0dfgEPdalTv_wgDU13id-x-sdHrD-Yi5g270_psbsOdN271ZoBfx45TSnUKIK8N-0She0udfXcTy06n5V8OOh1LN-PZp4H4jB_jSwOSHlHeKbyqnE1iJAwu5eRk-LsSn9Hi4-dPO_Q6Qiiom16oMOD6F4mu3jq52w1X8SaxX07nq_0xPmSwhh4ER9PVuYQ1LC44lIQ6AZ_WDClOnKBzPmzx5cena_MQfgLQvBTZ9wAAAAGHQ9QeAA")        
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
