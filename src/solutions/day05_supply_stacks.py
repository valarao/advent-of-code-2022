from collections import deque

def day05_solution_1(input):
    def is_crate_parsing_finished(line):
        return line == ""

    def separate_input(input):
        crates = []
        moves = []
        parsing_crates = True
        for line in input:
            if is_crate_parsing_finished(line):
                parsing_crates = False
            if parsing_crates:
                crates.append(line)
            elif line != "":
                moves.append(line)
        return (crates, moves)

    def create_stacks(crates):
        stacks = {
            1: deque([]),
            2: deque([]),
            3: deque([]),
            4: deque([]),
            5: deque([]),
            6: deque([]),
            7: deque([]),
            8: deque([]),
            9: deque([])
        }

        for crate_line in crates[:len(crates) - 1]:
            for end_index in range(4, len(crate_line) + 4, 4):
                start_index = end_index - 4
                crate_candidate = crate_line[start_index:end_index].rstrip()
                if crate_candidate != "":
                    stack_number = end_index // 4
                    stacks[stack_number].append(crate_candidate[1:2])
        return stacks
    
    def parse_stack_move(move):
        parsed_move = move.split(" ")
        return (int(parsed_move[1]), int(parsed_move[3]), int(parsed_move[5]))

    def simulate_stack_moves(crate_stacks, moves):
        stack_picture = crate_stacks
        for move in moves:
            parse_stack_move(move)
            move_count, start_pos, end_pos = parse_stack_move(move)
            while move_count != 0:
                crate_to_move = stack_picture[start_pos].popleft()
                stack_picture[end_pos].appendleft(crate_to_move)
                move_count -= 1

        return stack_picture

    crates, moves = separate_input(input)
    crate_stacks = create_stacks(crates)
    stack_picture = simulate_stack_moves(crate_stacks, moves)
    top_crates = ""
    for stack_key in stack_picture:
        stack_crates = stack_picture[stack_key]
        if len(stack_crates) != 0:
            top_crates += stack_crates[0]
    
    return top_crates

def day05_solution_2(input):
    def is_crate_parsing_finished(line):
        return line == ""

    def separate_input(input):
        crates = []
        moves = []
        parsing_crates = True
        for line in input:
            if is_crate_parsing_finished(line):
                parsing_crates = False
            if parsing_crates:
                crates.append(line)
            elif line != "":
                moves.append(line)
        return (crates, moves)

    def create_stacks(crates):
        stacks = {
            1: deque([]),
            2: deque([]),
            3: deque([]),
            4: deque([]),
            5: deque([]),
            6: deque([]),
            7: deque([]),
            8: deque([]),
            9: deque([])
        }

        for crate_line in crates[:len(crates) - 1]:
            for end_index in range(4, len(crate_line) + 4, 4):
                start_index = end_index - 4
                crate_candidate = crate_line[start_index:end_index].rstrip()
                if crate_candidate != "":
                    stack_number = end_index // 4
                    stacks[stack_number].append(crate_candidate[1:2])
        return stacks
    
    def parse_stack_move(move):
        parsed_move = move.split(" ")
        return (int(parsed_move[1]), int(parsed_move[3]), int(parsed_move[5]))

    def simulate_stack_moves(crate_stacks, moves):
        stack_picture = crate_stacks
        for move in moves:
            parse_stack_move(move)
            move_count, start_pos, end_pos = parse_stack_move(move)
            crates_to_move = []
            while move_count != 0:
                crate_to_move = stack_picture[start_pos].popleft()
                crates_to_move.append(crate_to_move)
                move_count -= 1
            crates_to_move.reverse()
            for crate_to_move in crates_to_move:
                stack_picture[end_pos].appendleft(crate_to_move)

        return stack_picture

    crates, moves = separate_input(input)
    crate_stacks = create_stacks(crates)
    stack_picture = simulate_stack_moves(crate_stacks, moves)
    top_crates = ""
    for stack_key in stack_picture:
        stack_crates = stack_picture[stack_key]
        if len(stack_crates) != 0:
            top_crates += stack_crates[0]
    
    return top_crates
