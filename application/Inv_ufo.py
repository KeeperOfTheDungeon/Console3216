# #include "Arduino.h"
# #include "sprite.h"
import Sprite
# #include "Joystick.h"
import Joystick


PILOT_TRIGGER_UP = 1
PILOT_TRIGGER_BODY = 2


class Ufo(Sprite):
    def __init__(self):
        self._movementPrescaler: int

    def move(self):
        pass

    # Im Original mit Schreibfehler
    def checkCollision(self, xPos: int) -> bool:
        pass

    def explode(self):
        pass
