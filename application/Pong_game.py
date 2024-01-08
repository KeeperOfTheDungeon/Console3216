import random

# #include "game.h"
import Game

# #include "pong_ball.h"
from Pong_ball import Ball
# #include "pong_paddle.h"
from Pong_Paddle import Paddle
# #include "Joystick.h"
import Joystick

import Display
import NumericDisplay
import Sine
import Sound

EVENT_NONE: int = 0
EVENT_PLAYER_LEFT_POINT: int = 1
EVENT_PLAYER_RIGHT_POINT: int = 2
EVENT_BOUNCE_TOP: int = 3
EVENT_BOUNCE_BOTTOM: int = 4
BALL_SPEED_INCREASE_FACTOR: int = 150

# C++ Source had typo: PADLE_SOUND_EFFECT_
PADDLE_SOUND_EFFECT_LEFT: int = 35
PADDLE_SOUND_EFFECT_RIGHT: int = 36


class Pong(Game):
    def __init__(self, leftJoystick: Joystick, rightJoystick: Joystick):
        # TODO Super constructor call
        super().__init__(leftJoystick, rightJoystick, "PONG")

        self._ball: Ball
        self._paddleLeft: Paddle
        self._paddleRight: Paddle

        self._fieldLineColor: int

        self._player1Points: int = 0
        self._player2Points: int = 0

        # TODO Rechtschreibfehler behoben: movePrescaller -> movePrescaler
        self._movePrescaler: int
        self._ballSpeedPrescaler: int

        self._paddleLeft.setPosition(0, Display.DISPLAY_Y_EXTEND / 2)
        self._paddleRight.setPosition(Display.DISPLAY_X_EXTEND - 2, Display.DISPLAY_Y_EXTEND / 2)

        self._paddleLeft.setBounceSoundEffect(PADDLE_SOUND_EFFECT_LEFT)
        self._paddleRight.setBounceSoundEffect(PADDLE_SOUND_EFFECT_RIGHT)

        self._paddleLeft.setOrientation(False)
        self._paddleRight.setOrientation(True)

        self._restart()

        self._fieldLineColor = Display.getColor(0, 7, 0)

        NumericDisplay.NumericDisplay.test()

    def play(self):
        pass

    def draw(self):
        pass

    def prepareDemo(self):
        pass

    def playDemo(self):
        pass

    def prepareGame(self):
        pass

    def playGame(self):
        pass

    def process(self):
        pass

    def _movePlayer(self):
        pass

    def _drawField(self):
        pass

    # TODO C++: void computerMove(Paddle * paddle, bool direction);
    def _computerMove(paddle: Paddle, direction: bool):
        pass

    # TODO Rechtschreibfehler behoben: _checkBoundarys -> _checkBoundaries
    def _checkBoundaries(self) -> int:
        pass

    # TODO Rechtschreibfehler behoben: _checkColision -> _checkCollision
    def _checkCollision(self) -> bool:
        pass

    def _restart(self):
        angle: int = random.randrange(16)
        vectorX: int = Sine.Sine.getSineValue(angle)
        vectorY: int = Sine.Sine.getCosineValue(angle)

        # TODO C++ Source was Switch/case
        randomNr = random.randrange(3)
        if randomNr == 1:
            vectorX = - vectorX
        elif randomNr == 2:
            vectorY = - vectorY
        elif randomNr == 3:
            vectorX = - vectorX
            vectorY = - vectorY
        
        vectorX >>= 3
        vectorY >>= 3

        self._ball.setPosition(Display.DISPLAY_X_EXTEND / 2, Display.DISPLAY_Y_EXTEND / 2)
        self._ball.setVector(vectorX, vectorY)
        self._ball.setSpeed(10)

        NumericDisplay.NumericDisplay.displayValue(NumericDisplay.DISPLAY_LEFT, self._player1Points)
        NumericDisplay.NumericDisplay.displayValue(NumericDisplay.DISPLAY_RIGHT, self._player2Points)

        self._ballSpeedPrescaler = 0
        pass
