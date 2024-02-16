import argparse


def read(operand, memory):
    while True:
        try:
            value = int(input(f"What number would you like read into location {operand}? "))
            memory[operand] = value
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    return value

def write(operand, memory):
    print(memory[operand])

def load(operand, memory):
    return memory[operand]

def store(accumulator, operand, memory):
    memory[operand] = accumulator

def add(accumulator, operand, memory):
    return accumulator + memory[operand]

def subtract(accumulator, operand, memory):
    return accumulator - memory[operand]

def multiply(accumulator, operand, memory):
    return accumulator * memory[operand]

def divide(accumulator, operand, memory):
    if memory[operand] == 0:
        print("Did not divide. Zero division error.")
        return accumulator
    return accumulator // memory[operand]

def branch(operand):
    return operand

def branchNeg(accumulator, operand, pc):
    if accumulator < 0:
        return operand
    else:
        return pc
    
def branchZero(accumulator, operand, pc):
    if accumulator == 0:
        return operand
    else:
        return pc
    
def read_ml_program(file_path):
    # Define BasicML program
    program = []
    
    # Read program from file
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

             # Check that line in file is a word
            try: 
                instruction = int(line)
            except:
                raise TypeError(f"Line {line} contains a non-integer character. All words must be integers. Please correct the program txt file.")

            # Check word size
            if len(line) == 5 and line[0] not in ('+', '-'):
                raise ValueError(f"Line {line[0]} == 5 but first character is not + or -. Please correct the program txt file.")            
            elif len(line) not in (4, 5):                   
                raise ValueError(f"Line {line} is more or less than 4 digits. Please correct the program txt file.")

            program.append(instruction)
        
        return program

def load_ml_program(program, memory):
    # Load program into main memory starting at location 00
    for i, instruction in enumerate(program):
        memory[i] = instruction

    return memory

def execute_program(memory, accumulator):
    
    pc = 0  # Program counter
    while True:
        # Get op and operand for current pc position
        op = memory[pc] // 100 # First two digits in memory location
        operand = memory[pc] % 100 # Last two digits of in memory location

        pc += 1  # If HALT did not occur, increment pc

        # Perform operation only if op code is found
        if op == 10:  # READ
            read(operand, memory)
        elif op == 11:  # WRITE
            write(operand, memory)

        elif op == 20:  # LOAD
            accumulator = load(operand, memory)
        elif op == 21:  # STORE
            store(accumulator, operand, memory)

        elif op == 30:  # ADD
            accumulator = add(accumulator, operand, memory)
        elif op == 31:  # SUBTRACT
            accumulator = subtract(accumulator, operand, memory)
        elif op == 32:  # DIVIDE
            accumulator = divide(accumulator, operand, memory)
        elif op == 33:  # MULTIPLY
            accumulator = multiply(accumulator, operand, memory)

        elif op == 40:  # BRANCH
            pc = branch(operand)
        elif op == 41:  # BRANCHNEG
            pc = branchNeg(accumulator, operand, pc)
        elif op == 42:  # BRANCHZERO
            pc = branchZero(accumulator, operand, pc)

        elif op == 43:  # HALT
            break

        if pc > 99:  # If pc > 99, it is outside memory. Memory only goes from 00 to 99. 
            raise RuntimeError (f"Program exceeds available memory. Program ran without encountering a HALT command. Exiting program.")

    return memory, accumulator

def main():
    # Initialize memory and accumulator
    memory = [0] * 100
    accumulator = 0

    # Ask for input file
    while True:
        filename = input("Enter the name of the input file: ")
        try:
            with open(filename, 'r'):
                break
        except FileNotFoundError:
            print("File not found. Please try again.")

    # Read BasicML program from file
    program = read_ml_program(filename)

    # Load program into memory
    memory = load_ml_program(program, memory)

    # Execute program
    memory, accumulator = execute_program(memory, accumulator)

    # Print the result
    print("Result:", accumulator)

if __name__ == "__main__":
    main()
    
