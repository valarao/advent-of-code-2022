def get_number_of_fully_contained_assignments(pairs):
    def contains_other_assignment_fully(outer_assignment_candidate, inner_assignment_candidate):
        oac_start, oac_end = outer_assignment_candidate.split("-")
        iac_start, iac_end = inner_assignment_candidate.split("-")
        return int(oac_start) <= int(iac_start) and int(oac_end) >= int(iac_end)

    fully_contained_assignments = 0
    for pair in pairs:
        assignment_1, assignment_2 = pair.split(",")
        if contains_other_assignment_fully(assignment_1, assignment_2) or contains_other_assignment_fully(assignment_2, assignment_1):
            fully_contained_assignments += 1
    
    return fully_contained_assignments

def get_number_of_overlapping_assignments(pairs):
    def are_overlapping_assignments(assignment_1, assignment_2):
        start_1, end_1 = assignment_1.split("-")
        start_2, _ = assignment_2.split("-")
        return int(start_1) <= int(start_2) and int(end_1) >= int(start_2)

    overlapping_assignments = 0
    for pair in pairs:
        assignment_1, assignment_2 = pair.split(",")
        if are_overlapping_assignments(assignment_1, assignment_2) or are_overlapping_assignments(assignment_2, assignment_1):
            overlapping_assignments += 1
    
    return overlapping_assignments
