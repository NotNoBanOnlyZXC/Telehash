from    config          import  text
from    datetime        import  datetime
startTime = datetime.now()
from    rich            import  print
from    rich.console    import  Console
from    rich.traceback  import  install
install()
print(text)
import  os, time, concurrent.futures, platform
import  random          as      r
from    threading       import  Event
from    pyrogram        import  filters, Client
from    pyrogram.raw    import  functions
from    pyrogram.types  import  Message
from    pyrogram.errors import  FloodWait
import  integrate       as      grate
from    config          import  api_id, api_hash, v, heart1, georg, heart2, ghoul
from    subprocess      import  Popen

def clear():
    os.system('cls')
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
chints = input(f'{ln(23)[0]}\n1 - Yes\n0 - No\n')
clear()
beta = input(ln(25)[0])
if chints == '1':
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
    cur.execute("SELECT EXISTS(SELECT 1 FROM settings WHERE key='chints_interval' LIMIT 1)")
    result = cur.fetchone()
    if result[0] == 0:
        cur.execute("INSERT INTO settings (key, val) VALUES (?, ?)", ('chints_interval', '60'))
    conn.commit()

if beta == '1':
    cur.execute('''CREATE TABLE IF NOT EXISTS variables(
             key TEXT NOT NULL,
             val TEXT NOT NULL)''')
    cur.execute("SELECT EXISTS(SELECT 1 FROM variables WHERE key='white' LIMIT 1)")
    result = cur.fetchone()[0]
    if result == 0:
        cur.execute("INSERT INTO variables (key, val) VALUES (?, ?)", ('white', '🤍'))

    cur.execute("SELECT EXISTS(SELECT 1 FROM variables WHERE key='blue' LIMIT 1)")
    result = cur.fetchone()[0]
    if result == 0:
        cur.execute("INSERT INTO variables (key, val) VALUES (?, ?)", ('blue', '💙'))

    cur.execute("SELECT EXISTS(SELECT 1 FROM variables WHERE key='red' LIMIT 1)")
    result = cur.fetchone()[0]
    if result == 0:
        cur.execute("INSERT INTO variables (key, val) VALUES (?, ?)", ('red', '❤'))
    
    cur.execute("SELECT EXISTS(SELECT 1 FROM variables WHERE key='green' LIMIT 1)")
    result = cur.fetchone()[0]
    if result == 0:
        cur.execute("INSERT INTO variables (key, val) VALUES (?, ?)", ('green', '💚'))
    conn.commit()

client = Client(user, api_id, api_hash, (f"Bot v.{v} | {languages[int(lng)-1]}"), (f"Telehash on {name}'s device"))
print(f'{ln(17)} {user}')
runTime = datetime.now()

@client.on_message(filters.command("type", prefixes='!') & filters.me)
def type(client, message: Message):
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
def hearts(client, message: Message):
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
def rib(client, message: Message):
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
def au(client, message: Message):
    try:
        message.edit(f'{ln(7)} {message.from_user.first_name}')
        client.join_chat('@telehashdev')
    except:
        message.reply(f'{ln(7)}')
        client.join_chat('@telehashdev')

@client.on_message(filters.command('spoti', prefixes='!') & filters.me)
def spot(client, message: Message):
    try:
        author, song = grate.spotify()[1], grate.spotify()[2]
        message.edit(f'{ln(11)[0]}\n{ln(11)[1]}{author}\n{ln(11)[2]}{song}')
    except:
        pass

@client.on_message(filters.command('.', prefixes='.') & filters.me)
def tochka(client, message: Message):
    message.delete()
    client.send_message(message.chat.id, (f'{ln(13)}{message.reply_to_message.from_user.first_name}'))
    client.copy_message(message.chat.id, message.chat.id, message.reply_to_message.id)

@client.on_message(filters.command('roll', '!') & filters.me)
def roll(client, message: Message):
    try:
        frm = message.text.split(' ')[1]
        to = message.text.split(' ')[2]
        message.edit(f'{message.from_user.first_name} {ln(15)} **{grate.roll(frm, to)}** [{frm}-{to}]')
    except:
        message.edit('attributes missing')

@client.on_message(filters.command('try', '!') & filters.me)
def trry(client, message: Message):
    try:
        right = message.text.split(' ', 1)[1]
        message.edit(f'{right.capitalize()}: **{ln(16)[grate.trry()]}**')
    except:
        message.edit('attributes missing')

