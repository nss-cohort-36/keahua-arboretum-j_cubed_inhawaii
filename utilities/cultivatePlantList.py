class CultivatePlantList:
    def cultivate_plant_list_maker(condition, biome_list, list):
        if condition:
            for biome in biome_list:
                if biome.plant_count() < biome.max_plants:
                    dic = {"biome": biome}
                    list.append(dic)
