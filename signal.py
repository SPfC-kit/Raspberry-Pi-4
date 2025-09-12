import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT) # 赤
GPIO.setup(21, GPIO.OUT) # 黄
GPIO.setup(26, GPIO.OUT) # 緑

while True:
    # 赤
    GPIO.output(20, 1)
    GPIO.output(21, 0)
    GPIO.output(26, 0)
    time.sleep(2)
    # 黄
    GPIO.output(20, 0)
    GPIO.output(21, 1)
    GPIO.output(26, 0)
    time.sleep(1)
    # 緑
    GPIO.output(20, 0)
    GPIO.output(21, 0)
    GPIO.output(26, 1)
    time.sleep(2)