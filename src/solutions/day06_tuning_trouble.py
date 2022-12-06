def get_start_of_packet_marker(buffer, distinct_count):
    seen = set()
    left = 0
    right = 0
    while right < len(buffer):
        element = buffer[right]
        while element in seen:
            seen.remove(buffer[left])
            left += 1
        seen.add(element)
        if len(seen) == distinct_count:
            return right + 1
        right += 1

def day06_solution_1(buffer_line):
    return get_start_of_packet_marker(buffer_line[0], 4)

def day06_solution_2(buffer_line):
    return get_start_of_packet_marker(buffer_line[0], 14)
