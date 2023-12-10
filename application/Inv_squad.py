# #include "Arduino.h"
# #include "sprite.h"
import Sprite
# #include "Joystick.h"
import Joystick
# #include "inv_alien.h"
from Inv_alien import Alien

# TODO Schreibfehler behoben: ALLIENS_SQUAD_MAX_SIZE -> ALIENS_SQUAD_MAX_SIZE
ALIENS_SQUAD_MAX_SIZE: int = 24


class Squad:
    def __init__(self):
        self._type: int
        self._movementCounter: int
        self._movementPrescaler: int
        # TODO C++: Alien aliens[ALLIENS_SQUAD_MAX_SIZE];
        self._aliens: Alien = [] * ALIENS_SQUAD_MAX_SIZE
        # TODO Schreibfehler behoben: _moviePrescaller -> _movePrescaler
        self._movePrescaler: int

    def prepareSquad(self):
        pass

    def draw(self):
        pass

    def move(self):
        pass

    def descent(self):
        pass

    def checkColision(self, xPos: int, yPos: int) -> int:
        pass
