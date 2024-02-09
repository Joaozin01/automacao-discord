import pyautogui
import time

pyautogui.PAUSEedge = 0.3


#abrir discord
time.sleep(3)
pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("discord")
time.sleep(1)
pyautogui.press("enter")
time.sleep(4)


pyautogui.click(x=222, y=361)#clicar no victor
time.sleep(3)
pyautogui.write("E ai, boa noite. O exercicio deu certo.")
