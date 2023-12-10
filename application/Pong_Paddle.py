# #include "Arduino.h"
# #include "sprite.h"
import Sprite

EVENT_NO_BOUNCE: int = 0
EVENT_BOUNCE_MIDDLE: int = 1
EVENT_BOUNCE_LOW: int = 2
EVENT_BOUNCE_HIGH: int = 3
EVENT_BOUNCE_MIDDLE_BEND: int = 4

PADDLE_IDLE: int = 0
PADDLE_BEND: int = 1
PADDLE_HOLD: int = 2


class Paddle(Sprite):
    def __init__(self):
        self._orientation: bool
        self._status: int
        self._bounceSoundEffect: int

    def setOrientation(self, paddleOrientation: bool):
        pass

    def setBounceSoundEffect(self, newBounceSoundEffect: int):
        # TODO Siehe inline Funktion weiter unten für C++ Code
        self._bounceSoundEffect = newBounceSoundEffect

    def bend(self):
        pass

    def unBend(self):
        pass

    def isBend(self) -> bool:
        pass

    def move(self, direction: bool):
        pass

    def checkContact(self, xPos: int, yPos: int):
        pass

# inline void Paddle::setBounceSoundEffect(uint8_t newBounceSoundEffect)
# {
# 	this->bounceSoundEffect = newBounceSoundEffect;
# }
