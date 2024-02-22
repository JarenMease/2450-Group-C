class UVSim():
  
    def __init__(self, size):
        self._memory = [0] * size
        self._accumulator = 0
        self._pc = 0
        self._operand = 0
        self._op = 0
        self._program = []

    def load_ml_program(self, program):
        for i, instruction in enumerate(program):
            self._memory[i] = instruction

    def load(self):
        return self._memory[self._operand]
      
    def store(self):
        self._memory[self._operand] = self._accumulator

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def divide(self, a, b):
        if b == 0:
            return a
        return a // b
    
    def multiply(self, a, b):
        return a * b
      
    def branch(self, operand):
        return operand
    
    def branch_neg(self, accumulator, operand, pc):
        if accumulator < 0:
            return operand
        else:
            return pc + 1
        
    def branch_zero(self, accumulator, operand, pc):
        if accumulator == 0:
            return operand
        else:
            return pc + 1
          
    def halt(self):
        return True
    
      
      

        
