# #include "Arduino.h"
# #include "sprite.h"
import Sprite

import Display

class Ball(Sprite):
    def __init__(self):
        # TODO Super constructor call
        super().__init__(0, 0, 1, 1)

        self._bitmap[0] = Display.getColor(7, 0, 0)
        self.activate()

        self._vectorX: int = -1
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
        if self._movementCounter >= self._movementPrescaler:
            self._intPosX += self._vectorX
            self._intPosY += self._vectorY

            # TODO
            self._xPos = self._intPosX >> 4
            self._yPos = self._intPosY >> 4

            self._movementCounter = 0
            self._moved = 1
        else:
            self._movementCounter += 1
            self._moved = 0
        pass

    def setVector(self, x: int, y: int):
        pass

    def bounce(self):
        self._vectorX = - self._vectorX
        self._vectorY = - self._vectorY

        # randomize
        self._vectorY = self._randomizeVector(self._vectorY)
        self._vectorX = self._randomizeVector(self._vectorX)

        self._correctVector()
        pass

    def bounceX(self):
        self._vectorX = - self._vectorX

        # randomize
        # vector darf das Vorzeichen nicht wechseln
        self._vectorY = self._randomizeVector(self._vectorY)
        self._vectorX = self._randomizeVector(self._vectorX)

        self._correctVector()
        pass

    def bounceY(self):
        self._vectorY = - self._vectorY

        # randomize
        self._vectorY = self._randomizeVector(self._vectorY)
        self._vectorX = self._randomizeVector(self._vectorX)

        self._correctVector()
        pass

    def hasMoved(self) -> bool:
        pass

    def _correctVector(self):
        pass

    def _randomizeVector(vector: int) -> int:
        pass
