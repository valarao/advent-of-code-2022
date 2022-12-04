from solutions.day01_calorie_counting import *
from solutions.day02_rock_paper_scissors import *
from solutions.day03_rucksack_reorganization import *
from solutions.day04_camp_cleanup import *

from helpers import print_solution_output

# Day 1
print_solution_output("day01_1_calorie_counting.txt", get_total_calories_of_elf_carrying_the_most, "Day 1 Question 1")
print_solution_output("day01_2_calorie_counting.txt", get_total_calories_of_top_3_elves_carrying_the_most, "Day 1 Question 2")

# Day 2
print_solution_output("day02_1_rock_paper_scissors.txt", calculate_rock_paper_scissors_score_with_recommended_moves, "Day 2 Question 1")
print_solution_output("day02_2_rock_paper_scissors.txt", calculate_rock_paper_scissors_score_with_outcomes, "Day 2 Question 2")

# Day 3
print_solution_output("day03_1_rucksack_reorganization.txt", sum_common_rucksack_priorities, "Day 3 Question 1")
print_solution_output("day03_2_rucksack_reorganization.txt", sum_common_rucksack_priorities_for_grouped_rucksacks, "Day 3 Question 2")

# Day 4
print_solution_output("day04_1_camp_cleanup.txt", get_number_of_fully_contained_assignments, "Day 4 Question 1")
print_solution_output("day04_2_camp_cleanup.txt", get_number_of_overlapping_assignments, "Day 4 Question 2")
