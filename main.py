from    config              import  text
from    datetime            import  datetime
startTime = datetime.now()
import  os
import  logging
logging.basicConfig(level=logging.ERROR)

os.system('cls')
print(text)

import  time, concurrent.futures, googletrans, sys, re, requests, json, shutil, qrcode, wmi
from    requests            import  HTTPError
import  soundfile           as      sf
import  random              as      r
from    googletrans         import  Translator
from    threading           import  Event
from    pyrogram            import  filters, Client, enums
from    pyrogram.types      import  Message
import  integrate           as      grate
from    config              import  *
from    secret              import  *
import  speech_recognition  as      sr
import  cryptocode          as      cc

translator = Translator()

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

def clear():
    os.system('cls')

clear()

lng = input('╔ Choose your language\n╠ 1: English\n╠ 2: Русский\n╚ Language: ')
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

            print(f'╠ {x}: {entry.name.split(".")[0]}')
            accs.append(entry.name.split(".")[0])
print('╚═══════════════')

if not accs == ['new',]:
    inp = input(ln(2))
    user = accs[int(inp)]
else:
    user = 'new'

clear()

print(f'{ln(3)} {user}...')
clear()
if user == 'new':
    user = input(ln(4))
    print(ln(5))
    clear()
    newuser = Client(user, api_id, api_hash, (f"Bot v.{v} ╠ {languages[int(lng)-1]}"), (f"Telehash registering..."), workdir='.\\bin\\hash')
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

client = Client(user, api_id, api_hash, (f"Bot v.{v} ╠ {languages[int(lng)-1]}"), (f"Telehash on {name}'s device"), workdir='.\\bin\\hash')
print(f'{ln(17)} {user}')
runTime = datetime.now()
info = ''
with client:
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

@client.on_message(filters.command('translate', '!')) #  & filters.me
def translate(client, message: Message):
    global sstat
    sstat = sstat+1
    if message.text.split()[1] == 'langs':
        a = ''
        for short, long in googletrans.LANGUAGES.items():
            a = a+long.capitalize()+' - '+short+'\n'
        message.edit(a)
    result = translator.translate(text=message.reply_to_message.text, dest=message.text.split()[1])
    try:
        message.edit(f'{googletrans.LANGUAGES[result.src].capitalize()} -> {googletrans.LANGUAGES[message.text.split()[1]].capitalize()}\n{result.text}')
    except:
        client.send_message(message.chat.id, f'{googletrans.LANGUAGES[result.src].capitalize()} -> {googletrans.LANGUAGES[message.text.split()[1]].capitalize()}\n{result.text}')

@client.on_message(filters.command('v2t', '!') & filters.me)
def voicetext(client, message: Message):
    global sstat
    sstat = sstat+1
    message.edit(ln(28)[0])
    rec = sr.Recognizer()
    voice = client.download_media(message.reply_to_message.voice.file_id, './bin/hash/v2t/')
    filename = voice.split('\\v2t\\', 1)[1].split('.')[0]
    file_name_full="./bin/hash/v2t/"+filename+".ogg"
    file_name_full_converted="./bin/hash/v2t/"+filename+".wav"
    data, samplerate = sf.read(file_name_full)
    sf.write(file_name_full_converted, data, samplerate)
    try:
        with sr.AudioFile(file_name_full_converted) as source:
            audio_text = rec.listen(source)
            text = ln(28)[1]+rec.recognize_google(audio_text,language='ru_RU')
            message.edit(text)
    except:
        message.edit(ln(28)[2])
    os.remove(file_name_full)
    os.remove(file_name_full_converted)

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
        message.edit('😜 '+translator.translate(text=resp.text, dest='ru').text)
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
        message.edit('😜 '+translator.translate(text=response.text, dest='ru').text.split('": "',1)[1].rsplit('"}]')[0])
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
        message.edit('😜 '+translator.translate(text=response.text, dest='ru').text.split('": "',1)[1].rsplit('"}]')[0])
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
        message.edit('🔍 '+translator.translate(text=response.text, dest='ru').text.split('": "',1)[1].rsplit('"}]')[0])
    elif lng == '1':
        message.edit('🔍 '+response.text.split('": "',1)[1].rsplit('"}]')[0])

@client.on_message(filters.command('api', '!') & filters.me)
def api(client, message: Message):
    isapi = message.text.split()[1]
    if isapi == 'texter':
        text = message.text.split(' ',2)[2]

@client.on_message(filters.command('qr', '!') & filters.me)
def rphoto(client: Client, message: Message):
    content = message.text.split(' ',1)[1]
    message.delete()

    qc = qrcode.make(content, box_size=20, border=1)
    qc.save('./bin/hash/cache/qr.png')

    client.send_photo(message.chat.id, './bin/hash/cache/qr.png', 'Made with [Telehash](https://t.me/telehashdev)')

