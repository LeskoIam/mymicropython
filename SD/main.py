__author__ = 'Lesko'
# main.py -- put your code here!
import pyb
from pyblib.leds import LEDS

a = LEDS()
delay = 200
while True:

    print("off()")
    a.off()
    a.delay(1)

    print("on()")
    a.on()
    a.delay(1)

    print("off([1, 2])")
    a.off([1, 2])
    a.delay(1)

    print("off(3)")
    a.off(3)
    a.delay(1)

    print("on()")
    a.on()
    a.delay(1)



