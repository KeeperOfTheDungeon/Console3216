# #include "game.h"
import Game

# #include "pong_ball.h"
from Pong_ball import Ball
# #include "pong_paddle.h"
from Pong_Paddle import Paddle
# #include "Joystick.h"
import Joystick


EVENT_NONE: int = 0
EVENT_PLAYER_LEFT_POINT: int = 1
EVENT_PLAYER_RIGHT_POINT: int = 2
EVENT_BOUNCE_TOP: int = 3
EVENT_BOUNCE_BOTTOM: int = 4
BALL_SPEED_INCREASE_FACTOR: int = 150


class Pong(Game):
    def __init__(self, leftJoystick: Joystick, rightJoystick: Joystick):
        self._ball: Ball
        self._paddleLeft: Paddle
        self._paddleRight: Paddle

        self._fieldLineColor: int

        self._player1Points: int
        self._player2Points: int

        # TODO Rechtschreibfehler behoben: movePrescaller -> movePrescaler
        self._movePrescaler: int
        self._ballSpeedPrescaler: int

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
        pass
