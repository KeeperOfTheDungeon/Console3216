# #include "Arduino.h"
# #include "CurveFeverLogic.h"
from CurveFeverLogic import CellUpdate

# TODO C++ includes:
# #include "inc/CurveFeverView.h"
# #include "inc/CurveFeverLogic.h"
# #include "display.h"
# #include "numericDisplay.h"
# #include "Sound.h"

# TODO C++: #define EMPTY_COLOR Display::getColor(0, 0, 0);
EMPTY_COLOR: int = Display.getColor(0, 0, 0) # Display::getColor(0, 0, 0);
PLAYER_1_COLOR_1: int = Display.getColor(7, 0, 0) # Display::getColor(7, 0, 0);
PLAYER_1_COLOR_2: int = Display.getColor(4, 0, 0) # Display::getColor(4, 0, 0);
PLAYER_2_COLOR_1: int = Display.getColor(0, 7, 0) # Display::getColor(0, 7, 0);
PLAYER_2_COLOR_2: int = Display.getColor(0, 4, 0) # Display::getColor(0, 4, 0);
ITEM_1_COLOR: int = Display.getColor(0, 0, 7) # Display::getColor(0, 0, 7);
ITEM_2_COLOR: int = Display.getColor(0, 2, 2) # Display::getColor(0, 2, 2);
ITEM_3_COLOR: int = Display.getColor(3, 3, 3) # Display::getColor(3, 3, 3);


class CurveFeverView:
    def __getColorOfState(state: int) -> int:
        color: int = EMPTY_COLOR
        # TODO C++ source was switch/case
        # TODO C++ source never used PLAYER_1_COLOR_2, assuming bug
        if state == STATE_PLAYER_1:
            color = PLAYER_1_COLOR_1
        elif state == STATE_PLAYER_2:
            color = PLAYER_2_COLOR_1 # TODO C++ source used PLAYER_2_COLOR_2
        elif state == STATE_ITEM_SLOW:
            color = ITEM_1_COLOR
        elif state == STATE_ITEM_WALL:
            color = ITEM_2_COLOR
        elif state == STATE_ITEM_CLEAR:
            color = ITEM_3_COLOR
        elif state == STATE_TAIL_1:
            color = PLAYER_1_COLOR_2 # TODO C++ source used PLAYER_1_COLOR_1
        elif state == STATE_TAIL_2:
            color = PLAYER_2_COLOR_2 # TODO C++ source used PLAYER_2_COLOR_1
        
        return color

    # TODO C++: void printGameName(char *name);
    def printGameName(self, name: int):
        nameColor: int = Display.getColor(2, 0, 2)
        Display.drawTest(name, 4, 4, nameColor, 1)
        Display.refresh()
        Display.drawText(name, 4, 4, nameColor, 1)
        pass

    # TODO C++: void updatePixels(CellUpdate* cells, uint8_t cellCount);
    def updatePixels(self, cells: CellUpdate, cellCount: int):
        for j in range(2):
            for i in range(cellCount):
                Display.drawPixel(cells[i].x, cells[i].y, self.__getColorOfState(cells[i].state))

            if j == 0:
                Display.refresh()
        pass

    def clearScreen(self):
        Display.clearDisplay()
        Display.refresh()
        Display.clearDisplay()
        pass

    def setBoost(self, player: int, boost: int):
        display: int = DISPLAY_LEFT
        if player == PLAYER_2:
            display = DISPLAY_RIGHT
        
        NumericDisplay.displayValue(display, boost)
        pass

    def setTime(self, time: int):
        NumericDisplay.displayTime(DISPLAY_MIDDLE, time)
        pass

    def printWinner(self, winner: int):
        value: int = 0
        # TODO C++ source: char* output = "Draw!";
        output: str = "Draw!"

        if winner == PLAYER_1:
            value = 60 * 11 + 11
            output = "P1 Wins!"
        elif winner == PLAYER_2:
            value = 60 * 22 + 22
            output = "P2 Wins!" # C++ Source: output = "P1 Wins!";
        
        NumericDisplay.displayTime(DISPLAY_LEFT, value)
        NumericDisplay.displayTime(DISPLAY_MIDDLE, value)
        NumericDisplay.displayTime(DISPLAY_RIGHT, value)
        Display.drawText(output, 1, 1, PLAYER_1, 1)
        pass

    def playSound(self, soundId: int):
        for i in range(0, 256, 5):
            if soundId == SOUND_ITEM_COLLECT:
                Sound.playSound(i, 9, 100)
            elif soundId == SOUND_ITEM_ACTIVATE:
                Sound.playSound(255 - i, 9, 100)
            elif soundId == SOUND_GAMEOVER:
                Sound.playSound(60, 9, 100)

        pass
