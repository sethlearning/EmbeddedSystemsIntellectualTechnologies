from gpiozero import LED
from time import sleep
from gpiozero import Button

button = Button(2)
led = LED(25)

button.wait_for_active()
# button.wait_for_inactive()
led.on()
sleep(3)
led.off()