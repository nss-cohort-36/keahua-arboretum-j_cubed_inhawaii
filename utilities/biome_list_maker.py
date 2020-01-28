from animals import Animal
from plants import Plant


def biome_list_maker(condition, biome_list, optionlist, inhabitant):
    if condition:
        for biome in biome_list:
            if isinstance(inhabitant, Plant):
                if biome.plant_count() < biome.max_plants:
                    dic = {"biome": biome}
                    optionlist.append(dic)
            elif isinstance(inhabitant, Animal):
                if biome.animal_count() < biome.max_animals:
                    dic = {"biome": biome}
                    optionlist.append(dic)
