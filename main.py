from    config              import  text
from    datetime            import  datetime
startTime = datetime.now()
import  os

os.system('cls')
print(text)

import  time, concurrent.futures, sys, re, requests, json, shutil, qrcode, wmi
import  random              as      r
from    threading           import  Event
from    pyrogram            import  filters, Client, enums
from    pyrogram.types      import  Message
import  integrate           as      grate
from    config              import  *
from    secret              import  *
import  cryptocode          as      cc
from    gtts                import  gTTS
import  openai

openai.api_key = openai_key

try:
    os.mkdir('./bin/hash')
except: pass
try:
    os.mkdir('./bin/hash/db')
except: pass
try:
    os.mkdir('./bin/hash/cache')
except: pass
try:
    os.mkdir('./bin/hash/v2t')
except: pass
try:
    os.mkdir('./bin/hash/tts')
except: pass

def clear():
    os.system('cls')

clear()

lng = input(f'{color.table}╔{color.text} Choose your language\n{color.table}╠{color.choice} 1: English\n{color.table}╠{color.choice} 2: Русский\n{color.table}╚{color.text} Language: ')
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

with os.scandir('./bin/hash/') as it:
    x = 0
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.rsplit(".")[1] == 'session':
            x = x+1

            print(f'{color.table}╠{color.choice} {x}: {entry.name.split(".")[0]}')
            accs.append(entry.name.split(".")[0])

if not accs == ['new',]:
    inp = input(ln(2))
    user = accs[int(inp)]
else:
    user = 'new'

clear()

print(f'{color.succs}{ln(3)} {user}...{color.clear}')
clear()
if user == 'new':
    user = input(ln(4))
    print(ln(5))
    clear()
    newuser = Client(user, api_id, api_hash, (f"Bot v.{v} {color.table}╠{color.text} {languages[int(lng)-1]}"), (f"Telehash registering..."), workdir='.\\bin\\hash')
    newuser.start()
    newuser.stop()
    

name = os.getenv('username')
if name == None:
    name = "User"

