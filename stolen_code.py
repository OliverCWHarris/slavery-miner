import time
import random
import pyautogui



randomtime=random.randint(1,4)


def opendiscord():
    #opening discord and selecting chat
    time.sleep(2)
    pyautogui.moveTo(320,1050)#moves cursor to discord in the tray
    pyautogui.click()#opens discord
    time.sleep(0.1)
    pyautogui.moveTo(30,400)#moves cursor to server
    pyautogui.click()#enters server
    time.sleep(0.1)
    pyautogui.move(100,80)#goes to chat list
    time.sleep(0.1)
    pyautogui.scroll(-10000)#scrolls to bottom of chat list
    pyautogui.click()#enters chat
    time.sleep(0.1)

def allcommands():
    #typing commands
    pyautogui.write(';f')#fish command
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';h')#hunt command
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';s')#sell command
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';up b a')#upgrades bag as much as possible
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';up p a')#upgrade pickaxe as much as possible
    pyautogui.press('enter')
    time.sleep(randomtime)

def justsell():
    pyautogui.write(';f')#fish command
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';h')#hunt command
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';s')#sell command
    pyautogui.press('enter')

def crates():
    pyautogui.write(';f')#fish command
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';h')#hunt command
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';s')#sell command
    pyautogui.press('enter')
    pyautogui.write(';hourly')
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';daily')
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';weekly')
    pyautogui.press('enter')




def closediscord():
    #mimnimises discord
    pyautogui.moveTo(320,1050)#goes to discord in the tray
    pyautogui.click()#minimised discord
    time.sleep(0.1)
    pyautogui.moveTo(1000,500)



start=1
repeated=0
while start==1:
    menuchoice=int(input("1 for everything\n2 for sell\n3 for crates\n:"))
    if menuchoice==1:
        opendiscord()
        time.sleep(2)
        allcommands()
        time.sleep(2)
        closediscord()
    elif menuchoice==2:
        opendiscord()
        time.sleep(2)
        justsell()
        time.sleep(2)
        closediscord()
    elif menuchoice==3:
        opendiscord()
        time.sleep(2)
        crates()
        time.sleep(2)
        closediscord()
    
    
    #time.sleep(420)
    #repeated=repeated+1
    #if repeated==10:
    #   start=0