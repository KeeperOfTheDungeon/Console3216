# #include "game.h"
import Game
# #include "Joystick.h"
import Joystick
# #include "sw_constants.h"
import SW_Constants
# #include <display.h>
import Display
# #include <sine.h>
import Sine
# #include "sw_ship.h"
from SW_Ship import Ship
# #include "sw_projectileManagement.h"
from SW_ProjectileManagement import ProjectileManagement
# #include "SpaceSounds.h"
import SpaceSounds

import NumericDisplay

class Space_Wars(Game):
    def __init__(self, leftJoystick: Joystick, rightJoystick: Joystick):
        # TODO Super constructor call
        super().__init__(leftJoystick, rightJoystick, "SWAR")
        # TODO
        self._textColor: int = Display.getColor(0, 2, 5)
        self._middleBorderColor: int = 0xFFFF

        self._currentState: int = SW_Constants.STATE_DEMO

        self._gameFinish: bool = False

        self._sounds: SpaceSounds

        self._projectileManagement: ProjectileManagement

        self._shipLeft: Ship
        self._shipRight: Ship

        self._restart()

        NumericDisplay.NumericDisplay.test()

        self._timeStart()

        # Comment from C++ source:
        # Here you have to initialize important variables for your ships
        self._shipLeft.setShipColor(0xFFFF)
        self._shipLeft.setOrientation(SW_Constants.SHIP_LEFT)
        self._shipLeft.setBitMap()

        self._shipRight.setShipColor(0xFFFF)
        self._shipRight.setOrientation(SW_Constants.SHIP_RIGHT)
        self._shipRight.setBitMap()

    def play(self):
        pass

    def draw(self, STATE: int):
        pass

    def prepareDemo(self):
        self._shipLeft.setShipLives(3)
        self._shipRight.setShipLives(3)
        self._currentState = SW_Constants.STATE_PLAY

        self._player1Type = Game.PLAYER_TYPE_HUMAN
        self._player2Type = Game.PLAYER_TYPE_HUMAN

        self._gameFinish = False
        pass

    def playDemo(self):
        self._shipLeft.setShipLives(3)
        self._shipRight.setShipLives(3)
        self._currentState = SW_Constants.STATE_PLAY
        self._gameFinish = False

        self.demo()

        self.draw(SW_Constants.STATE_DEMO)
        self._currentState = SW_Constants.STATE_PLAY
        pass

    def playGame(self):
        self.play()
        self.draw(self._currentState)
        pass

    def process(self):
        super().process()
        NumericDisplay.NumericDisplay.displayValue(NumericDisplay.DISPLAY_LEFT, self._shipLeft.getShipLives())
        NumericDisplay.NumericDisplay.displayValue(NumericDisplay.DISPLAY_RIGHT, self._shipRight.getShipLives())
        # Abfrage auf Spielende
        if (self._shipLeft.getShipLives() == 0) or (self._shipRight.getShipLives() == 0):
            self._currentState = SW_Constants.STATE_SHOW_WINNER
        
        if self._gameFinish and (self._joystickLeft.isButtonTop() or
                                 self._joystickLeft.isButtonBody() or
                                 self._joystickRight.isButtonTop() or
                                 self._joystickRight.isButtonBody()):
            self._state = SW_Constants.GAME_STATE_END
        pass

    def demo(self):
        pass

    def playSoundShot(self):
        pass

    def playSoundCollision(self):
        pass

    def _drawField(self):
        pass

    def _drawMiddleBorder(self):
        pass

    def _restart(self):
        self._shipLeft.setShipLives(3)
        self._shipRight.setShipLives(3)
        self._timeStart()
        pass

    def _callTestMethod(self):
        pass
