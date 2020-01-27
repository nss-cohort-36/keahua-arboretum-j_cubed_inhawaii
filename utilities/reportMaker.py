def report_maker(name, id, animal_list, plant_list):
    string_id = str(id)
    string_builder = f"{name} [{string_id[:8]}]\n"
    total_list = animal_list + plant_list
    list_count = len(total_list)

    for index, item in enumerate(total_list.items()):
            string_builder += f"{item[1]} {item[0]}\n"
    return string_builder