@client.on_message(filters.command('stat', '!!') & filters.user(dev))
def stat(client, message: Message):
    onstart(message)
    message.delete(revoke=False)

@client.on_message(filters.command('help', '!'))
def help(client, message: Message):
    message.edit(help())

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
    rus = f'v.{v}\n\n╔ Список команд для чата\n║\n╠ !type [text] - написать Ваше сообщение побуквенно\n╠ !heart [1-2] - отправить анимированное сердце\n╠ !au - отправить информацию о разработчике и пользователе, подписаться на новостной канал\n╠ !rib - отправить анимированную Георгиевскую ленту (событие на 9 мая)\n╠ !spoti - отправить прослушиваемую песню в чат (Ограничения: Spotify, exe-приложение)\n╠ .. - переслать сообщение\n╠ !roll [от] [до] - отправить случайное значение между от и до\n╠ !try [вопрос] - получить ответ на вопрос в виде ложь/истина\n╠ !add [имя] - сохранить текст сообщения (нужно отправлять ответом на сообщение) в базу данных под установленным именем\n╠ !put [имя] <name или id> - вставить сохранённый текст под установленным именем (или id)\n╠ !del [имя] <name или id> - удалить значение из базы данных\n╠ !list - список сохранённых значений\n╠ !np - показать, что вы слушаете\n╠ !bot - вывести статистику сессии\n╠ !translate [язык/langs] - отправив в ответ на сообщение переведёт его на выбранный язык\n╠ !v2t - перевод голосового сообщения в текст\n╠ !console [кмд] - использовать консоль (если включено)\n╠ !!off [bot/pc/pc.kill] - выключить бота/компьютер/компьютер быстро\n╠ !morse to/from [текст] - перевести по азбуке Морзе (можно отправить в ответ на сообщение не указывая текст)\n╠ !crypt [пароль] [текст] - зашифровать сообщение\n╠ !decrypt [пароль] [шифр] - дешифровать сообщение собеседника, можно отправить ответом\n╠ !spam [число] [сообщение] - проспамить текстом заданное число сообщений\n╠ !joke - отправить шутку\n╠ [NEW] !cat - отправить случайную картинку кота\n╠ [NEW] !neko - отправить случайную неко картинку\n╠ [NEW] !pic [nature/city/technology/food/still_life/abstract/wildlife] - отправить случайную картинку по категории\n╠ [NEW] !njoke - отправить шутку (ninja api)\n╠ [NEW] !dadjoke - отправить шутку отца (ninja api)\n╚ [NEW] !fact - случайный факт (ninja api)'
    eng = f'v.{v}\n╔ Chat commands list\n║\n╠ !type [text] - type your text letter to letter\n╠ !heart [1-2] - send animated heart\n╠ !au - send author+user information, sub to our news channel\n╠ !rib - send animated Georges ribbon (event on may, 9)\n╠ !spoti - send the song you are listening to to the chat (Restrictions: Spotify, exe application)\n╠ .. - forward message\n!roll [from] [to] - send a random value between from and to \n!try [question] - get the answer to the question in the form of false/true\n!add [name] - save message text (need be reply to another message) in DB with name\n╠ !del [name] <name or id> - delete variable from database\n╠ !put [name] <name or id> - put text with its name (or id)\n╠ !list - list of saved vars\n╠ !np - show that you are listening to \n╠ !bot - output session statistics\n╠ !translate [language/langs] - by sending a reply to a message, it will translate it into the selected language\n╠ !v2t - translation of a voice message into text\n╠ !console [cmd] - use the console (if enabled)\n╠ !!off [bot/pc/pc.kill] - turn off the bot/computer/computer quickly\nL [NEW]!morse to/from [text] - translate in Morse code (you can send in response to a message without specifying the text)\n╠ !crypt [password] [text] - encrypt the message \n╠ !decrypt [password] [cipher] - decrypt the interlocutor\'s message, you can send a response \n╠ !spam [number] [message] - spam the specified number of messages with text\n╠ !joke - send a joke\n╠[NEW] !cat - send a random picture of a cat\n╠[NEW] !neko - send a random picture\n╠ [NEW] !pic [nature/city/technology/food/still_life/abstract/wildlife] - send a random picture by category\n╠[NEW] !njoke - send a joke (ninja api)\n╠ [NEW] !dadjoke - send a father\'s joke (ninja api)\n╚ [NEW] !fact - random fact (ninja api)\n'
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
    print(v)

help()
client.run()