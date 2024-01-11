from enum import Enum

# #include "inc/TetrisPlayer.h"
import TetrisPlayer

import Display

class TetrisLogicStatus(Enum):
    UPDATING = 0
    ENDSCREEN = 1
    ENDGAME = 2


class TetrisLogic:
    def __init__(self):
        self.__status: TetrisLogicStatus

        # TODO C++: TetrisPlayer* playerLeft;
        self.playerLeft: TetrisPlayer.TetrisPlayer
        # TODO C++: TetrisPlayer* playerRight;
        self.playerRight: TetrisPlayer.TetrisPlayer

        self.initializeGame()

    def __handleStatus(self, player: TetrisPlayer.TetrisPlayer):
        # TODO C++ Source was Switch/case
        if player.getStatus() == TetrisPlayer.TetrisPlayerStatus.PLAYING:
            pass
        elif player.getStatus() == TetrisPlayer.TetrisPlayerStatus.LOST:
            self.__status = TetrisLogicStatus.ENDSCREEN
        pass

    def __drawBorders(self):
        for y in range(16):
            Display.Display.drawPixel(10, y, Display.Display.getColor(2, 0, 0))
            Display.Display.drawPixel(21, y, Display.Display.getColor(2, 0, 0))
        pass

    def update(self, delta: int):
        pass

    def startButtonPressed(self):
        pass

    def isGameEnd(self) -> bool:
        pass

    def isEndScreen(self) -> bool:
        pass

    def initializeGame(self):
        pass

    def resetGame(self):
        pass
