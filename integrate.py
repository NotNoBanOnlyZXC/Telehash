import win32gui, psutil, win32process
import random as r

def spotify():
    spw = 0
    while True:
        windowis = (win32gui.GetWindowText(win32gui.FindWindow('Chrome_WidgetWin_0', None)))
        if ' - ' in windowis:
            spotify = windowis.split(' - ')
            spw = [win32gui.FindWindow('Chrome_WidgetWin_0', None), spotify[0], spotify[1]]
            a = 0
            break
        else:
            spw = ['Spotify not found', 'ERR: 001', 'ERR: 001']
            if a == 0:
                print('Waiting for Spotify...')
                a = 1
    return(spw)

def roll(frm, to):
    return(r.randint(int(frm), int(to)))

def trry():
    return(r.randint(0, 1))

def fwws(sym):
    windows = []
    def callback(hwnd, lParam):
        if sym in win32gui.GetWindowText(hwnd) and not ' - AutoHotkey' in win32gui.GetWindowText(hwnd) and not 'Яндекс Музыка' in win32gui.GetWindowText(hwnd) and not ' - Visual Studio' in win32gui.GetWindowText(hwnd):
            windows.append(hwnd)
        return True
    
    win32gui.EnumWindows(callback, None)
    return windows

def nowplaying():
    windows = fwws(' - ')
    if windows == []:
        windows = fwws(' — ')
    for hwnd in windows:
        title = win32gui.GetWindowText(hwnd)
        process = psutil.Process(win32process.GetWindowThreadProcessId(hwnd)[1]).name()
        try:
            artist = title.split(' - ', 1)[0]
            name = title.split(' - ', 1)[1]
        except:
            artist = title.split(' — ', 1)[1].split(', ')[0]
            name = title.split(' — ', 1)[0]
    if windows == []:
        process = 'nothing'
        title = 'none - none'
        artist = 'none'
        name = 'none'
    return(process, title, artist, name)