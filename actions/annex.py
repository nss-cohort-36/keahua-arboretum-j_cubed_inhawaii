import os
from environments import River
from environments import Coastline
from utilities import Banner

def annex_habitat(arboretum):

    Banner.display_banner()

    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Forest")
    print("6. Mountain")

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
    if choice == "2":
        swamp = Swamp()
        arboretum.swamps.append(swamp)
    if choice == "3":
        coastline = Coastline()
        arboretum.coastlines.append(coastline)
    if choice == "4":
        grassland = Grassland()
        arboretum.grasslands.append(grassland)
    if choice == "5":
        forest = Forest()
        arboretum.forests.append(forest)
    if choice == "6":
        mountain = Mountain()
        arboretum.mountains.append(mountain)
