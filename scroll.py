# This is a program that 


# When starting the program, click once on the page and 
# then move mouse off the area that is to be captured

import time
from pynput.mouse._darwin import Button, Controller as MouseController
from pynput.keyboard._darwin import Key, Controller as KeyboardController
from mss import mss, tools

mouse = MouseController()
keyboard = KeyboardController()

# This is how long the program waits to execute after starting
time.sleep(15)

print("starting 'camera'")
counter = 0
with mss() as sct:
    while True:

        # The screen part to capture
        # mouse.click(Button.left)
        monitor = {"top": 137, "left": 453, "width": 534, "height": 755} 
        sct_img = sct.grab(monitor)
        tools.to_png(sct_img.rgb, sct_img.size, output=f"image-{counter}.png")

# For A4 size while chrome browser is 50%
# Replace line 20 with
# monitor = {"top": 167, "left": 519, "width": 401, "height": 566}

# For A4 size while chrome browser is 60%
#453 137 987 892 
#monitor = {"top": 137, "left": 453, "width": 534, "height": 755}

        # This will press the down arrow key 29 times 
        # May have to adjust this depending on the browser that is used
        for _ in range(29):
            keyboard.press(Key.down)

        print("sleeping")
        time.sleep(2)

        counter += 1

