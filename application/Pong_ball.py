# #include "Arduino.h"
# #include "sprite.h"
import Sprite


class Ball(Sprite):
    def __init__(self):
        self._vectorX: int
        self._vectorY: int

        self._intPosX: int
        self._intPosY: int

        self._movementCounter: int
        self._movementPrescaler: int

        # TODO C++: uint8_t moved:1;
        self._moved: int

    def setPosition(self, newXPos: int, newYPos: int):
        pass

    def increaseSpeed(self):
        pass

    def decreaseSpeed(self):
        pass

    def setSpeed(self, newSpeed: int):
        pass

    def move(self):
        pass

    def setVector(self, x: int, y: int):
        pass

    def bounce(self):
        pass

    def bounceX(self):
        pass

    def bounceY(self):
        pass

    def hasMoved(self) -> bool:
        pass

    def _correctVector(self):
        pass

    def _randomizeVector(vector: int) -> int:
        pass
