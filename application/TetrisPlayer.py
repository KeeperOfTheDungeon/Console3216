from enum import Enum

# #include "Arduino.h"
# #include "game.h"
import Game
# #include "inc/TetrisTetrom.h"
import TetrisTetrom


class TetrisPlayerStatus(Enum):
    PLAYING = 0
    LOST = 1


class TetrisPlayer:
    def __init__(self, offsetX: int, offsetY: int):
        self.__temporaryCounter: int

        self.__status: TetrisPlayerStatus
        # TODO C++: TetrisTetrom* currentTetrom;
        self.__currentTetrom: TetrisTetrom
        # TODO C++: TetrisTetrom* nextTetrom;
        self.__nextTetrom: TetrisTetrom
        self.__deltaSum: int
        self.__updateDelay: int
        self.__mapColor: int
        self.__mapOffsetX: int
        self.__mapOffsetY: int
        self.__softDropDelay: int = 50
        self.__normalDelay: int = 200

        # TODO C++: uint8_t map[16][10] = {...};
        self.__map: int = [[0] * 10] * 16

        self.playerpoints: int

    def __canMoveTetrom(self, tetrom: TetrisTetrom, xOffset: int, yOffset: int) -> bool:
        pass

    def __canRotateTetrom(self, tetrom: TetrisTetrom, clockwise: bool) -> bool:
        pass

    def __initializeTetroms(self):
        pass

    def __assignNextTetroms(self):
        pass

    def __generateTetrom(self) -> TetrisTetrom:
        pass

    def __logicalUpdate(self, delta: int):
        pass

    def __hasCollisions(self, tetrom: TetrisTetrom) -> bool:
        pass

    def __mapEmpty(self, x: int, y: int) -> bool:
        pass

    def __placeOnMap(self, tetrom: TetrisTetrom):
        pass

    def __changeMap(self, x: int, y: int, value: int):
        pass

    def __moveIfPossible(self, tetrom: TetrisTetrom, xOffset: int, yOffset: int):
        pass

    def __rotateIfPossible(self, tetrom: TetrisTetrom, clockwise: bool):
        pass

    def returnPlayerPoints(self) -> int:
        pass

    def displayPlayerPoints(self, b: bool):
        pass

    def init(self):
        pass

    def reset(self):
        pass

    def getStatus(self) -> TetrisPlayerStatus:
        pass

    def draw(self):
        pass

    def drawNextTetroms(self, offsetX: int, offsetY: int):
        pass

    def update(self, delta: int):
        pass

    def getCurrentTetrom(self) -> TetrisTetrom:
        pass

    def getNextTetrom(self) -> TetrisTetrom:
        pass

    def softDropOn(self):
        pass

    def softDropOff(self):
        pass

    def inputRotateClockwise(self):
        pass

    def inputRotateCounterClockwise(self):
        pass

    def inputMoveLeft(self):
        pass

    def inputMoveRight(self):
        pass

    def checkLine(self, y: int) -> bool:
        pass

    def removeLine(self, y: int):
        pass
