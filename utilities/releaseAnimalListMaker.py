class ReleaseAnimalListMaker:
    def release_animal_list_maker(condition, biome_list, list):
            if condition:
                for biome in biome_list:
                    if biome.animal_count() < biome.max_animals:
                        dic = {"biome": biome}
                        list.append(dic)
