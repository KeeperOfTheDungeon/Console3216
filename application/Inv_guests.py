# #include "Arduino.h"
# #include "sprite.h"
import Sprite

# TODO inv_guests.cpp does not exist, prototype from inc/inv_guests.h


class Guests(Sprite.Sprite):
    def __init__(self):
        self._vectorY: int

        self._movementPrescaler: int
        self._active: bool

    def move(self):
        pass

    def draw(self):
        pass

    def activate(self):
        pass

    def deActivate(self):
        pass

    def setDirection(self, direction: bool):
        pass

    def isActive(self) -> bool:
        pass
