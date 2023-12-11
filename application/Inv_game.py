# #include "game.h"
import Game
# #include "inv_pilot.h"
import Inv_pilot
# #include "inv_ufo.h"
import Inv_ufo
# #include "inv_projectile.h"
import Inv_projectile
# #include "inv_alien.h"
import Inv_alien
# #include "inv_squad.h"
import Inv_squad
# #include "Joystick.h"
import Joystick

PADLE_SOUND_EFFECT_LEFT = 35
PADLE_SOUND_EFFECT_RIGHT = 36

PILOT_DEFAULT_X_POSITION = 16
PILOT_DEFAULT_Y_POSITION = 15

POINTS_UFO = 100
UFO_APERANCE_PROPABILITY = 50


class Invaders(Game):
    def __init__(self, leftJoystick: Joystick, rightJoystick: Joystick):
        # TODO Super constructor call
        super().__init__(leftJoystick, rightJoystick, "INV")

        self._pilot: Inv_pilot.Pilot
        
        self._pilotProjectile: Inv_projectile.Projectile
        self._invadersProjectile: Inv_projectile.Projectile

        self._ufo: Inv_ufo.Ufo
        self._squad: Inv_squad.Squad

        self._player1Points: int

        # TODO C++: uint8_t movePrescaller;
        # TODO Rechtschreibfehler behoben: _movePrescaller -> _movePrescaler
        self._movePrescaler: int
        self._active: bool

        # TODO Perhaps leftJoystick needs to be instance variable
        self._pilot.init(leftJoystick)
        self._restart()

        self._pilotProjectile.setDirection(False)
        self._invadersProjectile.setDirection(True)

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
        self._pilot.setPosition(PILOT_DEFAULT_X_POSITION, PILOT_DEFAULT_Y_POSITION)
        self._pilotProjectile.deActivate()
        self._invadersProjectile.deActivate()

        self._squad.prepareSquad()

        self._player1Points = 0
        # TODO Game method
        self._timeStart()
        pass
