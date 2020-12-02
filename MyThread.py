from threading import Thread
import cv2
import keyboard
import numpy
from PIL import ImageGrab
import pyautogui as pg


class MyThread(Thread):
    deth = False

    def __init__(self, name, flag=True):
        Thread.__init__(self)
        self.name = name
        self.flag = flag
        self.deth = False
        self.left = int(790 + 70)
        self.right = int(self.left + 190)
        self.top = int(370 + 125)
        self.bot = int(self.top + 772 / 4) - 5
        self.dota_enter = [self.left, self.top, self.right, self.bot]

    def run(self):
        while not self.deth:
            if self.flag:
                screen = numpy.array(ImageGrab.grab(bbox=self.dota_enter))
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                _, threshold1 = cv2.threshold(screen, 252, 255, cv2.THRESH_BINARY)
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 5))
                closed = cv2.morphologyEx(threshold1, cv2.MORPH_CLOSE, kernel)
                closed = cv2.erode(closed, kernel, iterations=1)
                closed = cv2.dilate(closed, kernel, iterations=1)
                (centers, _) = cv2.findContours(closed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                try:
                    pg.sleep(1)
                    x, y = centers[0][0][0]
                    x_min = x
                    y_min = y
                    x_max = x
                    y_max = y
                    for i in range(len(centers[0])):
                        x, y = centers[0][i][0]
                        if x_min > x: x_min = x
                        if (y_min > y): y_min = y
                        if (x_max < x): x_max = x
                        if (y_max < y): y_max = y
                    screen_height = (y_max - y_min)
                    screen_width = (x_max - x_min)
                    s = screen_height * screen_width
                    if (s == 3969):
                        keyboard.send("Enter")
                        print("Я играю в доту и я принимаю это :(")
                        pg.sleep(1)

                except IndexError:
                    False
            else:
                pg.sleep(1)

    def swich_flag(self):
        self.flag = not self.flag
        if (self.flag):
            print("Поиск включен")
        else:
            print("Поиск отключен")

    def deth_Thread(self):
        self.deth = True
