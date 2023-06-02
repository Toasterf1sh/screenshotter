import time
from pynput.mouse._darwin import Button, Controller

from mss import mss, tools

mouse = Controller()

print("moving mouse")
mouse.position = (1406, 832)

#for campion 
    # mouse.position = (1083.30859375, 166.30859375)
    # monitor = {"top": 202, "left": 468, "width": 481, "height": 694}

#for pearson
    # mouse.position = (1406, 832)
    # monitor = {"top": 186, "left": 519, "width": 496, "height": 698}

#for iitomo (pearson)
    # mouse.position = (1406, 832)
    # monitor = {"top": 186, "left": 488, "width": 557, "height": 699}

#for signpost (pearson)
    # mouse.position = (1406, 832)
    # monitor = {"top": 186, "left": 501, "width": 531, "height": 698}

print("starting 'camera'")
counter = 0
with mss() as sct:
    while True:
        # The screen part to capture
        monitor = {"top": 186, "left": 501, "width": 531, "height": 698}
        sct_img = sct.grab(monitor)
        tools.to_png(sct_img.rgb, sct_img.size, output=f"image-{counter}.png")

        print("sleeping")
        time.sleep(2)

        # sct.shot(output=f"snip{counter}.png")
        mouse.click(Button.left)

        counter += 1

