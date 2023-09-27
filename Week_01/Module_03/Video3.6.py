#-----------------------------------------------------------------------------------------------------------------------
# 3.6 install external packages pyautogui and opencv
#-----------------------------------------------------------------------------------------------------------------------
from time import *
import cv2

# PyAutoGUI installation (https://youtu.be/1gjN1TAM3UU?si=QeB3UIhQeJkMfw8M)
# To Learn more, visit (https://pypi.org/project/PyAutoGUI/).

import pyautogui
print(pyautogui.__version__)
#-----------------------------------------------------------------------------------------------------------------------
for i in range(0, 3):
    sleep(3)
    pyautogui.write('How awesome Python is !!!', interval=0.2)
    pyautogui.press('enter')

# The above code will wait for 3 second, will write automatically, and will press enter.
# This will execute for 3 times.
#-----------------------------------------------------------------------------------------------------------------------

# OpenCV-Contrib-Python installation.
# To Learn more, visit (https://pypi.org/project/opencv-contrib-python/).

webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    cv2.imshow('My webcam:', frame)
    cv2.waitKey(1)

# The code above will open up a window, will connect with my webcam and will show the live feed.
#-----------------------------------------------------------------------------------------------------------------------