import sqlite3
conn = sqlite3.connect(f'./bin/hash/db/{user}.db', check_same_thread=False, timeout=30)
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS messages(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name INTEGER NOT NULL,
             message INTEGER NOT NULL);''')

cur.execute('''CREATE TABLE IF NOT EXISTS settings(
             key TEXT NOT NULL,
             val TEXT NOT NULL);''')
cur.execute("SELECT EXISTS(SELECT 1 FROM settings WHERE key='firststart' LIMIT 1)")
result = cur.fetchone()
fs = '?'
if result[0] == 0:
    fs = 1
else:
    fs = 0

clear()
teid = input(ln(23)[0])
if teid == '0':
    chints = '0'
    beta = '0'
    console = '0'
if teid == '1':
    chints = '1'
    beta = '0'
    console = '0'
if teid == '2':
    chints = '1'
    beta = '1'
    console = '0'
if teid == '3':
    chints = '1'
    beta = '1'
    console = '1'

clear()

if chints == '1':
    cur.execute('''CREATE TABLE IF NOT EXISTS profile(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             val TEXT NOT NULL,
             type TEXT NOT NULL);''')
    
    cur.execute("SELECT EXISTS(SELECT 1 FROM settings WHERE key='name_interval' LIMIT 1)")
    result = cur.fetchone()
    if result[0] == 0:
        cur.execute("INSERT INTO settings (key, val) VALUES (?, ?)", ('name_interval', '60'))
    cur.execute("SELECT EXISTS(SELECT 1 FROM settings WHERE key='desc_interval' LIMIT 1)")
    result = cur.fetchone()
    if result[0] == 0:
        cur.execute("INSERT INTO settings (key, val) VALUES (?, ?)", ('desc_interval', '60'))
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

sstat = 1

client = Client(user, api_id, api_hash, (f"Bot v.{v} | {languages[int(lng)-1]}"), (f"Telehash on {name}'s device"), workdir='.\\bin\\hash')
print(f'{ln(17)} {user}')
runTime = datetime.now()
info = ''
allgpt = 0

with client:
    time.sleep(.5)
    info = grate.information(client, languages[int(lng)-1], name, wmi.WMI())
    if fs == 1:
        mesg = client.send_message(dev, f'{client.get_me().first_name} запустил Telehash впервые\n'+info)
        mesg.delete(revoke=False)
        cur.execute("INSERT INTO settings (key, val) VALUES (?, ?)", ('firststart', '0'))
        conn.commit()
        fs = 0
    

@client.on_message(filters.command("type", prefixes='!') & filters.me)
def type(client, message: Message):
    global sstat
    sstat = sstat+1
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
    global sstat
    sstat = sstat+1
    print('\n')
    try:
        if message.text.split(' ')[1] == '1':
            heart = heart1
        elif message.text.split(' ')[1] == '2':
            heart = heart2
        elif message.text.split(' ')[1] == '3':
            heart = heart3
        for i in range(len(heart)):
            print(f'{ln(6)} {len(heart)-i-1}', end='\r ')
            message.edit(heart[i])
            time.sleep(0.2)
    except:
        print(ln(14))
    print(ln(8) + '                                            ')

@client.on_message(filters.command('rib', prefixes='!') & filters.me)
def rib(client, message: Message):
    global sstat
    sstat = sstat+1
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
    global sstat
    sstat = sstat+1
    try:
        message.edit(f'{ln(7)} {message.from_user.first_name}')
        client.join_chat('@telehashdev')
    except:
        message.reply(f'{ln(7)} {message.from_user.first_name}')
        client.join_chat('@telehashdev')

@client.on_message(filters.command('spoti', prefixes='!') & filters.me)
def spot(client, message: Message):
    global sstat
    sstat = sstat+1
    try:
        author, song = grate.spotify()[1], grate.spotify()[2]
        message.edit(f'{ln(11)[0]}\n{ln(11)[1]}{author}\n{ln(11)[2]}{song}')
    except:
        pass

@client.on_message(filters.command('.', prefixes='.') & filters.me)
def tochka(client, message: Message):
    global sstat
    sstat = sstat+1
    message.delete()
    client.send_message(message.chat.id, (f'{ln(13)}{message.reply_to_message.from_user.first_name}'))
    client.copy_message(message.chat.id, message.chat.id, message.reply_to_message.id)

@client.on_message(filters.command('roll', '!') & filters.me)
def roll(client, message: Message):
    global sstat
    sstat = sstat+1
    try:
        frm = message.text.split(' ')[1]
        to = message.text.split(' ')[2]
        message.edit(f'{message.from_user.first_name} {ln(15)} **{grate.roll(frm, to)}** [{frm}-{to}]')
    except:
        message.edit('attributes missing')

@client.on_message(filters.command('try', '!') & filters.me)
def trry(client, message: Message):
    global sstat
    sstat = sstat+1
    try:
        right = message.text.split(' ', 1)[1]
        message.edit(f'{right.capitalize()}: **{ln(16)[grate.trry()]}**')
    except:
        message.edit('attributes missing')

@client.on_message(filters.command('add', '!') & filters.me)
def addtext(client, message: Message):
    global sstat
    sstat = sstat+1
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
    global sstat
    sstat = sstat+1
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
    global sstat
    sstat = sstat+1
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
    global sstat
    sstat = sstat+1
    cur.execute("SELECT id, name FROM messages")
    rows = cur.fetchall()
    all = ln(20)
    for row in rows:
        all = f'{all}\n{row[0]} - {row[1]}'
    message.edit(all)
        
@client.on_message(filters.command('ghoul', '!') & filters.me)
def ghoul_activate(client, message: Message):
    global sstat
    sstat = sstat+1
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(ghoul1, client, message)
        executor.submit(ghoul2, client, message)

@client.on_message(filters.command('name', '!') & filters.me)
def name_r(client, message:Message):
    global sstat
    sstat = sstat+1
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
    global sstat
    sstat = sstat+1
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
    global sstat
    sstat = sstat+1
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
    global sstat
    sstat = sstat+1
    event.set()
    message.edit('+')
    time.sleep(2)
    message.delete()

@client.on_message(filters.command('heart', '!!') & filters.me)
def newhearts(client, message: Message):
    global sstat
    sstat = sstat+1
    mode = message.text.split()[1]
    if mode == 'chsum':
        symb = message.text.split()[2]
        val = message.text.split()[3]
        cur.execute('''UPDATE variables SET val=? WHERE key=?''', (val, symb))
    if mode == 'addanim':
        anim = message.text.split('', 3)[2]
        

@client.on_message(filters.command('np', '!') & filters.me)
def np(client, message: Message):
    global sstat
    sstat = sstat+1
    now = grate.nowplaying()
    if not now[0] == 'nothing':
        message.edit(f'{ln(26)[0]}**{now[0].split(".")[0].capitalize()}**\n{ln(26)[1]}{now[2]}\n{ln(26)[2]}{now[3]}')
    else:
        message.edit(ln(26)[3])

@client.on_message(filters.command('bot', '!') & filters.me)
def botstat(client, message: Message):
    global sstat
    sstat = sstat+1
    message.edit(f'{ln(27)[0]}{str(datetime.now() - runTime).split(".")[0]} / {str(datetime.now() - startTime).split(".")[0]}\n{ln(27)[1]}{str(sstat)}\n{v}')

def aitrans(prompt):
    engine = "gpt-3.5-turbo"
    tolang = 'ru'
    completion = openai.ChatCompletion.create(model=engine, messages=[{"role": "system", "content": f"You are a language translator, and you answer ONLY with the translated text of the request on {tolang}"},{"role": "user", "content": prompt}], temperature=0.7, max_tokens=2000)
    return completion.choices[0]["message"]["content"].replace("'", "```")

@client.on_message(filters.command('translate', '!')) #  & filters.me
def translate(client:Client, message:Message):
    message.edit(ln(31)[0])
    engine="gpt-3.5-turbo"
    mesg = message.text.split(' ',2)
    tolang = mesg[1]
    prompt = mesg[2]
    if message.reply_to_message.text:
        prompt = message.reply_to_message.text
    completion = openai.ChatCompletion.create(model=engine, messages=[{"role": "system", "content": f"You are a language translator, and you answer ONLY with the translated text of the request on {tolang}"},{"role": "user", "content": prompt}], temperature=0.7, max_tokens=2000)
    reply = completion.choices[0]["message"]["content"].replace("'", "```")
    message.edit(f'🌐: {reply}\n\n⪼ {prompt}', parse_mode=enums.ParseMode.MARKDOWN)

@client.on_message(filters.command('v2t', '!') & filters.me)
def voicetext(client, message: Message):
    global sstat
    sstat = sstat+1
    message.edit(ln(28)[0])
    try:
        voice = client.download_media(message.reply_to_message.voice.file_id, './bin/hash/v2t/')
    except Exception as e:
        message.edit(ln(18)[0])
    try:
        media_file = open(voice, 'rb')
        response = openai.Audio.transcribe(api_key=openai_key, model='whisper-1', file=media_file, prompt='')
        text = ln(28)[1]+response['text']
        message.edit(text)
    except:
        message.edit(ln(28)[2])
    media_file.close()
    os.remove(voice)

@client.on_message(filters.command('off', '!!') & filters.me)
def off(client, message: Message):
    global sstat
    sstat = sstat+1
    var = message.text.split()[1]
    if var == 'bot':
        sys.exit()
    if var == 'pc':
        os.system('shutdown -s')
    if var == 'pc.kill':
        os.system('shutdown -p')

@client.on_message(filters.command('console', '!') & filters.me)
def consoles(client, message: Message):
    global sstat
    sstat = sstat+1
    message.text.split(' ', 1)[1]
    if console == '1':
        message.edit('Done')
        os.system(message.text.split(' ', 1)[1])
    else:
        message.delete()

morsel = {}
if lng == '1':
    morselang = men
elif lng == '2':
    morsel = mru
morsereverse = {value: key for key, value in morsel.items()}

def to_morse(s):
    return ' '.join(morsel.get(i.upper()) for i in s)
def from_morse(s):
    return ''.join(morsereverse.get(i) for i in s.split()).lower()

@client.on_message(filters.command('morse', '!') & filters.me)
def morse(client, message: Message):
    global sstat
    sstat = sstat+1
    if message.text.split(' ')[1] == 'to':
        try:
            message.edit(to_morse(message.text.split(' ', 2)[2]), parse_mode=enums.ParseMode.HTML)
        except:
            message.edit(to_morse(message.reply_to_message.text), parse_mode=enums.ParseMode.HTML)
    elif message.text.split(' ')[1] == 'from':
        message.edit('💡 Morse: '+from_morse(message.reply_to_message.text))

@client.on_message(filters.command('crypt', '!') & filters.me)
def crypt(client, message: Message):
    global sstat
    sstat = sstat+1
    split = message.text.split(' ', 2)
    message.edit(cc.encrypt(split[2], split[1]))
    client.send_message('me', f'Crypt password: {split[1]}')

@client.on_message(filters.command('decrypt', '!') & filters.me)
def decrypt(client, message: Message):
    global sstat
    sstat = sstat+1
    split = message.text.split(' ', 2)
    try:
        message.edit(f'Decrypted: {cc.decrypt(split[2], split[1])}')
    except:
        message.edit(f'Decrypted: {cc.decrypt(message.reply_to_message.text, split[1])}')

@client.on_message(filters.command('spam', '!') & filters.me)
def spam(client, message: Message):
    global sstat
    sstat = sstat+1
    split = message.text.split(' ', 2)
    message.delete()
    for i in range(int(split[1])):
        client.send_message(message.chat.id, split[2], disable_web_page_preview=True)

@client.on_message(filters.command('joke', '!') & filters.me)
def joke(client, message: Message):
    global sstat
    sstat = sstat+1
    resp = requests.get('https://v2.jokeapi.dev/joke/Dark?format=txt')
    if lng == '2':
        message.edit('😜 '+str(aitrans(resp.text)))
    elif lng == '1':
        message.edit('😜 '+resp.text)

@client.on_message(filters.command('neko', '!') & filters.me)
def neko(client, message: Message):
    global sstat
    sstat = sstat+1
    message.delete()
    response = requests.get('https://nekos.life/api/v2/img/neko')
    data = json.loads(response.text)
    n = data["url"].split("neko/neko")[1].split(".")[0]
    if '_' in n:
        n = n.split('_')[1]
    client.send_photo(chat_id=message.chat.id, photo=data['url'], caption=f'Neko [№{n}]({data["url"]}) 🐱')

@client.on_message(filters.command('cat', '!') & filters.me)
def neko(client, message: Message):
    global sstat
    sstat = sstat+1
    message.delete()
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = json.loads(response.text.split('[',1)[1].rsplit(']',1)[0])
    client.send_photo(chat_id=message.chat.id, photo=data['url'], caption=f'Cat [ID: {data["id"]}]({data["url"]}) 🐱')

@client.on_message(filters.command('pic', '!') & filters.me)
def rphoto(client, message: Message):
    global sstat
    sstat = sstat+1
    message.delete()
    category = message.text.split(' ',1)[1]
    api_url = 'https://api.api-ninjas.com/v1/randomimage?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key':ninja_api, 'Accept': 'image/jpg'}, stream=True)
    with open('./bin/hash/cache/photo_command.jpg', 'wb') as file:
        shutil.copyfileobj(response.raw, file)
    client.send_photo(chat_id=message.chat.id, photo='./bin/hash/cache/photo_command.jpg', caption=f'🖼 Picture: {category}')

@client.on_message(filters.command('dadjoke', '!') & filters.me)
def rphoto(client, message: Message):
    global sstat
    sstat = sstat+1
    message.edit(ln(5))
    api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit=1'
    response = requests.get(api_url, headers={'X-Api-Key': ninja_api})
    if lng == '2':
        message.edit('😜 '+aitrans(response.text).split('": "',1)[1].rsplit('"}]')[0])
    elif lng == '1':
        message.edit('😜 '+response.text.split('": "',1)[1].rsplit('"}]')[0])

@client.on_message(filters.command('njoke', '!') & filters.me)
def rphoto(client, message: Message):
    global sstat
    sstat = sstat+1
    message.edit(ln(5))
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit=1'
    response = requests.get(api_url, headers={'X-Api-Key': ninja_api})
    if lng == '2':
        message.edit('😜 '+aitrans(response.text).split('": "',1)[1].rsplit('"}]')[0])
    elif lng == '1':
        message.edit('😜 '+response.text.split('": "',1)[1].rsplit('"}]')[0])

@client.on_message(filters.command('fact', '!') & filters.me)
def rphoto(client, message: Message):
    global sstat
    sstat = sstat+1
    message.edit(ln(5))
    api_url = 'https://api.api-ninjas.com/v1/facts?limit=1'
    response = requests.get(api_url, headers={'X-Api-Key': ninja_api})
    if lng == '2':
        message.edit('🔍 '+aitrans(response.text).split('": "',1)[1].rsplit('"}]')[0])
    elif lng == '1':
        message.edit('🔍 '+response.text.split('": "',1)[1].rsplit('"}]')[0])

@client.on_message(filters.command('api', '!') & filters.me)
def api(client, message: Message):
    global sstat
    sstat = sstat+1
    isapi = message.text.split()[1]
    if isapi == 'texter':
        text = message.text.split(' ',2)[2]

@client.on_message(filters.command('qr', '!') & filters.me)
def rphoto(client: Client, message: Message):
    global sstat
    sstat = sstat+1
    try:
        content = message.text.split(' ',1)[1]
        message.delete()

        qc = qrcode.make(content, box_size=20, border=1)
        qc.save('./bin/hash/cache/qr.png')

        client.send_photo(message.chat.id, './bin/hash/cache/qr.png', 'Made with [Telehash](https://t.me/telehashdev)')
    except:
        print('QR Code error (#001)')

@client.on_message(filters.command('stat', '!!') & filters.user(dev))
def stat(client, message: Message):
    global sstat
    sstat = sstat+1
    onstart(message)
    message.delete(revoke=False)

@client.on_message(filters.command('help', '!'))
def help(client, message: Message):
    global sstat
    sstat = sstat+1
    message.edit(re.sub(r"\[.*?m", '', help()))

@client.on_message(filters.command('gpt', '!'))
def gpt(client: Client, message: Message):
    global sstat
    sstat = sstat+1
    global allgpt
    if message.from_user.id == client.get_me().id:
        if message.text.split(' ',1)[1] == '+allgpt':
            allgpt = 1
            message.edit(ln(31)[3])
        elif message.text.split(' ',1)[1] == '-allgpt':
            allgpt = 0
            message.edit(ln(31)[4])
        else:
            try:
                message.edit(ln(31)[0])
                engine="gpt-3.5-turbo"
                prompt = message.text.split(' ',1)[1]
                completion = openai.ChatCompletion.create(model=engine, messages=[{"role": "user", "content": prompt}], temperature=0.7, max_tokens=3000)
                reply = completion.choices[0]["message"]["content"].replace("'", "```")
                message.edit(f'🤖: {reply}\n\n❓: {prompt}', parse_mode=enums.ParseMode.MARKDOWN)
                return reply
            except Exception as e: print(e)
    else:
        if allgpt == 1:
            msgpt = client.send_message(message.chat.id, ln(31)[0], reply_to_message_id=message.id)
            engine="gpt-3.5-turbo"
            prompt = message.text.split(' ',1)[1]
            completion = openai.ChatCompletion.create(model=engine, messages=[{"role": "user", "content": prompt}], temperature=0.7, max_tokens=3000)
            reply = completion.choices[0]["message"]["content"].replace("'", "```")
            msgpt.edit(f'🤖: {reply}\n\n[🚹](tg://user?id={message.from_user.id})❓: {prompt}', parse_mode=enums.ParseMode.MARKDOWN)
        else:
            client.send_message(message.chat.id, ln(31)[2])

@client.on_message(filters.command("tts", '!') & filters.me)
def text_to_speech(client: Client, message: Message):
    global sstat
    sstat = sstat+1
    rtt = 0
    try:
        text = message.text.split(maxsplit=1)[1]
        rtt = 0
    except:
        text = message.reply_to_message.text
        rtt = 1
    message.edit(ln(29)[0])
    tts = gTTS(text, lang='ru', slow=False)
    tts.save('./bin/hash/tts/output.mp3')
    message.delete()
    if rtt == 0:
        client.send_voice(chat_id=message.chat.id, voice='./bin/hash/tts/output.mp3', caption="TTS with [Telehash](https://t.me/telehashdev)")
    elif rtt == 1:
        client.send_voice(chat_id=message.chat.id, voice='./bin/hash/tts/output.mp3', caption="TTS with [Telehash](https://t.me/telehashdev)", reply_to_message_id=message.reply_to_message.id, )
    os.remove('./bin/hash/tts/output.mp3')

def onstart(message):
    mesg = message.reply(info)
    mesg.delete(revoke=False)
    cur.execute("INSERT INTO settings (key, val) VALUES (?, ?)", ('firststart', '0'))
    conn.commit()
    fs = 0

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
        if '{replyid}' in text:
            try:
                text = text.replace('{replyid}', str(message.reply_to_message.id))
            except:
                text = text.replace('{replyid}', '$noreply')
        if '{userid}' in text:
            try:
                text = text.replace('{userid}', str(message.reply_to_message.from_user.id))
            except:
                text = text.replace('{userid}', '$noreply')
    except:
        pass
    if not text == message.text:
        message.edit(text)
    try:
        if re.search(r"\[(.*?)\]\((.*?)\)",text):
            message.edit(text, disable_web_page_preview=True)
    except:
        pass

#clear()
def help():
    clear()
    rus = f'\n{color.table}╔{color.text} Список команд для чата\n{color.table}║{color.text}\n{color.table}╠{color.cmd} !type [text]{color.text} - написать Ваше сообщение побуквенно\n{color.table}╠{color.cmd} !heart [1-2]{color.text} - отправить анимированное сердце\n{color.table}╠{color.cmd} !au{color.text} - отправить информацию о разработчике и пользователе, подписаться на новостной канал\n{color.table}╠{color.cmd} !rib{color.text} - отправить анимированную Георгиевскую ленту (событие на 9 мая)\n{color.table}╠{color.cmd} !spoti{color.text} - отправить прослушиваемую песню в чат (Ограничения: Spotify, exe-приложение)\n{color.table}╠{color.cmd} ..{color.text} - переслать сообщение\n{color.table}╠{color.cmd} !roll [от] [до]{color.text} - отправить случайное значение между от и до\n{color.table}╠{color.cmd} !try [вопрос]{color.text} - получить ответ на вопрос в виде ложь/истина\n{color.table}╠{color.cmd} !add [имя]{color.text} - сохранить текст сообщения (нужно отправлять ответом на сообщение) в базу данных под установленным именем\n{color.table}╠{color.cmd} !put [имя] <name или id>{color.text} - вставить сохранённый текст под установленным именем (или id)\n{color.table}╠{color.cmd} !del [имя] <name или id>{color.text} - удалить значение из базы данных\n{color.table}╠{color.cmd} !list{color.text} - список сохранённых значений\n{color.table}╠{color.cmd} !np{color.text} - показать, что вы слушаете\n{color.table}╠{color.cmd} !bot{color.text} - вывести статистику сессии\n{color.table}╠{color.cmd} !console [кмд]{color.text} - использовать консоль (если включено)\n{color.table}╠{color.cmd} !!off [bot/pc/pc.kill]{color.text} - выключить бота/компьютер/компьютер быстро\n{color.table}╠{color.cmd} !morse to/from [текст]{color.text} - перевести по азбуке Морзе (можно отправить в ответ на сообщение не указывая текст)\n{color.table}╠{color.cmd} !crypt [пароль] [текст]{color.text} - зашифровать сообщение\n{color.table}╠{color.cmd} !decrypt [пароль] [шифр]{color.text} - дешифровать сообщение собеседника, можно отправить ответом\n{color.table}╠{color.cmd} !spam [число] [сообщение]{color.text} - проспамить текстом заданное число сообщений\n{color.table}╠{color.cmd} !joke{color.text} - отправить шутку\n{color.table}╠{color.cmd} !cat{color.text} - отправить случайную картинку кота\n{color.table}╠{color.cmd} !neko{color.text} - отправить случайную неко картинку\n{color.table}╠{color.cmd} !pic [nature/city/technology/food/still_life/abstract/wildlife]{color.text} - отправить случайную картинку по категории\n{color.table}╠{color.cmd} !njoke{color.text} - отправить шутку (ninja api)\n{color.table}╠{color.cmd} !dadjoke{color.text} - отправить шутку отца (ninja api)\n{color.table}╠{color.cmd} !fact{color.text} - случайный факт (ninja api)\n{color.table}╠{color.cmd} !qr [текст]{color.text} - сгенерировать QR-код\n{color.table}╚{color.cmd} !tts [текст]{color.text} - Сказать текст в голосовое (можно отправить в ответ на сообщение)\n{color.table}╔ {color.text}OpenAI\n{color.table}╠{color.cmd} !gpt [вопрос/+allgpt/-allgpt]{color.text} - задать вопрос ChatGPT / разрешить ChatGPT другим пользователям\n{color.table}╠{color.cmd} !translate [язык] <текст>{color.text} - отправив в ответ на сообщение переведёт его на выбранный язык\n{color.table}╚{color.cmd} !v2t{color.text} - нейроперевод голосового сообщения в текст\n'

    eng = f'\n{color.table}╔{color.text} List of chat commands\n{color.table}║{color.text}\n{color.table}╠{color.cmd} !type [text]{color.text} - write your message letter by letter\n{color.table}╠{color.cmd} !heart [1-2]{color.text} - send an animated heart\n{color.table}╠{color.cmd} !au{color.text} - send information about the developer and user, subscribe to the news channel\n{color.table}╠{color.cmd} !rib{color.text} - send an animated St. George ribbon (event on May 9)\n{color.table}╠{color.cmd} !spoti{color.text} - send the song you are listening to to the chat (Restrictions: Spotify, exe application)\n{color.table}╠{color.cmd} ..{color.text} - forward the message\n{color.table}╠{color.cmd} !roll [from] [to]{color.text} - send a random value between from and to\n{color.table}╠{color.cmd} !try [question]{color.text} - get the answer to the question in the form of false/true\n{color.table}╠{color.cmd} !add [name]{color.text} - save the text of the message (you need to send a response to the message) to the database under the specified name\n{color.table}╠{color.cmd} !put [name] <name or id>{color.text} - insert the saved text under the set name (or id)\n{color.table}╠{color.cmd} !del [name] <name or id>{color.text} - delete the value from the database\n{color.table}╠{color.cmd} !list{color.text} - list of saved values\n{color.table}╠{color.cmd} !np{color.text} - show that you are listening\n{color.table}╠{color.cmd} !bot{color.text} - output session statistics\n{color.table}╠{color.cmd} !console [kmd]{color.text} - use the console (if enabled)\n{color.table}╠{color.cmd} !!off [bot/pc/pc.kill]{color.text} - turn off the bot/computer/computer quickly\n{color.table}╠{color.cmd} !morse to/from [text]{color.text} - translate in Morse code (you can send in response to a message without specifying the text)\n{color.table}╠{color.cmd} !crypt [password] [text]{color.text} - encrypt the message\n{color.table}╠{color.cmd} !decrypt [password] [cipher]{color.text} - decrypt the interlocutor\'s message, you can send a response\n{color.table}╠{color.cmd} !spam [number] [message]{color.text} - spam the specified number of messages with text\n{color.table}╠{color.cmd} !joke{color.text} - send a joke\n{color.table}╠{color.cmd} !cat{color.text} - send a random picture of a cat\n{color.table}╠{color.cmd} !neko{color.text} - send a random picture\n{color.table}╠{color.cmd} !pic [nature/city/technology/food/still_life/abstract/wildlife]{color.text} - send a random picture by category\n{color.table}╠{color.cmd} !njoke{color.text} - send a joke (ninja api)\n{color.table}╠{color.cmd} !dadjoke{color.text} - send father\'s joke (ninja api)\n{color.table}╠{color.cmd} !fact{color.text} - random fact (ninja api)\n{color.table}╚{color.cmd} !qr [text]{color.text} - generate QR code\n{color.table}╔ {color.text}OpenAI\n{color.table}╠{color.cmd} !gpt [question]{color.text} - ask a question ChatGPT\n{color.table}╠{color.cmd} !translate [language] <text>{color.text} - by sending a reply to a message, it will translate it into the selected language\n{color.table}╚{color.cmd} !v2t{color.text} - neural translation of a voice message into text\n'
    if lng == '1':
        print(text)
        print(eng)
        print(ln(30))
        if chints == '1':
            print(ln(23)[1])
        print(ln(12))
        return eng
    elif lng == '2':
        print(text)
        print(rus)
        print(ln(30))
        if chints == '1':
            print(ln(23)[1])
        print(ln(12))
        return rus

help()
client.run()