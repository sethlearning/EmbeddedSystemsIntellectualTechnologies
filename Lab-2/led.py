from gpiozero import LED
from gpiozero import Button
import time

red = LED(25)
green = LED(24)
bt = Button(23)

red.on()
green.on()

bt.wait_for_active()

red.off()
green.off()

# time.sleep(2)