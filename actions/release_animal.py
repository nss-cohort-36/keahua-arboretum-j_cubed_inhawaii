import os
from animals import RiverDolphin
from stuff.banner import Banner



def release_animal(arboretum):
    Banner.display_banner()
    animal = None

    print("1. River Dolphin")
    print("2. Dragonfly")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()

    if choice == "2":
        pass

    Banner.display_banner()


    def print_habitats():
        option_list = []

        # if isinstance(animal, classinfo)
        for index, river in enumerate(arboretum.rivers):
            river_dict = {index : river}
            option_list.append(river_dict)

            print(f'{index + 1}. {river.name} ({river.animal_count()} {"animal" if river.animal_count() == 1 else "animals"})')

        print("Release the animal into which biome?")
        choice = input("> ")

        if choice.isnumeric():
            choice_input = int(choice)
            if choice_input <= len(arboretum.rivers):
                if arboretum.rivers[int(choice) - 1].add_animal(animal) == True:
                    input("\n\nPress any key to continue...")
                else:
                    Banner.display_banner()
                    print("** ** That biome is not large enough ** **\n**** Please choose another one ** **\n")
                    print_habitats()
            else:
                 Banner.display_banner()
                 print(
                     f"{choice_input} is not an option. Please choose an option that is available!")
                 print_habitats()
        else:
            Banner.display_banner()
            print(
                f"{choice} is not an option. Please choose an option that is available!")
            print_habitats()

    print_habitats()
