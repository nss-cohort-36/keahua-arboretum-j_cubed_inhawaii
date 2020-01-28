import os
from environments import grassland
from plants import Silversword
from utilities import display_banner
from utilities import biome_list_maker


# TODO: Refactor cultivate_plant and this to DRY them up
def cultivate_plant(arboretum):
    display_banner()
    plant = None

    print("1. Silversword")
    print("2. Crabgrass")

    choice = input("Choose plant to cultivate > ")

    if choice == "1":
        plant = Silversword()

    if choice == "2":
        pass

    display_banner()

    def print_habitats():
        option_list = []

        # biome_list_maker(plant.aquatic and  arboretum.rivers, option_list)

        biome_list_maker(plant.terrestrial and plant.drought_tolerant,
                         arboretum.grasslands, option_list, plant)

        for index, dic in enumerate(option_list):
            print(f'{index + 1}. {dic["biome"].print_list_options()}')
            # print(f'{index + 1}. {dic["biome"].name} ({dic["biome"].plant_count()} {"plant" if dic["biome"].plant_count() == 1 else "plants"})')

        option_list_length = len(option_list)
        if option_list_length == 0:
            print("All of your Biomes are at maximum capacity please create a new biome!")
            input("\n\nPress any key to go back to the main menu...")
        else:
            print(f"{option_list_length + 1}. Main Menu")
            print("Release the plant into which biome?")
            choice = input("> ")
            if int(choice) == option_list_length + 1:
                return
            elif choice.isnumeric():

                choice_input = int(choice)

                choice_biome = option_list[choice_input - 1]

                if choice_input <= option_list_length:
                 choice_biome["biome"].add_plant(plant)
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
