import argparse


def multiply(accumulator, operand, memory):
    return accumulator * memory[operand]

def test_multiply():
    memory = [0] * 100
    memory[0] = 4
    accumulator = 10
    operand = 0
    result = multiply(accumulator, operand, memory)
    print(result)

def divide(accumulator, operand, memory):
    return accumulator // memory[operand]

def test_divide():
    memory = [0] * 100
    memory[0] = 4
    accumulator = 10
    operand = 0
    result = divide(accumulator, operand, memory)
    print(result) 
    

# def read_program(file_path):
#     program = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             op, operand = map(int, line.split())
#             program.append((op, operand))
#     return program


def main():
    # parser = argparse.ArgumentParser(description='Process a BasicML program.')
    # parser.add_argument('file', help='The input file containing the BasicML program')
    # args = parser.parse_args()


    # Initialize memory and accumulator
    memory = [0] * 100
    accumulator = 0

    # Define BasicML program
    program = [
        (10, 0),  # READ into memory[0]
        (20, 0),  # LOAD memory[0] into accumulator
        (30, 0),  # ADD memory[0] to accumulator
        (21, 1),  # STORE accumulator into memory[1]
        (11, 1),  # WRITE memory[1] to screen
        (43, 0)   # HALT
    ]

    # Execute program
    pc = 0  # Program counter
    while True:
        op, operand = program[pc]
        pc += 1

        if op == 10:  # READ
            memory[operand] = int(input("Enter a number: "))
        elif op == 11:  # WRITE
            print(memory[operand])

        elif op == 20:  # LOAD
            accumulator = memory[operand]
        elif op == 21:  # STORE
            memory[operand] = accumulator

        elif op == 30:  # ADD
            accumulator += memory[operand]
        elif op == 31:  # SUBTRACT
            accumulator -= memory[operand]
        elif op == 32:  # DIVIDE
            accumulator /= memory[operand]
        elif op == 33:  # MULTIPLY
            accumulator = multiply(accumulator, operand, memory)

            
        elif op == 40:  #Branch
            pc == operand
        elif op == 41:  #BranchNeg
            if accumulator < 0:
                pc == operand
        elif op == 42:  #BranchZero
            if accumulator == 0:
                pc == operand

        elif op == 43:  # HALT
            break
        else:
            print(f"Unknown operation: {op}")
            break

if __name__ == "__main__":
    # main()
    test_multiply()
