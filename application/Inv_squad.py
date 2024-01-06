import random

# #include "Arduino.h"
# #include "sprite.h"
import Sprite
# #include "Joystick.h"
import Joystick
# #include "inv_alien.h"
from Inv_alien import Alien

# TODO Schreibfehler behoben: ALLIENS_SQUAD_MAX_SIZE -> ALIENS_SQUAD_MAX_SIZE
ALIENS_SQUAD_MAX_SIZE: int = 24


# TODO typedef struct {...} SquadMember_t
class SquadMember_t:
    def __init__(self):
        self.type: int
        self.xDelta: int
        self.yDelta: int

alienSquads: SquadMember_t = [[0 for x in range(ALIENS_SQUAD_MAX_SIZE)] for y in range(2)]


class Squad:
    def __init__(self):
        self._type: int
        self._movementCounter: int
        self._movementPrescaler: int
        # TODO C++: Alien aliens[ALLIENS_SQUAD_MAX_SIZE];
        self._aliens: Alien = [0 for x in range(ALIENS_SQUAD_MAX_SIZE)]
        # TODO Schreibfehler behoben: _moviePrescaller -> _movePrescaler
        self._movePrescaler: int

    def prepareSquad(self):
        pass

    def draw(self):
        for alienIndex in range(ALIENS_SQUAD_MAX_SIZE):
            self._aliens[alienIndex].draw()
        pass

    def move(self):
        alienMaxXPos: int = 0
        alienMinXPos: int = 31

        self._movePrescaler += 1
        if self._movePrescaler < 4:
            return

        self._movePrescaler = 0
        for squadCounter in ALIENS_SQUAD_MAX_SIZE:
            if alienMaxXPos < self._aliens[squadCounter].getXPos():
                alienMaxXPos = self._aliens[squadCounter].getXPos()
            
            if alienMinXPos > self._aliens[squadCounter].getXPos():
                alienMinXPos = self._aliens[squadCounter].getXPos()
            
        direction: bool

        randomNr = random.randrange(3)
        # TODO Source C++ code was Switch/Case
        if randomNr == 0:
            if alienMaxXPos < 31:
                direction = True

                for squadCounter in range(ALIENS_SQUAD_MAX_SIZE):
                    self._aliens[squadCounter].move(direction)
        elif randomNr == 2:
            if alienMinXPos > 0:
                direction = False

                for squadCounter in range(ALIENS_SQUAD_MAX_SIZE):
                    self._aliens[squadCounter].move(direction)
        pass

    # TODO No definition in C++ source
    def descent(self):
        pass

    # TODO C++ Source had a typo: checkColision
    def checkCollision(self, xPos: int, yPos: int) -> int:
        # TODO Unused in C++ source
        # alienXPos: int
        # alienYPos: int
        points: int = 0

        for squadCounter in range(ALIENS_SQUAD_MAX_SIZE):
            if self._aliens[squadCounter].isActive():
                if self._aliens[squadCounter].getXPos() == xPos:
                    if self._aliens[squadCounter].getYPos() == yPos:
                        self._aliens[squadCounter].deActivate()
                        points = self._aliens[squadCounter].getPoints()
        
        return points
