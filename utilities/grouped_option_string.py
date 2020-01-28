def grouped_option_string(inhabitant, animalList, plantList):
        string_builder = f"{inhabitant.name} ("
        total_list = animalList + plantList
        list_count = len(total_list)
        for index, item in enumerate(total_list.items()):
            string_builder += f"{item[1]} {item[0]}"
            if index + 1 != list_count:
                string_builder += ","
        string_builder += ")"
        return string_builder
