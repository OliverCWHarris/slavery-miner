import pynput
from pynput.mouse import Button, Controller
import time
import random
import pyautogui

mouse=Controller()

randomtime=random.randint(1,4)


def opendiscord():
    #opening discord and selecting chat
    mouse.position=(320,1050)#discord on the item tray
    mouse.click(Button.left, 1)#goes into discord
    time.sleep(0.1)
    mouse.position=(30,400)#goes to sesrver
    mouse.click(Button.left,1)#goes into server
    time.sleep(0.1)
    mouse.move(100,70)#moves mouse to chat list
    time.sleep(0.1)
    mouse.scroll(0,-10)#scrolls to bottom of chat list
    time.sleep(0.1)
    mouse.click(Button.left,1)#enters chat

def writecommands():
    #typing commands
    pyautogui.write(';f')
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';h')
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';s')
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';up b a')
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';up p a')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('nice')
    pyautogui.press('enter')
    time.sleep(randomtime)
    mouse.click(Button.left,1)

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
    time.sleep(420)
    repeated=repeated+1
    if repeated==10:
        start=0