from uvsim import *
            
            
class execute_program(UVSim):
      def execute(self):
        self._pc = 0
        while self._pc < len(self._memory.len()):
            self._op = self._memory.get[self._pc] // 100 # JA comment currently we don't have op as an attr in class #Brandon Comment, Added it haha
            self._operand = self._memory.get[self._pc] % 100  
            match self._op:
              case 10: #read
                  self.read() # BW GUI.READ THIS HAS TO BE DONE IN FRONT END
              case 11: #write
                  self.write() # BW GUI.WRITE THIS HAS TO BE DONE IN FRONT END
              case 20: #load
                  self._accumulator = self._memory.load(self._operand)
              case 21: #store
                  self._memory.store(self._operand, self._accumulator)
              case 30: #add
                  self._accumulator = arithmetic.add(self._accumulator, self._memory.get[self._operand])
              case 31: #subtract
                  self._accumulator = arithmetic.subtract(self._accumulator, self._memory.get[self._operand])
              case 32: #divide
                  self._accumulator = arithmetic.divide(self._accumulator, self._memory.get[self._operand])
              case 33: #multiply
                  self._accumulator = arithmetic.multiply(self._accumulator, self._memory.get[self._operand])
              case 40: #branch
                  self._pc = branch.branch(self._operand)
              case 41: #branchNeg
                  self._pc = branch.branchNeg(self._accumulator, self._operand, self._pc)
              case 42: #branchZero
                  self._pc = branch.branchZero(self._accumulator, self._operand, self._pc)
              case 43: #halt
                  my_bool = branch.halt()
                  if my_bool:
                    break
            if self._op not in (40, 41, 42):
              self._pc += 1
        if self._pc > 99:
            print("Program too long. Program halted.") #BW GUI.too_big? THIS HAS TO BE DONE IN FRONT END
    
      def read(self): #BW GUI.READ THIS HAS TO BE DONE IN FRONT END
        while True:
          try:
            value = int(input(f"What number would you like read into memory location {self._operand}? "))
            self._memory.store[self._operand] = value
            break
          except ValueError:
            print("Please enter a valid number.")
            continue
    
      def write(self): #BW GUI.WRITE THIS HAS TO BE DONE IN FRONT END
        print(self._memory.get[self._operand])
    



      
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