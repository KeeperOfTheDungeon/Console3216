# #include "CurveFeverPlayer.h"
from CurveFeverPlayer import Item, Player, Position
# #include "Joystick.h"
import Joystick

FIELD_HEIGHT = 16
FIELD_WIDTH = 32
FIELD_SIZE = 4 * FIELD_HEIGHT * FIELD_WIDTH / 8
MAX_CHANGE_COUNT = 5

PLAYER_1 = 0
PLAYER_2 = 1
DRAW = 2

NO_SOUND = 0
SOUND_BACKGROUND = 1
SOUND_ITEM_COLLECT = 2
SOUND_ITEM_ACTIVATE = 3
SOUND_GAMEOVER = 4

STATE_EMPTY = 0
STATE_PLAYER_1 = 1
STATE_PLAYER_2 = 2
STATE_ITEM_SLOW = 3
STATE_ITEM_WALL = 4
STATE_ITEM_CLEAR = 5
STATE_TAIL_1 = 6
STATE_TAIL_2 = 7

PROBABILITY_ITEM_SLOW = 16
PROBABILITY_ITEM_WALL = 8
PROBABILITY_ITEM_CLEAR = 4

STATE_ITEM_1 = 3
STATE_ITEM_2 = 4
STATE_ITEM_3 = 5


# TODO C++: typedef struct {...} CellUpdate;
class CellUpdate:
    def __init__(self):
        self.x: int
        self.y: int
        self.state: int


# TODO C++: typedef struct {...} GameStatus;
class GameStatus:
    def __init__(self):
        self.gameOver: bool
        self.clearScreen: bool
        self.cellUpdates: CellUpdate  # TODO C++: CellUpdate* cellUpdates;
        self.updateCount: int
        self.soundStatus: int
        self.player1Boost: int
        self.player2Boost: int


class Logic:

    def __init__(self):
        # TODO C++: Joystick* joystick1;
        self.__joystick1: Joystick
        # TODO C++: Joystick* joystick2;
        self.__joystick2: Joystick
        # TODO C++: CellUpdate cellUpdates[MAX_CHANGE_COUNT];
        self.__cellUpdates: CellUpdate = [] * MAX_CHANGE_COUNT

        self.__status: GameStatus
        self.__player1: Player
        self.__player2: Player
        self.__winner: int
        self.__currentItem: Item
        self.__itemPosition: Position
        self.__gameTicks: int

        # TODO C++: uint8_t field[FIELD_WIDTH][FIELD_HEIGHT];
        self.__field: int = [[] * FIELD_WIDTH] * FIELD_HEIGHT

    def __generateItem(self) -> int:
        pass

    def __getCellState(self, x: int, y: int) -> int:
        pass

    def __setCellState(self, x: int, y: int, state: int, publish: bool=False):
        pass
    
    def __clearField(self):
        pass

    def __setDirectionForPlayer(self, player: Player):
        pass

    def __updateOccursThisTick(self, speed: int) -> bool:
        pass

    def __updateCell(self, player: Player, head: bool):
        pass

    def __setWinnerAfterValidMove(self, player1Updated: bool, player2Updated: bool):
        pass

    def __maybeGenerateItem(self):
        pass

    def __updatePlayer(self, player: Player, joystick: Joystick) -> bool:
        pass

    def __maybeAbsorbItem(self):
        pass

    def __havePlayersCollided(self, pos1: Position, pos2: Position, dir1: int, dir2: int) -> bool:
        pass

    # TODO C++ return Pointer
    def initGame(self, p1_joystick: Joystick, p2_joystick: Joystick) -> GameStatus:
        self.__joystick1 = p1_joystick
        self.__joystick2 = p2_joystick
        self.__gameTicks = 0
        self.__currentItem = 0
        self.__itemPosition.x = 0
        self.__itemPosition.y = 0
        self.__winner = DRAW

        Player.setBounds(FIELD_WIDTH, FIELD_HEIGHT)

        self.__player1.setName(PLAYER_1)
        self.__player2.setName(PLAYER_2)

        self.__player1.reset()
        self.__player1.setPosition(1, FIELD_HEIGHT / 2)
        self.__player1.setDirection(RIGHT)

        self.__player2.reset()
        self.__player2.setPosition(FIELD_WIDTH - 1, FIELD_HEIGHT / 2)
        self.__player2.setDirection(LEFT)

        self.__status.gameOver = False
        self.__status.clearScreen = True
        self.__status.cellUpdates = self.__cellUpdates;
        self.__status.updateCount = 0
        self.__status.soundStatus = 0
        self.__status.player1Boost = self.__player1.getBoost()
        self.__status.player2Boost = self.__player2.getBoost()

        self.__clearField()
        # TODO return value is an address in C++
        return self.__status

    # TODO C++ return Pointer
    def move(self):
        if not self.__status.gameOver:
            self.__status.updateCount = 0
            self.__status.clearScreen = False

            self.__status.soundStatus = NO_SOUND
            player1Updated: bool = self.__updatePlayer(self.__player1, self.__joystick1)
            player2Updated: bool = self.__updatePlayer(self.__player2, self.__joystick2)

            self.__status.player1Boost = self.__player1.getBoost()
            self.__status.player2Boost = self.__player2.getBoost()

            # Has there been an update?
            if (player1Updated or player2Updated) and not self.__status.gameOver:
                self.__maybeAbsorbItem()

                if not self.__status.clearScreen:
                    self.__setWinnerAfterValidMove(player1Updated, player2Updated)

                    if player1Updated:
                        self.__updateCell(self.__player1, True)
                    
                    if player2Updated:
                        self.__updateCell(self.__player2, True)

            self.__gameTicks += 1
        
        # TODO return value is an address in C++
        return self.__status

    def getWinner(self) -> int:
        return self.__winner
