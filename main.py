# main.py -- put your code here!
import pyb
from pyblib import MyLEDS

a = MyLEDS()
delay = 200
while True:
    a.on()
    a.print_state()
    pyb.delay(delay)
    
    a.off([2, 3, 1])
    a.print_state()
    pyb.delay(delay)
    
    a.toggle([4])
    a.print_state()
    pyb.delay(delay)
    
    a.toggle([1, 3, 2])
    a.print_state()
    pyb.delay(delay)
    
    a.toggle()
    a.print_state()
    pyb.delay(delay)
    
    a.off()
    a.print_state()
    pyb.delay(delay)
    
    a.on()
    a.print_state()
    pyb.delay(delay)
    
    a.off()
    a.print_state()
    pyb.delay(delay)
    