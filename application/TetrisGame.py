# #include "game.h"
import Game
# #include "Joystick.h"
import Joystick
# #include "inc/TetrisDemo.h"
from TetrisDemo import TetrisDemo
# #include "inc/TetrisLogic.h"
from TetrisLogic import TetrisLogic, TetrisPlayer


class TetrisGame(Game):
    def __init__(self, leftJoystick: Joystick, rightJoystick: Joystick):
        # TODO C++: TetrisDemo* tetrisDemo;
        self.__tetrisDemo: TetrisDemo
        # TODO C++: TetrisLogic* tetrisLogic;
        self.__tetrisLogic: TetrisLogic
        # TODO C++: TetrisPlayer* playerLeft;
        self.__playerLeft: TetrisPlayer
        # TODO C++: TetrisPlayer* playerRight;
        self.__playerRight: TetrisPlayer

        self.__statusLeftJoystickOld: JoystickStatus
        self.__statusRightJoystickOld: JoystickStatus

        self.__lastTime: int = 0

        self.__repeatLeftRightTime: int = 100

        self.__joystickLeftRepeatLeft: int = 0
        self.__joystickLeftRepeatRight: int = 0

        self.__joystickRightRepeatLeft: int = 0
        self.__joystickRightRepeatRight: int = 0

    # TODO C++: struct JoystickStatus {...};
    class __JoystickStatus:
        def __init__(self):
            self.left: bool = False
            self.right: bool = False
            self.down: bool = False
            self.up: bool = False

            self.buttonTop: bool = False
            self.buttonBody: bool = False

    def prepareDemo(self):
        pass

    def playDemo(self):
        pass

    def prepareGame(self):
        pass

    def playGame(self):
        pass

    def updateStatus(self):
        pass