@client.on_message(filters.command('add', '!') & filters.me)
def addtext(client, message: Message):
    namex = message.text.split() # namex[1]
    textx = message.reply_to_message.text
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
def deltext(client, message: Message):
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
    if chints == '1':
        sp = message.text.split(maxsplit=2)
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
            try:
                cur.execute("UPDATE settings SET val=? WHERE key=?", (sp[2], 'name_interval'))
                conn.commit()
                message.edit(ln(19)[0])
                time.sleep(2)
                message.delete()
            except:
                message.edit(ln(19)[1])
                time.sleep(2)
                message.delete()
    elif chints == '0':
        message.edit('BETA not enabled')
        time.sleep(2)
        message.delete()

@client.on_message(filters.command('chints', '!') & filters.me)
def chints_r(client, message:Message):
    if chints == '1':
        sp = message.text.split(maxsplit=2)
        if sp[1] == 'list':
            cur.execute("SELECT id, val FROM profile WHERE type=?", ('chints',))
            rows = cur.fetchall()
            all = ln(20)
            for row in rows:
                all = f'{all}\n{row[0]} - {row[1]}'
            message.edit(all)
        elif sp[1] == 'add':
            try:
                cur.execute('INSERT INTO profile (val, type) VALUES (?, ?)', (sp[2], 'chints'))
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
            try:
                cur.execute("UPDATE settings SET val=? WHERE key=?", (sp[2], 'chints_interval'))
                conn.commit()
                message.edit(ln(19)[0])
                time.sleep(2)
                message.delete()
            except:
                message.edit(ln(19)[1])
                time.sleep(2)
                message.delete()
    elif chints == '0':
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

event = Event()
@client.on_message(filters.command('init', '!!') & filters.me)
def inithere(client, message:Message):
    cur.execute('SELECT val FROM profile WHERE type=?', ('name',))
    names = cur.fetchall()
    cur.execute('SELECT val FROM profile WHERE type=?', ('chints',))
    chintss = cur.fetchall()
    cur.execute('SELECT val FROM settings WHERE key=?', ('name_interval',))
    nameint = cur.fetchone()[0]
    cur.execute('SELECT val FROM settings WHERE key=?', ('chints_interval',))
    chintsint = cur.fetchone()[0]
    if names == [] or chintss == []:
        message.edit(ln(24)[1])
        time.sleep(3)
        message.delete()
    else:
        try:
            message.edit(f'{ln(24)[0]}⏱ intervals: {nameint} / {chintsint}')
            time.sleep(3)
            message.delete()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(namechint, names, nameint, event)
                executor.submit(chintschint, chintss, nameint, event)
        except:
            message.edit(ln(24)[2])
            time.sleep(3)
            message.delete()

def namechint(names, intr, event):
    while True:
        randd = r.choice(names)[0]
        client.update_profile(first_name=randd)
        time.sleep(int(intr))
        if event.is_set():
            print('stopped')
            return

def chintschint(chintss, intr, event):
    time.sleep(2)
    while True:
        randd = r.choice(chintss)[0]
        client.update_profile(bio=randd)
        time.sleep(int(intr))
        if event.is_set():
            print('stopped')
            event.clear()
            return

@client.on_message(filters.command('stop', '!!') & filters.me)
def stopinit(client, message:Message):
    event.set()
    message.edit('+')
    time.sleep(2)
    message.delete()

@client.on_message(filters.command('heart', '!!') & filters.me)
def newhearts(client, message: Message):
    mode = message.text.split()[1]
    if mode == 'changesymbol':
        symb = message.text.split()[2]
        val = message.text.split()[3]
        cur.execute('''UPDATE variables SET val=? WHERE key=?''', (val, symb))

@client.on_message(filters.command('np', '!') & filters.me)
def np(client, message: Message):
    now = grate.nowplaying()
    if not now[0] == 'nothing':
        message.edit(f'{ln(26)[0]}**{now[0].split(".")[0].capitalize()}**\n{ln(26)[1]}{now[2]}\n{ln(26)[2]}{now[3]}')
    else:
        message.edit(ln(26)[3])

