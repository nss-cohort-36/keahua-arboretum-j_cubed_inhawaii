from animals import RiverDolphin

def release_animal(arboretum):
    animal = None

    print("1. River Dolphin")
    print("2. Dragonfly")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()

    if choice == "2":
        pass


    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. {river}')

    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].add_animal(animal)

    choice = input("> ")


