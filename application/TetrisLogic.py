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
        Display.Display.clearDisplay()

        # TODO C++ Source was Switch/case
        if self.__status == TetrisLogicStatus.UPDATING:
            self.__handleStatus(self.playerLeft)
            self.__handleStatus(self.playerRight)

            # Serial.println("UPDATING")
            self.playerLeft.update(delta)
            self.playerRight.update(delta)
            self.playerLeft.displayPlayerPoints(True)
            self.playerRight.displayPlayerPoints(False)

            self.__drawBorders()
            self.playerLeft.drawNextTetroms(12, 2)
            self.playerRight.drawNextTetroms(17, 2)

            self.playerLeft.draw()
            self.playerRight.draw()
        elif self.__status == TetrisLogicStatus.ENDSCREEN:
            # Serial.println("ENDSCREEN")
            self.__drawBorders()
            self.playerLeft.draw()
            self.playerRight.draw()
        elif self.__status == TetrisLogicStatus.ENDGAME:
            # TODO C++ Source lines were commented out
            # Serial.println("ENDGAME");
            # self.resetGame();
            pass

        Display.Display.refresh()
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
