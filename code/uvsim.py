class UVSim():
    '''The UVSim class simulates a basic machine and defines machine language operations.
    Operations include loading a program into memory, load/store, math, branch, halt'''
    def __init__(self, size):
        self._memory = [0] * size  # size represents number of registers in memory
        self._accumulator = 0  # results of various operations are stored in accumualtor  
        self._pc = 0  # program counter
        self._operand = 0
        self._op = 0
        self._program = []

    def load_ml_program(self, program):
        # load a program into memory
        for i, instruction in enumerate(program):
            self._memory[i] = instruction

    def load(self):
        # load a word from memory into the accumulator
        return self._memory[self._operand]
      
    def store(self):
        # store a word from the accuulator into memory
        self._memory[self._operand] = self._accumulator

    def add(self, a, b):
        # add a word from memory to a word in the accumulator
        return a + b
    
    def subtract(self, a, b):
        # subtrat a word from memory from a word in the accumulator
        return a - b
    
    def divide(self, a, b):
        # divide a word in the accumulator by a word from memory
        if b == 0:
            return a
        return a // b
    
    def multiply(self, a, b):
        # multiply a word from meory by a word in the accumulator
        return a * b
      
    def branch(self, operand):
        # branch to a specific location in memory
        return operand
    
    def branch_neg(self, accumulator, operand, pc):
        # branch to a location in memroy if the accumulator is negative
        
        if accumulator < 0:
            return operand
        else:
            return pc + 1
        
    def branch_zero(self, accumulator, operand, pc):
        # branch to a location in memroy if the accumulator is 0
        if accumulator == 0:
            return operand
        else:
            return pc + 1
          
    def halt(self):
        # stop the program
        return True
    
        
