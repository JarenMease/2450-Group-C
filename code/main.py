from executeProgram import *
from uvsim import *

def main():
    my_Sim = execute_program()
    my_Sim.read_ml_program() #should rename to read_ml_program BW Need to go to the front end
    my_Sim._memory.load_ml_program(my_Sim._program)
    my_Sim.execute_program.execute()

if __name__ == "__main__":
    main()
    

# ELEPHANT CODE GRAVEYARD
    # Initialize memory and accumulator
    # memory = [0] * 100
    # accumulator = 0

    # Ask for input file
    # while True:
    #     filename = input("Enter the name of the input file: ")
    #     try:
    #         with open(filename, 'r'):
    #             break
    #     except FileNotFoundError:
    #         print("File not found. Please try again.")

    # Read BasicML program from file
    # program = read_ml_program(filename)

    # Execute program
    # memory, accumulator = execute_program(program, memory, accumulator)

    # Print the result
    
    # def read(operand, memory):
#     while True:
#         try:
#             value = int(input(f"What number would you like read into location {operand}? "))
#             memory[operand] = value
#             break
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue
#     return value

# def write(operand, memory):
#     print(memory[operand])

# def load(operand, memory):
#     return memory[operand]

# def store(accumulator, operand, memory):
#     memory[operand] = accumulator

# def add(accumulator, operand, memory):
#     return accumulator + memory[operand]

# def subtract(accumulator, operand, memory):
#     return accumulator - memory[operand]

# def multiply(accumulator, operand, memory):
#     return accumulator * memory[operand]

# def divide(accumulator, operand, memory):
#     if memory[operand] == 0:
#         print("Did not divide. Zero division error.")
#         return accumulator
#     return accumulator // memory[operand]

# def branch(operand):
#     return operand

# def branchNeg(accumulator, operand, pc):
#     if accumulator < 0:
#         return operand
#     else:
#         return pc
    
# def branchZero(accumulator, operand, pc):
#     if accumulator == 0:
#         return operand
#     else:
#         return pc
    
# def read_ml_program(file_path):
#     # Define BasicML program
#     program = []

#     valid_operands = [00, 10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43]
    
#     # Read program from file
#     with open(file_path, 'r') as file:
#         for line in file:
#             line = line.strip()
#             if len(line) > 5 or len(line) < 4:
#                 raise ValueError(f"Command {line} is more or less than 4 digits. Please correct the program txt file.")
#             instruction = int(line)
#             op = instruction // 100  # First two digits
#             operand = instruction % 100  # Last two digits5

#             if op not in valid_operands:
#                 raise ValueError(f"Invalid operand {op}. Please correct the file.")

#             program.append((op, operand))
        
#         return program

# def execute_program(program, memory, accumulator):
#     pc = 0  # Program counter
#     while True:
#         op, operand = program[pc]
#         pc += 1

#         if op == 10:  # READ
#             read(operand, memory)
#         elif op == 11:  # WRITE
#             write(operand, memory)

#         elif op == 20:  # LOAD
#             accumulator = load(operand, memory)
#         elif op == 21:  # STORE
#             store(accumulator, operand, memory)

#         elif op == 30:  # ADD
#             accumulator = add(accumulator, operand, memory)
#         elif op == 31:  # SUBTRACT
#             accumulator = subtract(accumulator, operand, memory)
#         elif op == 32:  # DIVIDE
#             accumulator = divide(accumulator, operand, memory)
#         elif op == 33:  # MULTIPLY
#             accumulator = multiply(accumulator, operand, memory)

#         elif op == 40:  # Branch
#             pc = branch(operand)
#         elif op == 41:  # BranchNeg
#             pc = branchNeg(accumulator, operand, pc)
#         elif op == 42:  # BranchZero
#             pc = branchZero(accumulator, operand, pc)

#         elif op == 43:  # HALT
#             break
#         else:
#             print(f"Unknown operation: {op}")
#             break

#     return memory, accumulator