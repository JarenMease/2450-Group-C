#import pytest
from main import *
from execute_program import *

def test_always_passes():
    assert True

# def test_always_fail():
#     assert False
   
def test_load():
    my_Sim = execute_program()
    my_Sim._memory.store(0, 10)
    accumulator = my_Sim._memory.load(my_Sim._operand)
    assert accumulator == 10

def test_neg_load():
    my_Sim = execute_program()
    my_Sim._memory.store(0, -5)
    accumulator = my_Sim._memory.load(my_Sim._operand)
    assert accumulator == -5
    
def test_store():
    my_Sim = execute_program()
    my_Sim._memory.store(0, 10)
    my_Sim.set_accumulator(50)
    my_Sim._memory.store(my_Sim._operand, my_Sim._accumulator)
    storing = my_Sim._memory.load(my_Sim._operand)
    assert storing == 50

def test_neg_store():
    my_Sim = execute_program()
    my_Sim._memory.store(0, -10)
    my_Sim.set_accumulator(-50)
    my_Sim._memory.store(my_Sim._operand, my_Sim._accumulator)
    storing = my_Sim._memory.load(0)
    assert storing == -50

def test_multiply():
    my_Sim = execute_program()
    my_Sim.set_accumulator(10)
    my_Sim._memory.store(0, 5)
    result = arithmetic.multiply(my_Sim._memory.load(0), my_Sim._accumulator)
    assert result == 50

def test_neg_multiply():
    my_Sim = execute_program()
    my_Sim.set_accumulator(-10)
    my_Sim._memory.store(0, 5)
    result = arithmetic.multiply(my_Sim._memory.load(0), my_Sim._accumulator)
    assert result == -50
    
def test_divide():
    my_Sim = execute_program()
    my_Sim.set_accumulator(10)
    my_Sim._memory.store(0, 5)
    result = arithmetic.divide( my_Sim.get_accumulator(), my_Sim._memory.load(0))
    assert result == 2

def test_zero_divide():
    my_Sim = execute_program()
    my_Sim.set_accumulator(10)
    result = arithmetic.divide(my_Sim.get_accumulator(), my_Sim._memory.load(0))
    assert result == 10

def test_neg_divide():
    my_Sim = execute_program()
    my_Sim.set_accumulator(-10)
    my_Sim._memory.store(0, 5)
    result = arithmetic.divide(my_Sim.get_accumulator(), my_Sim._memory.load(0))
    assert result == -2

def test_divide_less_one():
    my_Sim = execute_program()
    my_Sim.set_accumulator(1)
    my_Sim._memory.store(0, 5)
    result = arithmetic.divide(my_Sim.get_accumulator(), my_Sim._memory.load(0))
    assert result == 0
    
def test_branch():
    my_Sim = execute_program()
    my_Sim.set_operand(5)
    result = branch.branch(my_Sim.get_operand())
    assert result == 5
    
def test_branch2():
    my_Sim = execute_program()
    my_Sim.set_pc(10)
    my_Sim.set_operand(15)
    result = branch.branch(my_Sim.get_operand())
    assert result == 15
        
def test_branchNeg():
    my_Sim = execute_program()
    my_Sim.set_operand(20)
    my_Sim.set_accumulator(-5)
    result = branch.branchNeg(my_Sim.get_accumulator(), my_Sim.get_operand(), my_Sim.get_pc())
    assert result == 20
    
def test_branchNeg2():
    my_Sim = execute_program()
    my_Sim.set_operand(5)
    my_Sim.set_accumulator(5)
    result = branch.branchNeg(my_Sim.get_accumulator(), my_Sim.get_operand(), my_Sim.get_pc())
    assert result == 1

def test_branchZero():
    my_Sim = execute_program()
    my_Sim.set_operand(25)
    my_Sim.set_pc(5)
    result = branch.branchZero(my_Sim.get_accumulator(), my_Sim.get_operand(), my_Sim.get_pc())
    assert result == 25
    
def test_branchZero2():
    my_Sim = execute_program()
    my_Sim.set_accumulator(5)
    result = branch.branchZero(my_Sim.get_accumulator(), my_Sim.get_operand(), my_Sim.get_pc())
    assert result == 1
    
def test_add():
    my_Sim = execute_program()
    my_Sim.set_accumulator(5)
    my_Sim._memory.store(0, 5)
    result = arithmetic.add(my_Sim.get_accumulator(), my_Sim._memory.load(0))
    assert result == 10

def test_add2():
    my_Sim = execute_program()
    my_Sim.set_accumulator(5)
    my_Sim.set_program([3005, 4300, 0000, 0000, 0000, 5])
    my_Sim._memory.load_ml_program(my_Sim.get_program())
    my_Sim.execute()
    result = my_Sim.get_accumulator()
    assert result == 10
    # my_Sim = [(30, 5), (43,00)]
    # accumulator = 5
    # memory = [0] * 100
    # memory[5] = 5
    # memory, accumulator = execute_my_Sim(my_Sim, memory, accumulator)
    # assert accumulator == 10
    
def test_subtract():
    my_Sim = execute_program()
    my_Sim.set_accumulator(10)
    my_Sim._memory.store(0, 5)
    result = arithmetic.subtract(my_Sim.get_accumulator(), my_Sim._memory.load(0))
    assert result == 5
    
def test_subtract2():
    my_Sim = execute_program()
    my_Sim.set_accumulator(10)
    my_Sim.set_program([3105, 4300, 0000, 0000, 0000, 5])
    my_Sim._memory.load_ml_program(my_Sim.get_program())
    my_Sim.execute()
    result = my_Sim.get_accumulator()
    assert result == 5
    
def test_execute_my_Sim():
    my_Sim = execute_program()
    my_Sim.set_program([2006, 3006, 3106, 3006, 4300, 0000, 5])
    my_Sim._memory.load_ml_program(my_Sim.get_program())
    my_Sim.execute()
    result = my_Sim.get_accumulator()
    assert result == 10

def test_execute_my_Sim2():
    my_Sim = execute_program()
    my_Sim.set_program([2005, 3110, 4300, 0000, 0000, 10, 0000, 0000, 0000, 0000, 5])
    my_Sim._memory.load_ml_program(my_Sim.get_program())
    my_Sim.execute()
    result = my_Sim.get_accumulator()
    assert result == 5
