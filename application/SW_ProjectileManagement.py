# #include "sw_constants.h"
import SW_Constants
# #include "sw_projectile.h"
from SW_Projectile import SW_Projectile
# #include <display.h>
import Display


class ProjectileManagement:
    def __init__(self):
        # Array of projectiles
        # TODO C++: SW_Projectile projectile[2*MAXPROJECTILE];
        self.__projectile: SW_Projectile = [] * (2 * SW_Constants.MAXPROJECTILE)

        self.__tickMoveProjectiles: int = 0

    """
     * Diese Methode liefert eine Liste mit allen auf dem Spielfeld aktiven Projektilen.
    """
    def getProjectiles(self, index: int) -> SW_Projectile:
        pass

    """
     * Diese Methode wird von der Spiellogik aufgerufen, um die Rahmenbedingung der Projektile
     * zu prüfen. Die Projektile werden nacheinander mit Hilfe von Projectile::move() bewegt.
     * Zwischen jeder Bewegung eines Projektils wird mittels checkCollision() geprüft ob eine
     * Kollision aufgetreten ist. Sollte eine Kollision aufgetreten sein wird, mit Hilfe der
     * deleteProjectile() Methode, jedes kollidierte Projektil gelöscht.
    """
    def manageProjectiles(self):
        pass

    """
     * Diese Methode wird von den Raumschiffen aufgerufen, wenn diese ein Projektil abfeuern.
     * Diese Methode erzeugt ein Projektil und fügt es in die Liste der Projektile ein. Sie benötigt
     * als Übergabeparameter die Richtung und die X / Y Koordinaten des Projektils.
     * Die Koordinaten referenzieren die Abschussposition des Projektils auf dem Spielfeld. Das
     * Richtungsflag gibt an, ob sich das Projektil nach links (directionLeft = true) oder rechts
     * (directionLeft = false) bewegt.
     * @param x
     * @param y
     * @param directionLeft
    """
    def shoot(self, x: int, y: int, directionLeft: bool):
        pass

    """
     * Diese Methode löscht ein Projektil.
     * Diese Methode wird einerseits von den Raumschiffen aufgerufen, wenn sie von einem
     * Projektil getroffen wurden, als auch von ProjectileManagement, wenn zwei Projektile
     * kollidieren.
     * @param projectileID
    """
    def deleteProjectile(self, projectileID: int):
        pass

    """
     *  Diese Methode prüft auf Kollisionen zwischen Projektilen.
    """
    def checkCollision(self):
        pass

    """
     *  Diese Methode prüft auf Kollisionen mit der Wand.
    """
    def checkBoundaries(self):
        pass

    def draw(self):
        pass
