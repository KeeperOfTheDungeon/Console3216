from enum import Enum

# #include "inc/TetrisPlayer.h"
from TetrisPlayer import TetrisPlayer


class TetrisLogicStatus(Enum):
    UPDATING = 0
    ENDSCREEN = 1
    ENDGAME = 2


class TetrisLogic:
    def __init__(self):
        self.__status: TetrisLogicStatus

        # TODO C++: TetrisPlayer* playerLeft;
        self.playerLeft: TetrisPlayer
        # TODO C++: TetrisPlayer* playerRight;
        self.playerRight: TetrisPlayer

    def __handleStatus(self, player: TetrisPlayer):
        pass

    def __drawBorders(self):
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
