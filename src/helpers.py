import os

def print_solution_output(input_filename, solution_func, question_identifier):
    def get_input(filename):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        input_file = "{0}/inputs/{1}".format(dir_path, filename)

        with open(input_file) as file:
            lines = [line.rstrip() for line in file]

        return lines

    input = get_input(input_filename)
    answer = solution_func(input)
    print("{0} answer: {1}".format(question_identifier, str(answer)))