@client.on_message(filters.command('sb', '!') & filters.me)
def sb(client, message: Message):
    message.edit('Spamblock?')
    chatid = message.chat.id
    msg1 = message
    time.sleep(1)
    msg2 = client.send_message(chatid, 'Really?')
    time.sleep(1)
    msg1.edit_text('Ok')
    msg2.edit_text('...')
    time.sleep(1)
    msg2.delete()
    msg1.edit_text('Maybe')
    msg3 = client.send_message(chatid, 'NOT???')
    time.sleep(1)
    msg3.delete()
    msg1.delete()
    msg1 = client.send_message(chatid, 'HAHAHAHAHAHAHAHAH')
    time.sleep(0.3)
    msg2 = client.send_message(chatid, 'THERE IS NOT SPAMBLOCK')
    time.sleep(1)
    msg1.delete()
    msg2.delete()
    msg1 = client.send_message(chatid, 'huh.. okay...')
    time.sleep(1)
    msg1.edit_text('But can you see...')
    time.sleep(1)
    msg1.delete()
    msg1 = client.send_message(chatid, 'THIS???')
    msg2 = client.send_message(chatid, 'THIS???')
    msg3 = client.send_message(chatid, 'THIS???')
    msg4 = client.send_message(chatid, 'THIS???')
    msg5 = client.send_message(chatid, 'THIS???')
    msg6 = client.send_message(chatid, 'THIS???')
    msg7 = client.send_message(chatid, 'THIS???')
    msg8 = client.send_message(chatid, 'THIS???')
    time.sleep(1)
    msg1.delete()
    msg2.delete()
    msg3.delete()
    msg4.delete()
    msg5.delete()
    msg6.delete()
    msg7.delete()
    msg8.delete()
    msg1 = client.send_message(chatid, 'Okay')
    time.sleep(0.3)
    msg2 = client.send_message(chatid, 'Sorry')
    time.sleep(1)
    msg1.delete()
    msg2.delete()
    msg1 = client.send_message(chatid, 'Userbot: @TelehashDev')
    time.sleep(3)
    msg1.delete()

@client.on_message(filters.command('bot', '!') & filters.me)
def botstat(client, message: Message):
    message.edit(f'{ln(27)[0]}{str(datetime.now() - runTime).split(".")[0]} / {str(datetime.now() - startTime).split(".")[0]}')

@client.on_message(filters.me)
def edittags(client, message: Message):
    text = message.text
    try:
        if '{time}' in text:
            text = text.replace('{time}', str(datetime.now().time()).split('.')[0])
        if '{date}' in text:
            text = text.replace('{date}', str(datetime.now().date()))
        if '{nowartist}' in text:
            text = text.replace('{nowartist}', grate.nowplaying()[2])
        if '{nowname}' in text:
            text = text.replace('{nowname}', grate.nowplaying()[3])
        if '{phone}' in text:
            text = text.replace('{phone}', '+'+str(client.get_me().phone_number))
        if '{id}' in text:
            text = text.replace('{id}', str(client.get_me().id))
        if '{chatid}' in text:
            text = text.replace('{chatid}', str(message.chat.id))
        if '{ver}' in text:
            text = text.replace('{ver}', v)
        if '{userid}' in text:
            try:
                text = text.replace('{userid}', str(message.reply_to_message.from_user.id))
            except:
                text = text.replace('{userid}', '$noreply')
    except:
        pass
    if not text == message.text:
        message.edit(text)

clear()
if lng == '1':
    print(f'{text}\nv.{v}\nChat commands list\n\n!type [text] - type your text letter to letter\n!heart [1-2] - send animated heart\n!au - send author+user information, sub to our news channel\n!rib - send animated Georges ribbon (event on may, 9)\n!spoti - send the song you are listening to to the chat (Restrictions: Spotify, exe application)\n. - forward message\n!roll [from] [to] - send a random value between from and to \n!try [question] - get the answer to the question in the form of false/true\n!add [name] - save message text (need be reply to another message) in DB with name\n!del [name] <name or id> - delete variable from database\n!put [name] <name or id> - put text with its name (or id)\n!list - list of saved vars')
    print('----------')
    if chints == '1':
        print(ln(23)[1])
    print(ln(12))
elif lng == '2':
    print(f'{text}\nv.{v}\n\nСписок команд для чата\n\n!type [text] - написать Ваше сообщение побуквенно\n!heart [1-2] - отправить анимированное сердце\n!au - отправить информацию о разработчике и пользователе, подписаться на новостной канал\n!rib - отправить анимированную Георгиевскую ленту (событие на 9 мая)\n!spoti - отправить прослушиваемую песню в чат (Ограничения: Spotify, exe-приложение)\n. - переслать сообщение\n!roll [от] [до] - отправить случайное значение между от и до\n!try [вопрос] - получить ответ на вопрос в виде ложь/истина\n!add [имя] - сохранить текст сообщения (нужно отправлять ответом на сообщение) в базу данных под установленным именем\n!put [имя] <name или id> - вставить сохранённый текст под установленным именем (или id)\n!del [имя] <name или id> - удалить значение из базы данных\n!list - список сохранённых значений\n!np - показать, что вы слушаете')
    print('----------')
    if chints == '1':
        print(ln(23)[1])
    print(ln(12))

client.run()