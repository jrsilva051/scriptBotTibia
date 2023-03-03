import numpy as np
import pyautogui
from time import sleep
import cv2
import pytesseract
import threading

#Configurações de cura do personagem
config = {
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
def convertString(currentScreen):
    currentValue = cv2.cvtColor(np.array(currentScreen), cv2.COLOR_RGB2BGR)
    try:
        return int(pytesseract.image_to_string(currentValue))
    except:
        return 100

#Captura screenshot da vida do personagem
def getLife():
    currentScreen = pyautogui.screenshot(region=(1864, 138, 45, 18))
    return convertString(currentScreen)

#Captura screenshot da mana do personagem
def getMana():
    currentScreen = pyautogui.screenshot(region=(1864, 152, 45, 18))
    return convertString(currentScreen)

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

#Realiza a execução das tarefas em paralelo
if __name__ == "__main__":
    threading.Thread(target=eatFood).start()
    threading.Thread(target=unlogout).start()
    threading.Thread(target=healLife).start()
    threading.Thread(target=healMana).start()