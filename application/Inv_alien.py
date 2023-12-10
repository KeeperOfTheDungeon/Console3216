# #include "Arduino.h"
# #include "sprite.h"
import Sprite
# #include "Joystick.h"
import Joystick


ALIEN_TYPE_NONE = 0
ALIEN_TYPE_SCOUT = ALIEN_TYPE_NONE + 1
ALIEN_TYPE_FIGHTER = ALIEN_TYPE_SCOUT + 1
ALIEN_TYPE_BOMBER = ALIEN_TYPE_FIGHTER + 1

ALIEN_POINTS_NONE = 0
ALIEN_POINTS_SCOUT = 5
ALIEN_POINTS_FIGHTER = 10
ALIEN_POINTS_BOMBER = 20


class Alien(Sprite):
    def __init__(self):
        self._type: int
        self._movementCounter: int
        self._movementPrescaler: int

    def setType(self, newType: int):
        pass

    def getType(self) -> int:
        pass

    def getPoints(self) -> int:
        pass

    def move(self, direction: bool):
        pass

    def descent(self):
        pass
