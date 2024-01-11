import time
import psutil
import os

# #include "game.h"
import Game
# #include "Joystick.h"
import Joystick
# #include "inc/TetrisDemo.h"
import TetrisDemo
# #include "inc/TetrisLogic.h"
import TetrisLogic


class TetrisGame(Game):
    def __init__(self, leftJoystick: Joystick, rightJoystick: Joystick):
        # TODO Super constructor call
        super().__init__(leftJoystick, rightJoystick, "TTRS")

        # TODO C++: TetrisDemo* tetrisDemo;
        self.__tetrisDemo: TetrisDemo
        # TODO C++: TetrisLogic* tetrisLogic;
        self.__tetrisLogic: TetrisLogic
        # TODO C++: TetrisPlayer* playerLeft;
        self.__playerLeft: TetrisLogic.TetrisPlayer
        # TODO C++: TetrisPlayer* playerRight;
        self.__playerRight: TetrisLogic.TetrisPlayer

        self.__statusLeftJoystickOld: self.__JoystickStatus
        self.__statusRightJoystickOld: self.__JoystickStatus

        self.__lastTime: int = 0

        self.__repeatLeftRightTime: int = 100

        self.__joystickLeftRepeatLeft: int = 0
        self.__joystickLeftRepeatRight: int = 0

        self.__joystickRightRepeatLeft: int = 0
        self.__joystickRightRepeatRight: int = 0

        # TODO pyserial
        # Serial.println("Tetris Game Konstruktor!")

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
        # TODO pyserial
        # Serial.println("Tetris Game prepare Demo!")
        self.__tetrisDemo = TetrisDemo()
        self.__lastTime = self.millis()
        pass

    def playDemo(self):
        pass

    def prepareGame(self):
        pass

    def playGame(self):
        pass

    def updateStatus(self):
        pass

    # TODO Replacement for Arduinos millis() function
    """
    /**
    * Original Arduino function returns the process uptime.
    * This function can return Process uptime or System uptime.
    *
    * Method 1: Calculates the process uptime.
    * Grabs current process.
    * Grabs current time in unix timestamp format.
    * Subtracts unix timestamp of process creation time.
    * Returns result in milliseconds.
    *
    * Method 2: Calculates the system uptime.
    *
    * Grabs current time in unix timestamp format.
    * Subtracts unix timestamp of boot time.
    * Returns result in milliseconds.
    */
    """
    def millis(self) -> int:
        p = psutil.Process(os.getpid())
        return int(time.time() - p.create_time())
        # return int(time.time() - psutil.boot_time())
