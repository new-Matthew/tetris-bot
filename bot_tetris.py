from locate_pixelcolor_cpppragma import search_colors
import numpy as np
import numexpr
from fast_ctypes_screenshots import(
    ScreenshotOfOneMonitor,
)
from mousekey import MouseKey
import cv2
import os

mkey = MouseKey()
mkey.enable_failsafekill('ctrl+e')

base_path = os.path.expanduser('~')
dir_path = os.path.join(base_path, 'Desktop', 'airdrop-autobot', 'bot-tetris')
file_path = os.path.join(dir_path, 'imgresult.png')

# rgb no numpy inverte para bgr
green = 42, 127, 25
light_blue = 44,156,251
dark_blue = 34,62,141
cpus=5
r_green = np.array([list(reversed(green))], dtype=np.uint8)
r_light_blue = np.array([list(reversed(light_blue))], dtype=np.uint8)
r_dark_blue = np.array([list(reversed(dark_blue))], dtype=np.uint8)

with ScreenshotOfOneMonitor(
    monitor=0, ascontiguousarray=False
) as screenshot_monitor:
    pic = screenshot_monitor.screenshot_one_monitor()
colors0 = np.array([[255, 255, 255]], dtype=np.uint8)
resus0 = search_colors(pic=pic, colors=colors0, cpus=cpus)
cv2.imwrite(file_path, pic)