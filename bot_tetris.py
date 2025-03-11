from locate_pixelcolor_cpppragma import search_colors
import numpy as np
import numexpr
from fast_ctypes_screenshots import(
    ScreenshotOfOneMonitor,
)
from mousekey import MouseKey
import cv2
import os
import keyboard

ativo = False


def on_off():
    global ativo
    ativo = not ativo


keyboard.add_hotkey('ctrl+alt+s', on_off)

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
min_height = 500
max_height = 700
min_width = 850
max_width = 1000
co = 0

r_green = np.array([list(reversed(green))], dtype=np.uint8)
r_light_blue = np.array([list(reversed(light_blue))], dtype=np.uint8)
r_dark_blue = np.array([list(reversed(dark_blue))], dtype=np.uint8)


with ScreenshotOfOneMonitor(
    monitor=0, ascontiguousarray=False
) as screenshots_monitor:
    while True:
        if ativo:
            co+=1
            print(co, end='\r')

            pic = screenshots_monitor.screenshot_one_monitor()

            green_result = search_colors(pic=pic, colors=r_green, cpus=cpus)
            blue_light_result = search_colors(pic=pic, colors=r_light_blue, cpus=cpus)
            blue_dark_result = search_colors(pic=pic, colors=r_dark_blue, cpus=cpus)

            green_result_filter = green_result[((green_result[..., 1] > min_width)
                                                    & (green_result[..., 1] < max_width)) & (
                                                                (green_result[..., 0] > min_height)
                                                                & (green_result[..., 0] < max_height))]
            blue_light_result_filter = blue_light_result[((blue_light_result[..., 1] > min_width)
                                                    & (blue_light_result[..., 1] < max_width)) & (
                                                                (blue_light_result[..., 0] > min_height)
                                                                & (blue_light_result[..., 0] < max_height))]
            blue_dark_result_filter = blue_dark_result[((blue_dark_result[..., 1] > min_width)
                                                    & (blue_dark_result[..., 1] < max_width)) & (
                                                                (blue_dark_result[..., 0] > min_height)
                                                                & (blue_dark_result[..., 0] < max_height))]
            if np.any(blue_light_result_filter) and np.any(blue_dark_result_filter) and np.any(green_result_filter):
                x,y=int(np.mean(green_result_filter[...,1])),int(np.mean(green_result_filter[...,0]))
                mkey.left_click_xy(x, y)
                #mkey.move_to_natural(x,y)

# cv2.imwrite(file_path, pic)