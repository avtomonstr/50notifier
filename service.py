from telethon import TelegramClient, events, utils
from telethon.tl.types import PeerChannel,PeerChat
import json
import os
import configparser

# reading config from config.ini file
config = configparser.ConfigParser(allow_no_value=True)
config.optionxform=str
config.read('config.ini')

api_id = config['Default']['api_id']
api_hash = config['Default']['api_hash']
phone = config['Default']['phone']
channel_id = config['Default']['channel_id']
sticker_id = config['Default']['sticker_id']
msg = config['Default']['message']

#client instance creation
client = TelegramClient(phone, api_id, api_hash)

# handling messages from channel
@client.on(events.NewMessage(chats=[PeerChannel(channel_id=channel_id)]))
async def handler(event):
    # check if there is a sticker and if it is one of needed
    if event.message.sticker and (event.message.sticker.id==sticker_id or event.message.sticker.id==5195025178035240381):
        print("отправлено")
        # send link without preview back
        await client.send_message(PeerChannel(channel_id=1476750856), message=msg, link_preview=False)

client.start()
client.run_until_disconnected()
