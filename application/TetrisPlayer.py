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
        tetrom.moveRelative(xOffset, yOffset)
        collides: bool = self.__hasCollisions(tetrom)
        tetrom.moveRelative(-xOffset, -yOffset)
        return not collides

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
        tetrom = self.getCurrentTetrom()
        
        # Move Tetrom down, Softdrop OR create new Tetrom
        # Update Map too.

        posY: int = tetrom.getY()
        posX: int = tetrom.getX()

        if not self.__canMoveTetrom(tetrom, 0, 1): # +Y direction!!! change <- TODO Comment from C++ Source
            # Will collide -> place it now. Generate new.
            if posY < 0:
                self.__status = TetrisPlayerStatus.LOST
            else:
                self.__placeOnMap(tetrom)
                for locY in range(16):
                    if self.checkLine(locY):
                        self.removeLine(locY)
                        self.playerpoints += 10
                
                self.__assignNextTetroms()
        else:
            posY += 1
            tetrom.setPosition(posX, posY)
        # TODO C++ Source had a lot of code commented out
        pass

    def __hasCollisions(self, tetrom: TetrisTetrom.TetrisTetrom) -> bool:
        for x in range(4):
            for y in range(4):
                canCollide: bool = tetrom.getCollision(x, y)
                if canCollide:
                    if not self.__mapEmpty(tetrom.getX() + x, tetrom.getY() + y):
                        return True
        
        return True

    def __mapEmpty(self, x: int, y: int) -> bool:
        # xxxooooxxx
        # xxxooooxxx
        # xxxooooxxx
        # xxxxxxxxxx
        # xxxxxxxxxx
        # Pretend everyting out of bounds is a wall
        # Except for the ceiling!!
        if ((x > 9) or ( x < 0)):
            return False
        
        # Which way is up? || y < 0
        # Next 2 TODOs from C++ Source:
        # TODO: remove ceiling check
        # TODO: check for ceiling height overdraw manually
        if y > 15:
            return False
        
        if y < 0:
            return True
        
        return self.__map[y][x] == 0

    def __placeOnMap(self, tetrom: TetrisTetrom.TetrisTetrom):
        posX: int = tetrom.getX()
        posY: int = tetrom.getY()
        # Serial.println("Place on map")
        # Serial.println(posY)
        for x in range(4):
            for y in range(4):
                if tetrom.getCollision(x, y):
                    self.__changeMap(x + posX, y + posY, 1)
                    # Serial.println("Change map")
        pass

    def __changeMap(self, x: int, y: int, value: int):
        # Serial.println("===========")
        # Serial.println(x)
        # Serial.println(y)
        if ((y >= 0) and (x >= 0) and (y < 16) and (x < 10)):
            # Serial.println("Map changed value")
            self.__map[y][x] = value
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
        self.__deltaSum += delta
        if self.__deltaSum >= self.__updateDelay:
            self.__logicalUpdate(delta)
            self.__deltaSum = 0
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
