from enum import Enum
import random

# #include "Arduino.h"
# #include "game.h"
import Game
# #include "inc/TetrisTetrom.h"
import TetrisTetrom

import Display

class TetrisPlayerStatus(Enum):
    PLAYING = 0
    LOST = 1


class TetrisPlayer:
    def __init__(self, offsetX: int, offsetY: int):
        self.__temporaryCounter: int

        self.__status: TetrisPlayerStatus
        # TODO C++: TetrisTetrom* currentTetrom;
        self.__currentTetrom: TetrisTetrom.TetrisTetrom
        # TODO C++: TetrisTetrom* nextTetrom;
        self.__nextTetrom: TetrisTetrom.TetrisTetrom
        self.__deltaSum: int
        self.__updateDelay: int
        self.__mapColor: int
        self.__mapOffsetX: int = offsetX
        self.__mapOffsetY: int = offsetY
        self.__softDropDelay: int = 50
        self.__normalDelay: int = 200

        # TODO C++: uint8_t map[16][10] = {...};
        self.__map: int = [[0 for _ in range(10)] for _ in range(16)]

        self.playerpoints: int

        self.init()

    def __canMoveTetrom(self, tetrom: TetrisTetrom.TetrisTetrom, xOffset: int, yOffset: int) -> bool:
        pass

    def __canRotateTetrom(self, tetrom: TetrisTetrom.TetrisTetrom, clockwise: bool) -> bool:
        if clockwise:
            tetrom.rotateRight()
        else:
            tetrom.rotateLeft()
        
        collides: bool = self.__hasCollisions(tetrom)

        if clockwise:
            tetrom.rotateLeft()
        else:
            tetrom.rotateRight()
        return not collides

    def __initializeTetroms(self):
        self.__currentTetrom = self.__generateTetrom()
        self.__nextTetrom = self.__generateTetrom()
        pass

    def __assignNextTetroms(self):
        del self.__currentTetrom
        self.__currentTetrom = self.__nextTetrom
        self.__nextTetrom = self.__generateTetrom()
        pass

    def __generateTetrom(self) -> TetrisTetrom.TetrisTetrom:
        tetrom = TetrisTetrom.TetrisTetrom(self.__mapOffsetX, self.__mapOffsetY)
        tetrom.setType(random.randrange(0, 7)) # Random type
        tetrom.setPosition(5, -5) # Top center?
        rColor: int = Display.Display.getColor(random.randrange(0, 3), random.randrange(0, 3), random.randrange(0, 3))
        # TODO C++ Source overrides previous line
        rColor = Display.Display.getColor(2, 2, 3)
        tetrom.setColor(rColor)
        return tetrom

    def __logicalUpdate(self, delta: int):
        pass

    def __hasCollisions(self, tetrom: TetrisTetrom.TetrisTetrom) -> bool:
        pass

    def __mapEmpty(self, x: int, y: int) -> bool:
        pass

    def __placeOnMap(self, tetrom: TetrisTetrom.TetrisTetrom):
        pass

    def __changeMap(self, x: int, y: int, value: int):
        pass

    def __moveIfPossible(self, tetrom: TetrisTetrom.TetrisTetrom, xOffset: int, yOffset: int):
        pass

    def __rotateIfPossible(self, tetrom: TetrisTetrom.TetrisTetrom, clockwise: bool):
        pass

    def returnPlayerPoints(self) -> int:
        pass

    def displayPlayerPoints(self, b: bool):
        pass

    def init(self):
        self.playerpoints = 0
        self.__status = TetrisPlayerStatus.PLAYING
        self.__mapColor = Display.Display.getColor(2, 0, 2)
        self.__temporaryCounter = 0
        self.__deltaSum = 0
        self.__updateDelay = self.__normalDelay

        self.__initializeTetroms()
        pass

    def reset(self):
        self.init()

        for x in range(10):
            for y in range(y):
                self.__changeMap(x, y, 0)
        pass

    def getStatus(self) -> TetrisPlayerStatus:
        pass

    def draw(self):
        pass

    def drawNextTetroms(self, offsetX: int, offsetY: int):
        pass

    def update(self, delta: int):
        pass

    def getCurrentTetrom(self) -> TetrisTetrom.TetrisTetrom:
        return self.__currentTetrom

    def getNextTetrom(self) -> TetrisTetrom.TetrisTetrom:
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
