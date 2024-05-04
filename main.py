import time
from pynput.mouse._darwin import Button, Controller

from mss import mss, tools

mouse = Controller()

print("moving mouse")

# This should be the coordinates of the page turn button
mouse.position = (1406, 832)

#Screen capture sizes for different textbook readers below: 

#campion 
    # mouse.position = (1083.30859375, 166.30859375)
    # monitor = {"top": 202, "left": 468, "width": 481, "height": 694}

#pearson
    # mouse.position = (1406, 832)
    # monitor = {"top": 186, "left": 519, "width": 496, "height": 698}

#iitomo (pearson)
    # mouse.position = (1406, 832)
    # monitor = {"top": 186, "left": 488, "width": 557, "height": 699}

#signpost (pearson)
    # mouse.position = (1406, 832)
    # monitor = {"top": 186, "left": 501, "width": 531, "height": 698}

print("starting 'camera'")
counter = 0
with mss() as sct:
    while True:
        
        # Replace this with the coordinates of the top left and bottom right corners of the page
        monitor = {"top": 186, "left": 501, "width": 531, "height": 698}
        
        sct_img = sct.grab(monitor)
        tools.to_png(sct_img.rgb, sct_img.size, output=f"image-{counter}.png")

        print("sleeping")
        time.sleep(2)

        # sct.shot(output=f"snip{counter}.png")
        mouse.click(Button.left)

        counter += 1

