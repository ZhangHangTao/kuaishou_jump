import pyautogui
import time
import xlrd
import pyperclip
from PIL import ImageGrab
import random
import  win32gui
import win32api
from pymouse import PyMouse
from pynput.mouse import Button, Controller




while True:
    # x1, y1 = pyautogui.position()
    # posStr = "Position:" + str(x1).rjust(4) + ',' + str(y1).rjust(4)
    # print(posStr)
    towards = 0  # 0左1右
    time.sleep(1.5)
    while 1:
        k1 = 390 #右
        k2 = 383 #左
        imagegg = ImageGrab.grab()
        im_pixelgg = imagegg.load()
        pixelgg = im_pixelgg[1178, 109]
        r_guanggao=pixelgg[0];
        m = PyMouse()
        if abs(r_guanggao-162)<2 :
            m.click(1186, 105)
            print('已帮您关闭广告')
        #关闭红包
        pixelhb = im_pixelgg[971, 747]
        r_guanggao = pixelhb[0];
        g_guanggao = pixelhb[1];
        b_guanggao = pixelhb[2];
        if abs(r_guanggao-254)<3  and g_guanggao <50 and b_guanggao<80:
            m.click(971, 747)
            print('已帮您关闭红包')

        location1 = pyautogui.locateCenterOnScreen('tigerRight.png', confidence=0.75)
        location2 = pyautogui.locateCenterOnScreen('tigerLeft.png', confidence=0.75)
        if location1 is not None and location2 is None:
            x = int(location1.x)
            y = int(location1.y)
            towards=1
            print('准备向右跳')
            break
        if location2 is not None and location1 is None:
            x = int(location2.x)
            y = int(location2.y)
            towards=0
            print('准备向左跳')
            break
        else :
            print('搜索小老虎中...')

    if towards==1 : #向右
        y += 65
        x += 2
        # y -= 57

        image = ImageGrab.grab()
        im_pixel = image.load()
        startpoint=True
        edge1=True
        edge2=True
        line = []
        color=248
        edge=0
        first=1
        while edge1 or edge2 :
            x=x+1
            y=y-0.57
            pixel = im_pixel[x, y]
            r=pixel[0]
            g=pixel[1]
            b=pixel[2]
            # print(pixel)
            dc = win32gui.GetDC(0)
            red = win32api.RGB(0, 0, 0)
            win32gui.SetPixel(dc, int(x), int(y), red)
            line.append(r)
            if len(line)>65 and abs(r-237)<7 and b>170:
                startpoint=False
            if startpoint==False:
                if r >color and g>190 and b>150:
                    edge1=False
                    if first:
                        edge=len(line)
                        first=0
                        # print('边界1')
                if edge1==False and r <color and g<150 and b>228:
                    edge2=False
                    # print('边界2')
            if  x>1910 or y> 1070 :
                exit(0)

        distant= (edge + len(line))/2
        # print(distant)
        # exit(3)
        mouse = Controller()
        mouse.press(Button.left)
        if len(line)>270:
            k1=394
        if len(line)<220:
            k1=394
        time.sleep(distant/k1)
        mouse.release(Button.left)
        print('跳跃距离:'+str(len(line)))

        time.sleep(0.8)

    elif towards==0 : #向左
        y += 61
        x += 30
        # x += 100
        # y -= 57

        image = ImageGrab.grab()
        im_pixel = image.load()
        startpoint=True
        edge1=True
        edge2=True
        line = []
        color=247
        edge=0
        first = 1
        while edge1 or edge2 :
            x=x-1
            y=y-0.57
            pixel = im_pixel[x, y]
            r=pixel[0]
            g=pixel[1]
            b=pixel[2]
            # print(pixel)
            dc = win32gui.GetDC(0)
            red = win32api.RGB(0, 0, 0)
            win32gui.SetPixel(dc, int(x), int(y), red)
            line.append(r)
            if len(line)>80 and abs(r-237)<14 and g<150 and b>200:
                startpoint=False
            if startpoint==False:
                if r >color and g>200 and b>160:
                    edge1=False
                    if first:
                        edge=len(line)
                        first=0
                        # print('边界1')

                if edge1==False and r <color and g<150 and b>200:
                    edge2=False
            if  x>1910 or y> 1070 :
                print('超出屏幕了要')
                exit(0)


        distant= (edge + len(line))/2
        # print(distant)
        # exit(3)
        mouse = Controller()
        mouse.press(Button.left)
        #跳远了就变大.跳近了就变小
        if len(line)>370:
            k2=398
        if len(line)<285:
            k2=388
        time.sleep(distant/k2)
        mouse.release(Button.left)
        print('跳跃距离:'+str(len(line)))
        time.sleep(0.8)

