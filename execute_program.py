class Execute:
    def execute_program(sim, gui):
        sim._pc = 0
        while sim._pc < len(sim._memory):

            sim._op = sim._memory[sim._pc] // 100
            sim._operand = sim._memory[sim._pc] % 100  

            match sim._op:
              case 10: #read
                  gui.read() #front end function
              case 11: #write
                  gui.write() #front end function
              case 20: #load
                  sim._accumulator = sim.load()
              case 21: #store
                  sim.store()
              case 30: #add
                  sim._accumulator = sim.add(sim._accumulator, sim.load())
              case 31: #subtract
                  sim._accumulator = sim.subtract(sim._accumulator, sim.load())
              case 32: #divide
                  sim._accumulator = sim.divide(sim._accumulator, sim.load())
              case 33: #multiply
                  sim._accumulator = sim.multiply(sim._accumulator, sim.load())
              case 40: #branch
                  sim._pc = sim.branch(sim._operand)
              case 41: #branchNeg
                  sim._pc = sim.branch_neg(sim._accumulator, sim._operand, sim._pc)
              case 42: #branchZero
                  sim._pc = sim.branch_zero(sim._accumulator, sim._operand, sim._pc)
              case 43: #halt
                  my_bool = sim.halt()
                  if my_bool:
                      break
            if sim._op not in (40, 41, 42):
              sim._pc += 1
        if sim._pc > 99:
            gui.too_long() #front end function
