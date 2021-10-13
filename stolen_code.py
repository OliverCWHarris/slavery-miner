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

def writecommands():
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

def closediscord():
    #mimnimises discord
    pyautogui.moveTo(320,1050)#goes to discord in the tray
    pyautogui.click()#minimised discord
    time.sleep(0.1)
    pyautogui.moveTo(1000,500)



start=1
repeated=0
while start==1:
    opendiscord()
    time.sleep(2)
    writecommands()
    time.sleep(2)
    closediscord()
    #time.sleep(420)
    #repeated=repeated+1
    #if repeated==10:
    #   start=0
    start=0