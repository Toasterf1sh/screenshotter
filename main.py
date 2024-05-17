import time
from pynput.mouse._darwin import Button, Controller

from mss import mss, tools

mouse = Controller()

print("moving mouse")

# Replace x, y with coordinates of the page turn button
mouse.position = (x, y)


print("starting 'camera'")
counter = 0
with mss() as sct:
    while True:

        # Replace x,y,a,b with respective coordinates of the dimensions 
        # of the size of screenshot to be taken: 
        
        # top - top left corner y component
        # left - top left corner x component
        # width - bottom right corner x component
        # height - bottom right corner y component

        monitor = {"top": y, "left": x, "width": a, "height": b}
        sct_img = sct.grab(monitor)
        tools.to_png(sct_img.rgb, sct_img.size, output=f"image-{counter}.png")

        print("sleeping")
        time.sleep(2)

        # For screenshotting the full page, replace "sct.grab(monitor)" with: 
        # sct.shot(output=f"snip{counter}.png")
        mouse.click(Button.left)

        counter += 1

