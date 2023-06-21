print('Starting...')
import os, time
from pyrogram import filters, Client
from pyrogram.raw import functions
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import integrate as grate
import concurrent.futures
from config import api_id, api_hash, v, heart1, georg, heart2, ghoul

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
time.sleep(0.5)
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
user = accs[int(inp)]
clear()
print(f'{ln(3)} {user}...')
clear()
print(f'{ln(17)} {user}')
time.sleep(0.5)
if user == 'new':
    user = input(ln(4))
    print(ln(5))
    clear()
    newuser = Client(user, api_id, api_hash, (f"Bot v.{v} | {languages[int(lng)-1]}"), (f"Telehash registering..."))
    newuser.start()
    newuser.stop()
    

name = os.getenv('username')
if name == None:
    name = "User"

import sqlite3
conn = sqlite3.connect(f'{user}.db', check_same_thread=False)
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS messages(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name INTEGER NOT NULL,
             message INTEGER NOT NULL);''')
clear()
desc = input(f'[BETA] {ln(23)[0]}\n1 - Yes\n0 - No\n')
if desc == '1':
    cur.execute('''CREATE TABLE IF NOT EXISTS profile(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             val TEXT NOT NULL,
             type TEXT NOT NULL);''')
    cur.execute('''CREATE TABLE IF NOT EXISTS settings(
             key TEXT NOT NULL,
             val TEXT NOT NULL);''')
    
    cur.execute("SELECT EXISTS(SELECT 1 FROM settings WHERE key='name_interval' LIMIT 1)")
    result = cur.fetchone()
    if result[0] == 0:
        cur.execute("INSERT INTO settings (key, val) VALUES (?, ?)", ('name_interval', '60'))
    cur.execute("SELECT EXISTS(SELECT 1 FROM settings WHERE key='desc_interval' LIMIT 1)")
    result = cur.fetchone()
    if result[0] == 0:
        cur.execute("INSERT INTO settings (key, val) VALUES (?, ?)", ('desc_interval', '60'))
    conn.commit()

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

@client.on_message(filters.command("au", prefixes='!'))
def au(clients_object, message: Message):
    try:
        message.edit(f'{ln(7)} {message.from_user.first_name}')
        client.join_chat('@telehashdev')
    except:
        message.reply(f'{ln(7)} {message.from_user.first_name}')
        client.join_chat('@telehashdev')

@client.on_message(filters.command('spoti', prefixes='!') & filters.me)
def spot(clients_object, message: Message):
    try:
        author, song = grate.spotify()[1], grate.spotify()[2]
        message.edit(f'{ln(11)[0]}\n{ln(11)[1]}{author}\n{ln(11)[2]}{song}')
    except:
        pass

@client.on_message(filters.command('.', prefixes='.') & filters.me)
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

@client.on_message(filters.command('add', '!') & filters.me)
def addtext(client_object, message: Message):
    namex = message.text.split() # namex[1]
    textx = message.reply_to_message.text
    print(f'!add received with name "{namex[1]}", saving with text "{textx}"...')
    try:
        cur.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (namex[1], textx))
        conn.commit()
        message.edit(ln(19)[0])
        time.sleep(2)
        message.delete()
    except:
        message.edit(ln(19)[1])
        time.sleep(2)
        message.delete()

@client.on_message(filters.command('del', '!') & filters.me)
def deltext(client_object, message: Message):
    id = message.text.split()[1]
    try:
        typ = message.text.split()[2]
        if not typ == 'name' and not typ == 'id':
            typ = 'name'
    except:
        typ = 'name'
    if typ == 'name':
        try:
            cur.execute("DELETE FROM messages WHERE name=?", (id,))
            conn.commit()
            message.edit(ln(21)[0])
            time.sleep(2)
            message.delete()
        except:
            message.edit(ln(21)[1])
            time.sleep(2)
            message.delete()
    elif typ == 'id':
        try:
            cur.execute("DELETE FROM messages WHERE id=?", (id,))
            conn.commit()
            message.edit(ln(21)[0])
            time.sleep(2)
            message.delete()
        except:
            message.edit(ln(21)[1])
            time.sleep(2)
            message.delete()

@client.on_message(filters.command('put', '!') & filters.me)
def put(client, message: Message):
    id = message.text.split()[1]
    try:
        typ = message.text.split()[2]
        if not typ == 'name' and not typ == 'id':
            typ = 'name'
    except:
        typ = 'name'
    if typ == 'name':
        try:
            cur.execute("SELECT message FROM messages WHERE name=?", (id,))
            message.edit(cur.fetchone()[0])
        except:
            message.edit(ln(21)[1])
            time.sleep(2)
            message.delete()
    elif typ == 'id':
        try:
            cur.execute("SELECT message FROM messages WHERE id=?", (id,))
            message.edit(cur.fetchone()[0])
        except:
            message.edit(ln(21)[1])
            time.sleep(2)
            message.delete()

@client.on_message(filters.command('list', '!') & filters.me)
def list(client, message: Message):
    cur.execute("SELECT id, name FROM messages")
    rows = cur.fetchall()
    all = ln(20)
    for row in rows:
        all = f'{all}\n{row[0]} - {row[1]}'
    message.edit(all)
        
@client.on_message(filters.command('ghoul', '!') & filters.me)
def ghoul_activate(client, message: Message):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(ghoul1, client, message)
        executor.submit(ghoul2, client, message)

@client.on_message(filters.command('name', '!') & filters.me)
def name_r(client, message:Message):
    if desc == '1':
        sp = message.text.split()
        if sp[1] == 'list':
            cur.execute("SELECT id, val FROM profile WHERE type=?", ('name',))
            rows = cur.fetchall()
            all = ln(20)
            for row in rows:
                all = f'{all}\n{row[0]} - {row[1]}'
            message.edit(all)
        elif sp[1] == 'add':
            try:
                cur.execute('INSERT INTO profile (val, type) VALUES (?, ?)', (sp[2], 'name'))
                conn.commit()
                message.edit(ln(19)[0])
                time.sleep(2)
                message.delete()
            except:
                message.edit(ln(19)[1])
                time.sleep(2)
                message.delete()
        elif sp[1] == 'del':
            try:
                cur.execute('DELETE FROM profile WHERE id=?', (sp[2],))
                conn.commit()
                message.edit(ln(19)[0])
                time.sleep(2)
                message.delete()
            except:
                message.edit(ln(19)[1])
                time.sleep(2)
                message.delete()
        elif sp[1] == 'int':
            cur.execute('REPLACE INTO settings (key, val) VALUES (?, ?)', ('name_interval', sp[2]))
            conn.commit()
    elif desc == '0':
        message.edit('BETA not enabled')
        time.sleep(2)
        message.delete()
            

@client.on_message(filters.command('desc', '!') & filters.me)
def desc_r(client, message:Message):
    if desc == '1':
        sp = message.text.split()
        if sp[1] == 'list':
            cur.execute("SELECT id, val FROM profile WHERE type=?", ('desc',))
            rows = cur.fetchall()
            all = ln(20)
            for row in rows:
                all = f'{all}\n{row[0]} - {row[1]}'
            message.edit(all)
        elif sp[1] == 'add':
            try:
                cur.execute('INSERT INTO profile (val, type) VALUES (?, ?)', (sp[2], 'desc'))
                conn.commit()
                message.edit(ln(19)[0])
                time.sleep(2)
                message.delete()
            except:
                message.edit(ln(19)[1])
                time.sleep(2)
                message.delete()
        elif sp[1] == 'del':
            try:
                cur.execute('DELETE FROM profile WHERE id=?', (sp[2],))
                conn.commit()
                message.edit(ln(19)[0])
                time.sleep(2)
                message.delete()
            except:
                message.edit(ln(19)[1])
                time.sleep(2)
                message.delete()
        elif sp[1] == 'int':
            cur.execute('REPLACE INTO settings (key, val) VALUES (?, ?)', ('desc_interval', sp[2]))
            conn.commit()
    elif desc == '0':
        message.edit('BETA not enabled')
        time.sleep(2)
        message.delete()

def ghoul1(client, message: Message):
    message.edit(ln(22)[0])
    time.sleep(1)
    message.edit(ln(22)[1])
    time.sleep(1)
    a = 1000
    b = ''
    while a >= 0:
        time.sleep(0.15)
        b = f'{b} {a}-7'
        message.edit(b)
        a -= 7

def ghoul2(client, message: Message):
    sm = message.reply('Let let let me die')
    for i in range(len(ghoul)):
        time.sleep(0.6)
        sm.edit_text(ghoul[i])

@client.on_message(filters.command('init', '!') & filters.me)
def inithere(client, message:Message):
    cur.execute('SELECT val FROM profile WHERE type=?', ('name',))
    names = cur.fetchall()
    print(names)
    #while True:


#@client.on_message()
#def all(client_object, message: Message):
#    print(f'{message.from_user.first_name}: {message.text}')
clear()
if lng == '1':
    print(f'Hello, You`re using Telehash with version v.{v}\nChat commands list\n\n!type [text] - type your text letter to letter\n!heart [1-2] - send animated heart\n!au - send author+user information, sub to our news channel\n!rib - send animated Georges ribbon (event on may, 9)\n!spoti - send the song you are listening to to the chat (Restrictions: Spotify, Windows, exe application)\n. - forward message\n!roll [from] [to] - send a random value between from and to \n!try [question] - get the answer to the question in the form of false/true\n!add [name] - save message text (need be reply to another message) in DB with name\n!del [name] <name or id> - delete variable from database\n!put [name] <name or id> - put text with its name (or id)\n!list - list of saved vars')
    print('----------')
    if desc == '1':
        print(ln(23)[1])
    print(ln(12))
elif lng == '2':
    print(f'Привет, Вы используете Telehash на версии v.{v}\nСписок команд для чата\n\n!type [text] - написать Ваше сообщение побуквенно\n!heart [1-2] - отправить анимированное сердце\n!au - отправить информацию о разработчике и пользователе, подписаться на новостной канал\n!rib - отправить анимированную Георгиевскую ленту (событие на 9 мая)\n!spoti - отправить прослушиваемую песню в чат (Ограничения: Spotify, Windows, exe-приложение)\n. - переслать сообщение\n!roll [от] [до] - отправить случайное значение между от и до\n!try [вопрос] - получить ответ на вопрос в виде ложь/истина\n!add [имя] - сохранить текст сообщения (нужно отправлять ответом на сообщение) в базу данных под установленным именем\n!put [имя] <name или id> - вставить сохранённый текст под установленным именем (или id)\n!del [имя] <name или id> - удалить значение из базы данных\n!list - список сохранённых значений')
    print('----------')
    if desc == '1':
        print(ln(23)[1])
    print(ln(12))

# run на start не меняй, будет пиздец, 1 цикл вместо повтора
client.run()