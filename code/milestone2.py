import argparse

def load(operand, memory):
    return memory[operand]

def store(accumulator, operand, memory):
    memory[operand] = accumulator

def multiply(accumulator, operand, memory):
    return accumulator * memory[operand]

def divide(accumulator, operand, memory):
    return accumulator // memory[operand]

def branch(operand):
    return operand

def branchNeg(operand, pc):
    if operand < 0:
        return operand
    else:
        return pc
    
def branchZero(operand, pc):
    if operand == 0:
        return operand
    else:
        return pc
    

def read_ml_program(file_path):
    program = []
    with open(file_path , 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('+'):
                op = int(line[1:3]) 
                operand = int(line[3:])
                operand = f"{operand:02}"
                program.append((op, int(operand)))
            else:
                op = int(line[:2])
                operand = int(line[2:]) 
                operand = int(f"{operand:02}") 
                program.append((op, operand))
    # print(program)  
    return program


def execute_program(program, memory, accumulator):
    pc = 0  # Program counter
    while True:
        op, operand = program[pc]
        pc += 1

        if op == 10:  # READ
            memory[operand]
        elif op == 11:  # WRITE
            print(memory[operand])

        elif op == 20:  # LOAD
            accumulator = load(operand, memory)
        elif op == 21:  # STORE
            store(accumulator, operand, memory)

        elif op == 30:  # ADD
            accumulator += memory[operand]
        elif op == 31:  # SUBTRACT
            accumulator -= memory[operand]
        elif op == 32:  # DIVIDE
            accumulator = divide(accumulator, operand, memory)
        elif op == 33:  # MULTIPLY
            accumulator = multiply(accumulator, operand, memory)

        elif op == 40:  # Branch
            pc = branch(operand)
        elif op == 41:  # BranchNeg
            pc = branchNeg(operand, pc)
        elif op == 42:  # BranchZero
            pc = branchZero(operand, pc)

        elif op == 43:  # HALT
            break
        else:
            print(f"Unknown operation: {op}")
            break

    return memory, accumulator

def main():
    # Initialize memory and accumulator
    memory = [0] * 100
    accumulator = 0

    # Ask for input file
    filename = input("Enter the name of the input file: ")

    # Define BasicML program
    program = []

    # Read program from file
    with open(filename, 'r') as file:
        for line in file:
            instruction = int(line)
            op = instruction // 100  # First two digits
            operand = instruction % 100  # Last two digits

            if op == 10:  # READ
                value = int(input(f"What number would you like read into location {operand}? "))
                memory[operand] = value
                continue

            program.append((op, operand))

    # Execute program
    memory, accumulator = execute_program(program, memory, accumulator)

    # Print the result
    print("Result:", accumulator)

if __name__ == "__main__":
    # read_ml_program("programtest.txt")
    main()
    
