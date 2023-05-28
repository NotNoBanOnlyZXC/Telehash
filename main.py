import os
def clear():
    os.system('cls')
print('Starting...')
clear()
lng = input('Choose your language\n1: English\n2: Русский\nLanguage: ')
languages = ['en','ru']
from config import ru, en
if lng == "1":
    lang = en
elif lng == "2":
    lang = ru

def ln(id):
    return(lang[id])
clear()
print(ln(0))
print(ln(5))
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import time
import integrate as grate
from config import api_id, api_hash, v, heart1, georg, heart2
accs = ['new',]
clear()
print(ln(1))
with os.scandir('.') as it:
    x = 0
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.rsplit(".")[1] == 'session':
            x = x+1

            print(f'{x}: {entry.name.split(".")[0]}')
            accs.append(entry.name.split(".")[0])
print('----------------')
inp = input(ln(2))
clear()
print(f'{ln(3)} {accs[int(inp)]}...')
user = accs[int(inp)]
clear()
print(f'{ln(17)} {accs[int(inp)]}')
time.sleep(1)
if accs[int(inp)] == 'new':
    user = input(ln(4))
    print(ln(5))
    time.sleep(1)
name = os.getenv('username')

client = Client(user, api_id, api_hash, (f"Bot v.{v} | {languages[int(lng)-1]}"), (f"Telehash on {name}'s device"))

@client.on_message(filters.command("type", prefixes='!') & filters.me)
def type(client_object, message: Message):
    input_text = message.text.split("!type ", maxsplit=1)[1]
    temp_text = input_text
    edited_text = ""
    typing_symbol = "I"

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
    print('\n')
    try:
        if message.text.split(' ')[1] == '1':
            heart = heart1
        elif message.text.split(' ')[1] == '2':
            heart = heart2
        for i in range(len(heart)):
            print(f'{ln(6)} {len(heart)-i-1}', end='\r ')
            message.edit(heart[i])
            time.sleep(0.2)
    except:
        print(ln(14))
    print(ln(8) + '                                            ')

@client.on_message(filters.command('rib', prefixes='!') & filters.me)
def rib(client_object, message: Message):
    print('\n')
    message.edit(ln(10))
    for o in range(4):
        for i in range(4):
            print(f'{ln(9)} {len(georg)*o-i*o-1}', end=' \r')
            message.edit(georg[i])
            time.sleep(0.6)
    for i in range(4, len(georg)):
        print(f'{ln(9)} {len(georg)*o-i*o-1}', end=' \r')
        message.edit(georg[i])
        time.sleep(0.6)
    print(ln(8) + '                                            ')

@client.on_message(filters.command("au", prefixes='!') & filters.me)
def au(clients_object, message: Message):
    try:
        message.edit(f'{ln(7)} {message.from_user.first_name}')
        client.join_chat('@telehashdev')
    except:
        pass

@client.on_message(filters.command('spoti', prefixes='!') & filters.me)
def spot(clients_object, message: Message):
    try:
        author, song = grate.spotify()[1], grate.spotify()[2]
        message.edit(f'{ln(11)[0]}\n{ln(11)[1]}{author}\n{ln(11)[2]}{song}')
    except:
        pass

@client.on_message(filters.command('', prefixes='.') & filters.me)
def tochka(client_object, message: Message):
    message.delete()
    client.send_message(message.chat.id, (f'{ln(13)}{message.reply_to_message.from_user.first_name}'))
    client.copy_message(message.chat.id, message.chat.id, message.reply_to_message.id)

@client.on_message(filters.command('roll', '!') & filters.me)
def roll(client_object, message: Message):
    try:
        frm = message.text.split(' ')[1]
        to = message.text.split(' ')[2]
        message.edit(f'{message.from_user.first_name} {ln(15)} **{grate.roll(frm, to)}** [{frm}-{to}]')
    except:
        message.edit('attributes missing')

@client.on_message(filters.command('try', '!') & filters.me)
def trry(client_object, message: Message):
    try:
        right = message.text.split(' ', 1)[1]
        message.edit(f'{right.capitalize()}: **{ln(16)[grate.trry()]}**')
    except:
        message.edit('attributes missing')

if lng == '1':
    print(f'Hello, You`re using Telehash with version v.{v}\nChat commands list\n\n!type [text] - type your text letter to letter\n!heart [1-2] - send animated heart\n!au - send author+user information, sub to our news channel\n!rib - send animated Georges ribbon (event on may, 9)\n!spoti - send the song you are listening to to the chat (Restrictions: Spotify, Windows, exe application)\n. - forward message\n!roll [from] [to] - send a random value between from and to \n!try [question] - get the answer to the question in the form of false/true')
    print('----------')
    print(ln(12))
elif lng == '2':
    print(f'Привет, Вы используете Telehash на версии v.{v}\nСписок команд для чата\n\n!type [text] - написать Ваше сообщение побуквенно\n!heart [1-2] - отправить анимированное сердце\n!au - отправить информацию о разработчике и пользователе, подписаться на новостной канал\n!rib - отправить анимированную Георгиевскую ленту (событие на 9 мая)\n!spoti - отправить прослушиваемую песню в чат (Ограничения: Spotify, Windows, exe-приложение)\n. - переслать сообщение\n!roll [от] [до] - отправить случайное значение между от и до\n!try [вопрос] - получить ответ на вопрос в виде ложь/истина')
    print('----------')
    print(ln(12))
# После клиента части бота не ставить
client.run()