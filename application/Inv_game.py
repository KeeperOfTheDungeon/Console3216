# #include "game.h"
import Game
# #include "inv_pilot.h"
from Inv_pilot import Pilot
# #include "inv_ufo.h"
import Inv_ufo
# #include "inv_projectile.h"
from Inv_projectile import Projectile
# #include "inv_alien.h"
import Inv_alien
# #include "inv_squad.h"
import Inv_squad
# #include "Joystick.h"
import Joystick


class Invaders(Game):
    def __init__(self, leftJoystick: Joystick, rightJoystick: Joystick):
        self._pilot: Pilot
        self._pilotProjectile: Projectile
        self._invadersProjectile: Projectile

        self._player1Points: int

        # TODO C++: uint8_t movePrescaller;
        # TODO Rechtschreibfehler behoben: _movePrescaller -> _movePrescaler
        self._movePrescaler: int
        self._active: bool

    def play(self):
        pass

    def draw(self):
        pass

    def prepareDemo(self):
        pass

    def playDemo(self):
        pass

    def playGame(self):
        pass

    def process(self):
        pass

    def _movePlayer(self):
        pass

    def _drawField(self):
        pass

    def _checkBoundarys(self) -> int:
        pass

    # TODO Rechtschreibfehler behoben: _checkColosion -> _checkCollision
    def _checkCollision(self) -> bool:
        pass

    def _prepareSquad(self):
        pass

    def _restart(self):
        pass
