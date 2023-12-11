import random

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

import NumericDisplay

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
        action: int = self._pilot.checkActions()

        if not self._pilotProjectile.isActive():
            # TODO C++ source was switch/case
            # TODO combined elif into or case
            if action == Inv_pilot.PILOT_TRIGGER_UP or action == Inv_pilot.PILOT_TRIGGER_BODY:
                self._pilotProjectile.activate()
                self._pilotProjectile.setPosition(self._pilot.getXPos(), self._pilot.getYPos())
            # elif action == Inv_pilot.PILOT_TRIGGER_BODY:
            #     self._pilotProjectile.activate()
            #     self._pilotProjectile.setPosition(self._pilot.getXPos(), self._pilot.getYPos())

        self._ufo.move()
        self._pilotProjectile.move()

        # UFO
        if (self._pilotProjectile.getYPos() == 0) and (self._pilotProjectile.isActive()):
            if self._ufo.checkCollision(self._pilotProjectile.getXPos()):
                self._ufo.deActivate()
                self._ufo.explode()
                self._player1Points += POINTS_UFO
                # TODO Serial not implemented
                # Serial.println("hit !");
        
        if not self._ufo.isActive():
            if random.randrange(UFO_APERANCE_PROPABILITY) == 5:
                self._ufo.setPosition(0, 0)
                self._ufo.activate()
        
        # Aliens
        points: int
        if self._pilotProjectile.isActive():
            points = self._squad.checkColision(self._pilotProjectile.getXPos(), self._pilotProjectile.getYPos())
            if points != 0:
                self._player1Points += points
                self._pilotProjectile.deActivate()
        self._squad.move()

        NumericDisplay.displayValue(NumericDisplay.DISPLAY_LEFT, self._player1Points)
        pass

    def draw(self):
        pass

    def prepareDemo(self):
        self._player1Type = Game.PLAYER_TYPE_AI_0
        self._player1Type = Game.PLAYER_TYPE_AI_0
        pass

    def playDemo(self):
        self.play()
        self.draw()
        pass

    def playGame(self):
        pass

    def process(self):
        # TODO C++ source:
        # Game::process();
        # process is not a static (class) method
        super().process()
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
