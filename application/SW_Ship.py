# #include "Arduino.h"
# #include "sprite.h"
import Sprite
# #include "Joystick.h"
import Joystick
# #include "sw_projectileManagement.h"
import SW_ProjectileManagement
# #include "sw_constants.h"
import SW_Constants
# #include "display.h"
import Display
# TODO #include "RgbLed.h"
# #include "sw_projectile.h"
import SW_Projectile


class Ship(Sprite):
    def __init__(self):
        # Attribute
        self._shipLives: int = 3
        self._orientation: int
        self._shipColor: int
        self._timerTickMove: int = SW_Constants.SHIP_TICK_MOVE
        self._timerTickShot: int = SW_Constants.SHIP_TICK_SHOT
        self._hitBoxOne: int
        self._hitBoxTwo: int
        self._hitBoxThree: int
        self._rightBorder: int
        self._leftBorder: int
        self._upperBorder: int
        self._bottomBorder: int
        self._xPos: int
        self._yPos: int

        # TODO C++: uint8_t shipBorderArray[4];
        self._shipBorderArray: int = [] * 4

    """
     * Die Methode erzeugt ein spezifisches Projektil​ (siehe Modul ProjectileManagement - getProjectiles)​.
     * @param projectile
    """
    def _shot(self, projectileManagement: SW_ProjectileManagement.ProjectileManagement):
        pass

    """
     * Diese Methode wird bei der Instanziierung und nach jeder Bewegung des Raumschiffes aufgerufen.
     * Sie setzt die Hitboxen auf die abzufragenden Felder der Raumschiffe.
    """
    def _setHitBoxes(self):
        pass

    """
     * Diese Methode generiert die Form eines Raumschiffs. Die Form besteht aus einer Anordnung von Einträgen in eine
     * Bitmap. Jeder Eintrag bestimmt ein individuelles Element der Form. Vor dem Aufruf dieser Methode muss die
     * Methode setOrientation() für jede Schiffsinstanz aufgerufen werden.
    """
    def setBitMap(self):
        pass

    """
     * Diese Methode prüft auf eingetretene Kollision mit Projektilen.
     * @param projectile
    """
    def checkHitWithProjectile(projectileManagement: SW_ProjectileManagement.ProjectileManagement):
        pass

    """
     * Diese Methode wird von der Spiellogik für jede Schiffsinstanz aufgerufen. Die Orientierung des Joystick`s muss
     * an die Orientierung der Schiffsinstanz angepasst werden. Die Methode benötigt für die Erzeugung einen Parameter
     * der die Funktionalität bietet die Projektil Listen aufzurufen (siehe Modul ProjectileManagement - getProjectiles).
     * @param joystick
     * @param projectile (optional)
     * @param projectileManagement (optional)
    """
    def moveShipAndShot(self, joystick: Joystick, projectileManagement: SW_ProjectileManagement.ProjectileManagement):
        pass

    """
     * Die Methode reduziert die verbleibende Anzahl des Spielerlebens um Eins.
    """
    def decrementShipLives(self):
        pass

    """
     * Diese Methode setzt die Orientierung / Spielfeldseite eines Raumschiffes.
     * @param orientation
    """
    def setOrientation(self, orientation: int):
        pass

    """
     * Diese Methode gibt die Orientierung / Spielfeldseite eines Raumschiffes zurück.
     * @return uint8_t orientation
    """
    def getOrientation(self) -> int:
        pass

    """
     * Diese Methode ändert die Farbe aller Pixel eines Raumschiffes.
     * @param color
    """
    def setShipColor(self, color: int):
        pass

    """
     * Mit dieser Methode kann jeder Pixel des Raumschiffs separat verändert werden. Durch einen Indexzugriff auf das
     * Feld des Pixels und ein Indexzugriff auf die Farbe kann auf einen Pixel zugegriffen werden.
     * @param pixel
     * @param color
    """
    # TODO C++: void setShipPixelColor(uint8_t *pixel, uint16_t *color);
    def setShipPixelColor(self, pixel: int, color: int):
        pass

    """
     * Mit dieser Methode kann der Default-Tickwert der Bewegung verändert werden.
     * @param tickValue
    """
    def setTickMoveDefault(self, tickValue: int):
        pass

    """
     * Diese Methode setzt die Anzahl der Leben eines Schiffes (Spielerleben).
     * @param livesValue
    """
    def setShipLives(self, livesValue: int):
        pass

    """
     * Diese Methode liefert die derzeitige Anzahl der Leben eines Schiffs (Spielerleben) zurück.
     * @return uint8_t shipLives
    """
    def getShipLives(self) -> int:
        pass

    """
     * Mit dieser Methode kann der Default-Tickwert der Schusshäufigkeit verändert werden.
     * @param tickValue
    """
    def setTickShotDefault(self, tickValue: int):
        pass

    """
     * Diese Methode gibt den Default-Tickwert der Bewegung des Raumschiffes zurück.
     * @return uint8_t TickMoveDefault
    """
    def getTickMoveDefault(self) -> int:
        pass

    """
     * Diese Methode liefert die Spielfeldgrenzen als Array zurück.
     * @return unit8_t 4 int-Werte für die Grenzen.
    """
    # TODO C++: uint8_t *getBorderRightLeftUpperBottom(void);
    def getBorderRightLeftUpperBottom(self) -> int:
        pass

    """
    /**
     * Diese Methode setzt anhand der Parameter die Spielfeldgrenzen eines Spielers. Diese Methode wird bei der
     * Initialisierung der Schiffsinstanzen aufgerufen und setzt die Grenzen auf die Größe der Konsole.
     * @param right
     * @param left
     * @param upper
     * @param bottom
     */
    """
    def setBorderRightLeftUpperBottom(self, right: int, left: int, upper: int, bottom: int):
        pass
