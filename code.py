import time

import board
import digitalio as dio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print("---Pico Pad Keyboard---")

led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT
led.value = True

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)