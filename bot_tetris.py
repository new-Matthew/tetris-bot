from locate_pixelcolor_cpppragma import search_colors
import numpy as np
import numexpr
from fast_ctypes_screenshots import(
    ScreenshotOfOneMonitor,
)
from mousekey import MouseKey

mkey = MouseKey()
mkey.enable_failsafekill('ctrl+e')

# blue green red no numpy inverte
green = 42, 127, 25 
light_blue = 44,156,251 
dark_blue = 34,62,141 

r_green = np.array([list(reversed(green))], dtype=np.uint8)
r_light_blue = np.array([list(reversed(light_blue))], dtype=np.uint8)
r_dark_blue = np.array([list(reversed(dark_blue))], dtype=np.uint8)
