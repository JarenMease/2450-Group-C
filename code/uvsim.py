from main import *
from execute_program import *

class UVSim():
  
    def __init__(self):
        self._memory = memory()
        self._accumulator = 0
        self._pc = 0
        self._operand = 0
        self._op = 0
        self._program = []
    
#     def read_ml_program(self):  #Brandon Comment THIS NEEDS TO BE DONE IN FRONT END
#       self._file = input("Enter the name of the input file: ")
#       try:
#   # Read program from file
#         with open(self._file, 'r') as file:
#           for line in file:
#               line = line.strip()
              
#               # Check that line in file is a word
#               try: 
#                   instruction = int(line)
#               except:
#                   raise ValueError(f"Line {line} contains a non-integer character. All words must be integers. Please correct the program txt file.")

#               # Check word size
#               if len(line) == 5 and line[0] not in ('+', '-'):
#                   raise ValueError(f"Line {line[0]} == 5 but first character is not + or -. Please correct the program txt file.")            
#               elif len(line) not in (4, 5):                   
#                   raise ValueError(f"Line {line} is more or less than 4 digits. Please correct the program txt file.")

#               self._program.append(instruction)
    
#       except FileNotFoundError:
#           print(f"File {self._file} not found. Please enter a valid file name.")
#           self.read_ml_program()
    
    
    def set_accumulator(self, value):
        self._accumulator = value
      
    def get_accumulator(self):
      return self._accumulator
    
    def set_operand(self, value):
      self._operand = value
      
    def get_operand(self):
      return self._operand
    
    def set_program(self, program):
      self._program = program
    
    def get_program(self):
      return self._program
    
    def set_pc(self, value):
      self._pc = value
    
    def get_pc(self):
      return self._pc
    


class arithmetic():
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def divide(a, b):
        if b == 0:
            # print("Did not divide. Zero division error.") Taking out since it communicates with user. We don't like talking to them.
            return a
        return a // b
    
    def multiply(a, b):
        return a * b
      
class branch():
    def branch(operand):
        return operand
    
    def branchNeg(accumulator, operand, pc):
        if accumulator < 0:
            return operand
        else:
            return pc + 1
        
    def branchZero(accumulator, operand, pc):
        if accumulator == 0:
            return operand
        else:
            return pc + 1
          
    def halt():
        return True
      
      
class memory():
  
    def __init__(self, size=100):
        self._memory = [0] * size
        
    def load_ml_program(self, program):
        for i, instruction in enumerate(program):
            self._memory[i] = instruction
    
    def load(self, operand):
        return self._memory[operand]
      
    def store(self, operand, accumulator):
        self._memory[operand] = accumulator
        
      
    def len(self):
        return len(self._memory)
