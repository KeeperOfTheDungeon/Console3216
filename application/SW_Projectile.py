# #include "Arduino.h"
# #include "Joystick.h"
import Joystick


class SW_Projectile:
    def __init__(self):
        # x-Koordinate
        self.__xCoordinate: int

        # y-Koordinate
        self.__yCoordinate: int

        # Richtungsflag
        self.__directionLeft: bool

        # Valid flag
        self.__valid: bool = False

    """
     * Diese Methode gibt das Richtungsflag eines Projektils zurück.
     * Bei true ist die Flugrichtung eines Projektils links und bei
     * falls ist sie rechts.
     * @return bool directionLeft
    """
    def getDirection(self) -> bool:
        pass

    def getValid(self) -> bool:
        pass

    def setValid(self, valid: bool):
        pass

    """
    * Diese Methode setzt das Richtungsflag eines Projektils.
    * Bei true ist die Flugrichtung eines Projektils links und bei
    * falls ist sie rechts.
    """
    def setDirection(self, directionLeft: bool):
        pass

    """
     * Diese Methode gibt die x-Koordinate eines Projektils zurück.
     * @return int xCoordinate
    """
    def getXCoordinate(self) -> int:
        pass

    """
     * Diese Methode gibt die y-Koordinate eines Projektils zurück.
     * @return int yCoordinate
    """
    def getYCoordinate(self) -> int:
        pass

    """
     * Diese Methode setzt die x-Koordinate eines Projektils auf die
     * übergebene x-Koordinate
     * @param int xCoordinate
    """
    def setXCoordinate(self, xCoordinate: int):
        pass

    """
     * Diese Methode setzt die y-Koordinate eines Projektils auf die
     * übergebene y-Koordinate
     * @param int yCoordinate
    """
    def setYCoordinate(self, yCoordinate: int):
        pass

    """
     * Diese Methode wird aufgerufen, um ein Projektil um ein Pixel
     * nach links oder rechts zu bewegen.
    """
    def move(self):
        pass
