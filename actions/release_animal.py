import os
from animals import RiverDolphin
from utilities import display_banner
from utilities import biome_list_maker

def release_animal(arboretum):
    display_banner()
    animal = None

    print("1. River Dolphin")
    print("2. Dragonfly")

    choice = input("Choose animal to release > ")
    option_list = []
    if choice == "1":
        animal = RiverDolphin()

    if choice == "2":
        pass

    display_banner()

    def print_habitats():
        option_list = []

        biome_list_maker(animal.aquatic and animal.cell_type ==
                                  "hypertonic" or animal.cell_type == "isotonic", arboretum.rivers, option_list, animal)

        biome_list_maker(animal.aquatic and animal.cell_type ==
                                  "hypotonic" or animal.cell_type == "isotonic", arboretum.coastlines, option_list, animal)

        for index, dic in enumerate(option_list):
            print(f'{index + 1}. {dic["biome"].print_list_options()}')
            # print(f'{index + 1}. {dic["biome"].name} ({dic["biome"].animal_count()} {"animal" if dic["biome"].animal_count() == 1 else "animals"})')

        option_list_length = len(option_list)
        if option_list_length == 0:
            print("All of your Biomes are at maximum capacity please create a new biome!")
            input("\n\nPress any key to go back to the main menu...")
        else:
            print(f"{option_list_length + 1}. Main Menu")
            print("Release the animal into which biome?")
            choice = input("> ")
            if int(choice) == option_list_length + 1:
                return
            elif choice.isnumeric():

                choice_input = int(choice)

                choice_biome = option_list[choice_input - 1]

                if choice_input <= option_list_length:
                    choice_biome["biome"].add_animal(animal)
                else:
                    display_banner()
                    print(
                        f"{choice_input} is not an option. Please choose an option that is available!")
                    print_habitats()
            else:
                display_banner()
                print(
                    f"{choice} is not an option. Please choose an option that is available!")
                print_habitats()

    print_habitats()
