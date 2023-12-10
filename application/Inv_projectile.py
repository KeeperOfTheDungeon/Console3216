# #include "Arduino.h"
# #include "sprite.h"
import Sprite


class Projectile(Sprite):
    def __init__(self):
        self._vectorY: int

        self._movementPrescaler: int
        self._active: bool

    def move(self):
        pass

    def setDirection(self, direction: bool):
        pass
