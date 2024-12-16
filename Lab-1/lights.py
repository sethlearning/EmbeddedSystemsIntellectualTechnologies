from gpiozero import LED
from time import sleep
from gpiozero import Button

button = Button(2)
green = LED(25)
yellow = LED(24)
red = LED(23)
mode = 0

# button.wait_for_active()
# green.on()
# yellow.on()
# red.on()
# sleep(3)

def normal():
    green.on()
    sleep(1)
    green.off()
    for i in range(5):
        yellow.on()
        sleep(0.1)
        yellow.off()
        sleep(0.1)
    red.on()
    sleep(1)
    red.off()

def alarm():
    for i in range(5):
        yellow.on()
        sleep(0.1)
        yellow.off()
        sleep(0.1)

def pedestrians():
    green.on()
    sleep(1)
    green.off()
    for i in range(5):
        green.on()
        sleep(0.1)
        green.off()
        sleep(0.1)
    red.on()
    sleep(1)
    red.off()

while True:
    if button.is_active == True:
        mode = (mode + 1) % 3
    if mode == 0:
        normal()
    elif mode == 1:
        alarm()
    else:
        pedestrians()
