# #include "game.h"
import Game
# #include "Joystick.h"
import Joystick
# #include "CurveFeverLogic.h"
from CurveFeverLogic import Logic, GameStatus
# #include "CurveFeverView.h"
import CurveFeverView

class Curve(Game):
    # TODO C++ Konstruktor: Curve(Joystick & leftJoystick, Joystick & rightJoystick);
    def __init__(self, leftJoystick: Joystick, rightJoystick: Joystick):
        # TODO C++: GameStatus* gameStatus;
        self.__gameStatus: GameStatus
        self.__logic: Logic
        self.__view: CurveFeverView

    def prepareDemo(self):
        pass

    def playDemo(self):
        pass

    def prepareGame(self):
        pass

    def playGame(self):
        pass

    def gameOver(self):
        pass

    def process(self):
        pass
