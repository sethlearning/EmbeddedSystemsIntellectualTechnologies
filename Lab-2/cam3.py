from gpiozero import LED
from gpiozero import Button
import time
from picamera2 import Picamera2, Preview

red = LED(25)
green = LED(24)
bt = Button(23)

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
i = 0

bt.wait_for_active()
time.sleep(0.5)

while True:
    if (bt.is_active):
        red.off()
        green.off()
        break
    green.on()
    red.off()
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    time.sleep(2)
    green.off()
    red.on()
    # picam2.start_and_capture_file(f'test{i}.jpg')
    picam2.capture_file(f'test{i}.jpg')
    picam2.stop_preview()
    picam2.stop()
    time.sleep(1)
    i += 1

green.off()
red.off()

# picam2.start_and_capture_file("test.jpg")