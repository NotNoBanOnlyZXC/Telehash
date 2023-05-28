import win32gui
import random as r

def spotify():
    spw = 0
    while True:
        windowis = (win32gui.GetWindowText(win32gui.FindWindow('Chrome_WidgetWin_0', None)))
        if ' - ' in windowis:
            spotify = windowis.split(' - ')
            print('Artist: '+spotify[0])
            print('Song: '+spotify[1])
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