import numpy as np
import pyautogui
from time import sleep
import cv2
import pytesseract
import threading

#Configurações de cura do personagem
config = {
    'healMode':True,
    'manaMode':False,
    'foodMode':True,
    'unlogoutMode':True,
    'attackMode':True,
    'timeHeal': 1.2,
    'timeHealDanger': 1,
    'timeHealMana': 2.0,
    'percentHeal': 97,
    'percentHealDanger': 70,
    'percentHealMana': 40
}

#Configuração do Tesseract
path = "C:/Users/junior.silva/AppData/Local/Tesseract-OCR/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path

#Faz a leitura dos dados
def convertToInt(currentScreen):
    currentValue = cv2.cvtColor(np.array(currentScreen), cv2.COLOR_RGB2BGR)
    try:
        return int(pytesseract.image_to_string(currentValue))
    except:
        return 100

#Captura screenshot da vida do personagem
def getLife():
    currentScreen = pyautogui.screenshot(region=(1864, 138, 45, 18))
    return convertToInt(currentScreen)

#Captura screenshot da mana do personagem
def getMana():
    currentScreen = pyautogui.screenshot(region=(1864, 152, 45, 18))
    return convertToInt(currentScreen)

#Garante que o personagem se mantenha logado
def unlogout():
    pyautogui.hotkey('CTRL', "UP")
    pyautogui.hotkey('CTRL', "LEFT")
    sleep(4.5 * 60)

#Garante que personagem se alimente
def eatFood():
    pyautogui.hotkey('=')
    pyautogui.hotkey('=')
    sleep(60)

#Realiza a cura da vida do personagem
def healLife():
    while True:
        life = getLife()
        if life < config['percentHealDanger']:
            pyautogui.hotkey('F3')
            sleep(config['timeHealDanger'])
        elif life < config['percentHeal']:
            pyautogui.hotkey('F1')
            sleep(config['timeHeal'])

#Realiza a cura da mana do personagem
def healMana():
    while True:
        mana = getMana()
        if mana < config['percentHealMana']:
            pyautogui.hotkey('F8')
            sleep(config['timeHealMana'])

def findMonster():
    currentScreen = pyautogui.screenshot(region=(1748, 415, 154, 27))
    currentValue = cv2.cvtColor(np.array(currentScreen), cv2.COLOR_RGB2BGR)
    try:
        monstro = str(pytesseract.image_to_string(currentValue))
        if len(monstro) > 0:
            return True
    except:
        return False

#Ataca os montros
def attack():
    while True:
        if findMonster():
            #pyautogui.click(x=1811, y=428)
            pyautogui.hotkey("F2")
            sleep(2)

#Realiza a execução das tarefas em paralelo
if __name__ == "__main__":
    if config['foodMode']:
        threading.Thread(target=eatFood).start()
    if config['unlogoutMode']:
        threading.Thread(target=unlogout).start()
    if config['healMode']:
        threading.Thread(target=healLife).start()
    if config['manaMode']:
        threading.Thread(target=healMana).start()
    if config['attackMode']:
        threading.Thread(target=attack).start()