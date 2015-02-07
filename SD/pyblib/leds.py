__author__ = 'Lesko'
import pyb


class LEDS():
    def __init__(self, debug=False):
        self.debug = debug
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
        """Turn LEDs specified by their id on.
        ids = [1, 2, 3, 4]
        ids = 2
        """
        if type(ids) is int and 0 < ids < 5:
            ids = [ids]
        if len(ids) == 0:
            self._all_on()
        else:
            for xid in ids:
                led = self.leds[xid - 1]
                led.on()
                self._set_led_state(xid - 1, 1)
    
    def off(self, ids=[]):
        """Turn LEDs specified by their id off.
         ids = [1, 2, 3, 4]
         ids = 2
         """
        if type(ids) is int and 0 < ids < 5:
            ids = [ids]
        if len(ids) == 0:
            self._all_off()
        else:
            for xid in ids:
                led = self.leds[xid - 1]
                led.off()
                self._set_led_state(xid - 1, 0)
    
    def toggle(self, ids=[]):
        """Toggle LEDs specified by their id.
         ids = [1, 2, 3, 4]
         ids = 4
         """
        if type(ids) is int and 0 < ids < 5:
            ids = [ids]
        if len(ids) == 0:
            self._all_toggle()
        else:
            for id in ids:
                led = self.leds[id - 1]
                led.toggle()
                new_state = 1 if not self.led_state[id - 1] else 0
                self._set_led_state(id - 1, new_state)

    def delay(self, t):
        pyb.delay(t*1000)

    def print_state(self):
        print (self.led_state)
        return self.led_state

if __name__ == '__main__':
    a = LEDS()

    a.on(2)