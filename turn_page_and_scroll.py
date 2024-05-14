import time 
import pyautogui
import getpixelcolor
from pynput.mouse._darwin import Button, Controller as MouseController
from pynput.keyboard._darwin import Key, Controller as KeyboardController

from mss import mss, tools

mouse = MouseController()
keyboard = KeyboardController()

#Moves the mouse to a random part of the screen, clicks the screen

time.sleep(2)
print("moving mouse")
mouse.position = (1386, 500) 
mouse.click(Button.left)

time.sleep(2)
print("starting 'camera'")


counter = 0
with mss() as sct:
    while True:

        time.sleep(3)
        mouse.position = (1386, 500)
        pyautogui.scroll(-1)
        c = getpixelcolor.pixel(1397,218) #top
        c1 = getpixelcolor.pixel(1397,511) #bottom
        c2 = getpixelcolor.pixel(369,369)  #random
        print(c)
        print(c1)
        print(c2)
        time.sleep(4)

    # Contents page is blue
        if c2[0] != 255 : 

            pyautogui.scroll(1)
            time.sleep(2)

            monitor = {"top": 179, "left": 466, "width": 494, "height": 704} 
            sct_img = sct.grab(monitor)
            tools.to_png(sct_img.rgb, sct_img.size, output=f"image17-{counter}.png")

            print("1st taken blue")
            time.sleep(2)
            counter += 1


    # If the page is not blue, it is not the contents page
        else:
        
            print("else")

         # 1 screenshot
            if c[0] == 255 and c1 == 255:
                pyautogui.scroll(1)
                time.sleep(2)

                monitor = {"top": 179, "left": 466, "width": 494, "height": 704} 
                sct_img = sct.grab(monitor)
                tools.to_png(sct_img.rgb, sct_img.size, output=f"image17-{counter}.png")

                print("1st taken white")
                time.sleep(2)
                counter += 1


        # 2 screenshots
            if c[0] == 127 and c1[0] == 127: 
                pyautogui.scroll(1)
                time.sleep(2)

                monitor = {"top": 179, "left": 466, "width": 494, "height": 704} 
                sct_img = sct.grab(monitor)
                tools.to_png(sct_img.rgb, sct_img.size, output=f"image17-{counter}.png")

                print("1st taken")
                time.sleep(2)
                counter += 1

                pyautogui.scroll(-17.5)

                monitor = {"top": 179, "left": 466, "width": 494, "height": 704} 
                sct_img = sct.grab(monitor)
                tools.to_png(sct_img.rgb, sct_img.size, output=f"image17-{counter}.png")

                print("2nd taken")
                time.sleep(2)
                counter += 1

        # 3 screenshots
            if c[0] == 127 and c1[0] == 255: 
                pyautogui.scroll(1)
                time.sleep(1)

                monitor = {"top": 179, "left": 466, "width": 494, "height": 704} 
                sct_img = sct.grab(monitor)
                tools.to_png(sct_img.rgb, sct_img.size, output=f"image17-{counter}.png")

                print("1st taken")
                time.sleep(2)
                counter += 1

                pyautogui.scroll(-17.5)
                time.sleep(1)

                monitor = {"top": 179, "left": 466, "width": 494, "height": 704} 
                sct_img = sct.grab(monitor)
                tools.to_png(sct_img.rgb, sct_img.size, output=f"image17-{counter}.png")
      
                print("2nd taken")
                time.sleep(2)
                counter += 1


                pyautogui.scroll(-17.5)
                time.sleep(1)

                monitor = {"top": 179, "left": 466, "width": 494, "height": 704} 
                sct_img = sct.grab(monitor)
                tools.to_png(sct_img.rgb, sct_img.size, output=f"image17-{counter}.png")

                print("3rd taken")
                time.sleep(2)
                counter += 1 
       

        mouse.position = (1386, 543) #MOVE TO THE BUTTON
        mouse.click(Button.left)

        print("please")
        time.sleep(2)
        
         