import cv2
from time import time
import numpy as np
import pytesseract
from PIL import ImageGrab
from PIL import Image
from mss import mss
import os
import pyautogui
import pygetwindow
import time
from playsound import playsound
from tkinter import *

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print('How much money did you start with:')
money_now = input()
money_now = float(money_now)
rich_money = float(money_now + money_now * 2/100)
poor_money = float(money_now - money_now * 2/100)

a=0
while True:
    a = a + 1

    img = ImageGrab.grab(bbox=(140, 400, 300, 450))                     # x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", img_np)                                         #shows screen live

    text = pytesseract.image_to_string(img_np, config='digits')
    # text = pytesseract.image_to_string(img_np)

    # print(float(text))

    try:
        if float(text) >= rich_money:
            playsound('C:\\Business\\CryptoAlarm\\Hey.mp3')
            print(float(text), '-> +2% SELL NOW, YOU RICH!!')

        elif float(text) <= poor_money:
            playsound('C:\\Business\\CryptoAlarm\\Fart.mp3')
            print(float(text), '-> -2% SELL TO SAVE YOUR ASS')
        else:
             print('Keep it up champ,', "{:.2f}".format(float(rich_money - float(text))), 'more to collect')
    except Exception:
        pass

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# print(a)

cv2.destroyWindow
