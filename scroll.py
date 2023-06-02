import time
from pynput.mouse._darwin import Button, Controller as MouseController
from pynput.keyboard._darwin import Key, Controller as KeyboardController

from mss import mss, tools

mouse = MouseController()
keyboard = KeyboardController()

# print("moving mouse")
# mouse.position = (1406, 832)
time.sleep(15)
print("starting 'camera'")
counter = 0
with mss() as sct:
    while True:
        # The screen part to capture
       # mouse.click(Button.left)
        monitor = {"top": 137, "left": 453, "width": 534, "height": 755} #click once on the page and then move mouse off the page
        sct_img = sct.grab(monitor)
        tools.to_png(sct_img.rgb, sct_img.size, output=f"image-{counter}.png")
#50%
#519 167 920 733
#monitor = {"top": 167, "left": 519, "width": 401, "height": 566}

#60%
#453 137 987 892 
#monitor = {"top": 137, "left": 453, "width": 534, "height": 755}


        for _ in range(29):
            keyboard.press(Key.down)

        print("sleeping")
        time.sleep(2)


        counter += 1

