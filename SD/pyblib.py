import pyb
 
class MyLEDS():
    def __init__(self, debug=False):
        self.leds = (pyb.LED(1), pyb.LED(2), pyb.LED(3), pyb.LED(4))
        self.led_state = [0, 0, 0, 0]
        self.off()

    def _debug(self, message):
        if self.debug:
            print(message)
            
    def _set_led_state(self, pos, state):
        """Track state of LEDs and do some error checking."""
        if type(state) != int or state not in [0, 1]:
            raise TypeError("haha")
        self.led_state[pos] = state
    
    def _all_off(self):
        """Turn all onboard LEDs off."""
        for n, led in enumerate(self.leds):
            led.off()
            self._set_led_state(n, 0)
     
    def _all_on(self):
        """Turn all onboard LEDs on."""
        for n, led in enumerate(self.leds):
            led.on()
            self._set_led_state(n, 1)
     
    def _all_toggle(self):
        """Toggle all onboard LEDs."""
        for n, led in enumerate(self.leds):
            led.toggle()
            new_state = 1 if not self.led_state[n] else 0
            self._set_led_state(n, new_state)
    
    def on(self, ids=[]):
        """Turn LEDs specified by their id [1, 2, 3, 4] on."""
        if len(ids) == 0:
            self._all_on()
        else:
            for id in ids:
                led = self.leds[id - 1]
                led.on()
                self._set_led_state(id - 1, 1)
    
    def off(self, ids=[]):
        """Turn LEDs specified by their id [1, 2, 3, 4] off."""
        if len(ids) == 0:
            self._all_off()
        else:
            for id in ids:
                led = self.leds[id - 1]
                led.off()
                self._set_led_state(id - 1, 0)
    
    def toggle(self, ids=[]):
        """Toggle LEDs specified by their id [1, 2, 3, 4] off."""
        if len(ids) == 0:
            self._all_toggle()
        else:
            for id in ids:
                led = self.leds[id - 1]
                led.toggle()
                new_state = 1 if not self.led_state[id - 1] else 0
                self._set_led_state(id - 1, new_state)
            
    def print_state(self):
        print (self.led_state)
        return self.led_state