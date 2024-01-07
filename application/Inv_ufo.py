# #include "Arduino.h"
# #include "sprite.h"
import Sprite
# #include "Joystick.h"
import Joystick

import Display

PILOT_TRIGGER_UP = 1
PILOT_TRIGGER_BODY = 2


class Ufo(Sprite):
    def __init__(self):
        # TODO Super constructor call
        super().__init__(0, 0, 1, 1)

        self._movementPrescaler: int

        # TODO GetColor
        self._bitmap[0] = Display.getColor(7, 7, 7)
        self.activate()
        self._yPos = 0

    def move(self):
        self._xPos += 1
        if self._xPos > 31:
            self.deActivate()
        pass

    # Im Original mit Schreibfehler
    def checkCollision(self, xPos: int) -> bool:
        pass

    def explode(self):
        pass
