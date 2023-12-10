# #include "Arduino.h"
# #include "sprite.h"
import Sprite
# #include "Joystick.h"
import Joystick


PILOT_TRIGGER_UP = 1
PILOT_TRIGGER_BODY = 2


class Pilot(Sprite):
    def __init__(self):
        # TODO C++: Joystick *joystick;
        self._joystick: Joystick

        self._movementCounter: int
        self._movementPrescaler: int

        self._moved: int

    # TODO C++: void init(Joystick & myJoystick);
    def init(self, myJoystick: Joystick):
        pass

    def checkActions(self):
        pass
