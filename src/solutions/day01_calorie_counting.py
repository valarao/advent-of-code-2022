def get_total_calories_of_elf_carrying_the_most(calories_info):
    maximum_calories = 0
    current_calories = 0
    for calorie_info in calories_info:
        if current_calories > maximum_calories:
            maximum_calories = current_calories

        if calorie_info == "":
            current_calories = 0
        else:
            current_calories += int(calorie_info)

    return maximum_calories

def get_total_calories_of_top_3_elves_carrying_the_most(calories_info):
    current_calories = 0
    elf_calories = []

    for calorie_info in calories_info:
        if calorie_info == "":
            elf_calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(calorie_info)

    elf_calories.sort()
    
    return sum(elf_calories[-3:])
