# #include "Arduino.h"
# #include "sprite.h"
import Sprite

import Display

class Projectile(Sprite):
    def __init__(self):
        super().__init__(0, 0, 1, 1)
        self._vectorY: int

        self._movementPrescaler: int
        self._active: bool

        self._bitmap[0] = Display.getColor(4, 7, 0)

    def move(self):
        if self._yPos > 0 and self._yPos < 16:
            self._yPos += self._vectorY
        else:
            self.deActivate()
        pass

    def setDirection(self, direction: bool):
        if direction:
            self._vectorY = 1
        else:
            self._vectorY = -1
        pass
