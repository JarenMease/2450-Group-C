from uvsim import *
class Execute:
    def execute(op, operand, pc, uvsim, gui):
        # self._pc = 0
        # while self._pc < self._memory.len():

        #     self._op = self._memory.load(self._pc) // 100
        #     self._operand = self._memory.load(self._pc) % 100  

            match op:
              case 10: #read
                  gui.read_input()                  
                  
              case 11: #write
                  gui.write() # BW GUI.WRITE THIS HAS TO BE DONE IN FRONT END
                  
              case 20: #load
                  uvsim.set_accumulator(uvsim._memory.load(operand))
                  value = uvsim.get_accumulator()
                  gui.load(value)
                  
              case 21: #store
                  uvsim._memory.store(operand, uvsim.get_accumulator())
                  value = uvsim._memory.load(operand)
                  gui.store(value)
              case 30: #add
                  accumulator = arithmetic.add(uvsim.get_accumulator(), uvsim._memory.load(operand))
                  uvsim.set_accumulator(accumulator)
                  gui.add(accumulator)
              case 31: #subtract
                  accumulator = arithmetic.subtract(uvsim.get_accumulator(), uvsim._memory.load(operand))
                  uvsim.set_accumulator(accumulator)
                  gui.subtract(accumulator)
              case 32: #divide
                  accumulator = arithmetic.divide(uvsim.get_accumulator(), uvsim._memory.load(operand))
                  uvsim.set_accumulator(accumulator)
                  gui.divide(accumulator)
              case 33: #multiply
                  accumulator = arithmetic.multiply(uvsim.get_accumulator(), uvsim._memory.load(operand))
                  uvsim.set_accumulator(accumulator)
                  gui.multiply(accumulator)
              case 40: #branch
                  pc = branch.branch(operand)
                  gui.branch(pc)
              case 41: #branchNeg
                  pc = branch.branchNeg(uvsim.get_accumulator(), operand, pc)
                  gui.branchNeg(pc)
              case 42: #branchZero
                  pc = branch.branchZero(uvsim.get_accumulator(), operand, pc)
                  gui.branchZero(pc)
              case 43: #halt
                  gui.halt()
            # if self._op not in (40, 41, 42):
            #   self._pc += 1
        # if self._pc > 99:
        #     print("Program too long. Program halted.") #BW GUI.too_big? THIS HAS TO BE DONE IN FRONT END
    
    #   def read(self): #BW GUI.READ THIS HAS TO BE DONE IN FRONT END
    #     while True:
    #       try:
    #         value = int(input(f"What number would you like read into memory location {self._operand}? "))
    #         self._memory._memory[self._operand] = value
    #         break
    #       except ValueError:
    #         print("Please enter a valid number.")
    #         continue
    
    #   def write(self): #BW GUI.WRITE THIS HAS TO BE DONE IN FRONT END
    #     print(self._memory.load(self._operand))
    



      
      # ELEPHANT GRAVEYARD
      
    #   def read(self):
    #   while True:
    #       try:
    #         value = int(input(f"What number would you like read into memory location {self._operand}? "))
    #         self._memory[self._operand] = value
    #         break
    #       except ValueError:
    #         print("Please enter a valid number.")
    #         continue
    
    # def write(self):
    #   print(self._memory[self._operand])
      
    # def load(self):
    #   return self._memory[self._operand]
    
    # def store(self):
    #   self._memory[self._operand] = self._accumulator
      
    # def add(self):
    #   return self._accumulator + self._memory[self._operand]
    
    # def subtract(self):
    #   return self._accumulator - self._memory[self._operand]
    
    # def divide(self):
    #   if self._memory[self._operand] == 0:
    #       print("Did not divide. Zero division error.")
    #       return self._accumulator
    #   return self._accumulator // self._memory[self._operand]
    
    # def multiply(self):
    #   return self._accumulator * self._memory[self._operand]
    
    # def branch(self):
    #   return self._operand
    
    # def branchNeg(self):
    #   if self._accumulator < 0:
    #       return self._operand
    #   else:
    #       return self._pc + 1
        
    # def branchZero(self):
    #   if self._accumulator == 0:
    #       return self._operand
    #   else:
    #       return self._pc + 1
        
    # def set_accumulator(self, value):
    #   self._accumulator = value
      
    # def get_accumulator(self):
    #   return self._accumulator
    
    # def set_memory(self, index, value):
    #   self._memory[index] = value
      
    # def get_memory(self, index):
    #   return self._memory[index]
    
    # def set_pc(self, value):
    #   self._pc = value
    
    # def get_pc(self):
    #   return self._pc
    
    # def set_operand(self, value):
    #   self._operand = value
      
    # def get_operand(self):
    #   return self._operand
    
    # def set_program(self, program):
    #   self._program = program
    
    
    # class UVSim(): #JA Should rename to UVSim or Sim or B
  
    # def __init__(self):
    #     self._memory = memory()
    #     self._accumulator = 0
    #     self._pc = 0
    #     self._operand = 0
    #     self._op = 0
    #     self._program = []
        
    
            
    # def read_ml_program(self): #JA comment should use snake case for Python #Brandon Comment THIS NEEDS TO BE DONE IN FRONT END
    #     self._file = input("Enter the name of the input file: ")
    #     try:
    # # Read program from file
    #       with open(self._file, 'r') as file:
    #         for line in file:
    #             line = line.strip()
                
    #             # Check that line in file is a word
    #             try: 
    #                 instruction = int(line)
    #             except:
    #                 raise ValueError(f"Line {line} contains a non-integer character. All words must be integers. Please correct the program txt file.")

    #             # Check word size
    #             if len(line) == 5 and line[0] not in ('+', '-'):
    #                 raise ValueError(f"Line {line[0]} == 5 but first character is not + or -. Please correct the program txt file.")            
    #             elif len(line) not in (4, 5):                   
    #                 raise ValueError(f"Line {line} is more or less than 4 digits. Please correct the program txt file.")

    #             self._program.append(instruction)
      
    #     except FileNotFoundError:
    #         print(f"File {self._file} not found. Please enter a valid file name.")
    #         self.read_ml_program()
