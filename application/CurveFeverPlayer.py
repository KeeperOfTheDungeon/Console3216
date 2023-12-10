RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

SLOW = 4
REGULAR = 2
FAST = 1

MAX_BOOST = 100
MIN_GAP_DURATION = 2
MAX_GAP_DURATION = 4
MIN_TAIL_DURATION = 4
MAX_TAIL_DURATION = 8

NO_ITEM = 0
ITEM_SLOW = 1
ITEM_WALL = 2
ITEM_CLEAR = 3
ITEM_DURATION = 20


# TODO C++: typedef uint8_t Item;
class Item:
    pass


# TODO C++: typedef struct {...} Position;
class Position:
    def __init__(self):
        self.x: int
        self.y: int


class Player:
    # C++: static uint8_t width;
    width: int
    # C++: static uint8_t height;
    height: int

    def __init__(self):
        self.__name: int
        self.__speed: int = REGULAR
        self.__item: Item = NO_ITEM
        self.__itemActive: bool
        self.__itemDuration: int = ITEM_DURATION
        self.__position: Position
        self.__boost: int = MAX_BOOST
        self.__direction: int = UP
        self.__creatingGap: bool = True
        self.__gapDuration: int = 0

    def __movePlayer(self) -> bool:
        pass

    @classmethod
    def setBounds(cls, width: int, height: int):
        pass

    def setName(self, name: int):
        pass

    def getName(self) -> int:
        pass

    def setPosition(self, x: int, y: int):
        pass

    def getPosition(self) -> Position:
        pass

    def setDirection(self, direction: int):
        pass

    def getDirection(self) -> int:
        pass

    def setItem(self, item: Item):
        pass

    def getItem(self) -> Item:
        pass
