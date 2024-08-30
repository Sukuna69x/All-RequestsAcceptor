import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQFm0AUbAb3bHpMQcT_Xn8r_zPvafOBkz7mqlXjr7osnVz-rYrwaMhjmANSBxiq3mJp9vU2fZLWW5xMZCeR-ultYn_bjQAzYBCoELlPqa5P9kM5TE6-bKzRpcsoIXNEE-KHgmHJHBWSDh6N6hC4NEhFlLRA0yN5GHjBnojj4stNvGZyOF5Hc4cBiczX4iP11LgrCTdYSn6R8Z839KXFO4wQWAif65JNYBz6tsvC1YLDfaayWw4zU7fhYNx2qHRJccz9c2ObnG_Xecr9wO5rEnuEXyzZFc_J4g863G5JYn_RigjMlGX10Lj4DEqLJU0Z2GwlAlTupbTmWoBclV-nHR4XNPwAAAAGHQ9QeAA")        
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
