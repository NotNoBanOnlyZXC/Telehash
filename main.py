from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import time
import os
from config import api_id, api_hash, v, chearts
accs = ['new',]
with os.scandir('.') as it:
    x = 0
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.rsplit(".")[1] == 'session':
            x = x+1

            print(f'{x}: {entry.name.split(".")[0]}')
            accs.append(entry.name.split(".")[0])
print('---------------')
inp = input('Choose account (0 for new): ')
print(f'Entering {accs[int(inp)]}...')
user = accs[int(inp)]
print('---------------')
time.sleep(1)
if accs[int(inp)] == 'new':
    user = input('Okay. A new account. How to name it?\n')
    print('Wait...')
    time.sleep(1)
name = os.getenv('username')

client = Client(user, api_id, api_hash, (f"Bot v.{v}"), (f"Telehash on {name}'s device"))
print(f'Hello, You`re using Telehash with version v.{v}\nChat commands list\n\n!type [text] - type your text letter to letter\n!heart - send animated heart')

@client.on_message(filters.command("type", prefixes='!') & filters.me)
def type(client_object, message: Message):
    input_text = message.text.split("!type ", maxsplit=1)[1]
    temp_text = input_text
    edited_text = ""
    typing_symbol = "```I```"

    while edited_text != input_text:
        try:
            message.edit(edited_text + typing_symbol)
            time.sleep(0.03)
            edited_text = edited_text + temp_text[0]
            temp_text = temp_text[1:]
            message.edit(edited_text)
            time.sleep(0.03)
        except:
            pass

@client.on_message(filters.command("heart", prefixes='!') & filters.me)
def hearts(client_object, message: Message):
    for i in range(len(chearts)):
        print(i)
        message.edit(chearts[i])
        print(chearts[i])
        time.sleep(0.3)
client.run()