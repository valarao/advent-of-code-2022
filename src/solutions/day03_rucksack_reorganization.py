def sum_common_rucksack_priorities(rucksacks):
    def get_priority_value(item):
        if item.isupper():
            return ord(item) - 38
        else:
            return ord(item) - 96
    
    total_priority_sum = 0
    for rucksack in rucksacks:
        midpoint = len(rucksack) // 2
        first_compartment = set(rucksack[:midpoint])
        second_compartment = set(rucksack[midpoint:])
        common_items = first_compartment.intersection(second_compartment)
        for common_item in common_items:
            total_priority_sum += get_priority_value(common_item)

    return total_priority_sum

def sum_common_rucksack_priorities_for_grouped_rucksacks(rucksacks):
    def get_priority_value(item):
        if item.isupper():
            return ord(item) - 38
        else:
            return ord(item) - 96

    def group_rucksacks_in_threes(rucksacks):
        index = 0
        rucksack_groups = []
        current_group = []
        while index < len(rucksacks):
            current_group.append(rucksacks[index])
            if len(current_group) == 3:
                rucksack_groups.append(current_group)
                current_group = []
            index += 1
        return rucksack_groups

    def get_common_items_for_rucksack_grouping(rucksack_grouping):
        common_items = set(rucksack_grouping[0])
        for rucksack_set in rucksack_grouping[1:]:
            common_items = common_items.intersection(set(rucksack_set))        
        return common_items
    
    rucksack_groupings = group_rucksacks_in_threes(rucksacks)
    total_priority_sum = 0
    for rucksack_grouping in rucksack_groupings:
        common_items = get_common_items_for_rucksack_grouping(rucksack_grouping)
        for common_item in common_items:
             total_priority_sum += get_priority_value(common_item)

    return total_priority_sum
