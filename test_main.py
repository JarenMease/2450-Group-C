#import pytest
from main import *
from execute_program import *

def test_always_passes():
    assert True

# def test_always_fail():
#     assert False
   
def test_load():
    my_Sim = UVSim()
    my_Sim._memory.store(0, 10)
    accumulator = my_Sim._memory.load(my_Sim._operand)
    assert accumulator == 10

def test_neg_load():
    my_Sim = UVSim()
    my_Sim.set_memory(0, -5)
    accumulator = my_Sim.load()
    assert accumulator == -5
    
def test_store():
    my_Sim = UVSim()
    my_Sim.set_memory(0, 10)
    my_Sim.set_accumulator(50)
    my_Sim.store()
    storing = my_Sim.get_memory(0)
    assert storing == 50

def test_neg_store():
    my_Sim = UVSim()
    my_Sim.set_memory(0, -10)
    my_Sim.set_accumulator(-50)
    my_Sim.store()
    storing = my_Sim.get_memory(0)
    assert storing == -50

def test_multiply():
    my_Sim = UVSim()
    my_Sim.set_accumulator(10)
    my_Sim.set_memory(0, 5)
    result = my_Sim.multiply()
    assert result == 50

def test_neg_multiply():
    my_Sim = UVSim()
    my_Sim.set_accumulator(-10)
    my_Sim.set_memory(0, 5)
    result = my_Sim.multiply()
    assert result == -50
    
def test_divide():
    my_Sim = UVSim()
    my_Sim.set_accumulator(10)
    my_Sim.set_memory(0, 5)
    result = my_Sim.divide()
    assert result == 2

def test_zero_divide():
    my_Sim = UVSim()
    my_Sim.set_accumulator(10)
    my_Sim.set_memory(0, 0)
    result = my_Sim.divide()
    assert result == 10

def test_neg_divide():
    my_Sim = UVSim()
    my_Sim.set_accumulator(-10)
    my_Sim.set_memory(0, 5)
    result = my_Sim.divide()
    assert result == -2

def test_divide_less_one():
    my_Sim = UVSim()
    my_Sim.set_accumulator(1)
    my_Sim.set_memory(0, 5)
    result = my_Sim.divide()
    assert result == 0
    
def test_branch():
    my_Sim = UVSim()
    my_Sim.set_operand(5)
    result = my_Sim.branch()
    assert result == 5
    
def test_branch2():
    my_Sim = UVSim()
    my_Sim.set_pc(10)
    my_Sim.set_operand(15)
    result = my_Sim.branch()
    assert result == 15
        
def test_branchNeg():
    my_Sim = UVSim()
    my_Sim.set_operand(20)
    my_Sim.set_accumulator(-5)
    result = my_Sim.branchNeg()
    assert result == 20
    
def test_branchNeg2():
    my_Sim = UVSim()
    my_Sim.set_operand(5)
    my_Sim.set_accumulator(5)
    result = my_Sim.branchNeg()
    assert result == 1

def test_branchZero():
    my_Sim = UVSim()
    my_Sim.set_operand(25)
    my_Sim.set_pc(5)
    result = my_Sim.branchZero()
    assert result == 25
    
def test_branchZero2():
    my_Sim = UVSim()
    my_Sim.set_accumulator(5)
    result = my_Sim.branchZero()
    assert result == 1
    
def test_add():
    my_Sim = UVSim()
    my_Sim.set_accumulator(5)
    my_Sim.set_memory(0, 5)
    result = my_Sim.add()
    assert result == 10

def test_add2():
    my_Sim = UVSim()
    my_Sim.set_accumulator(5)
    my_Sim.set_program([3005, 4300, 0000, 0000, 0000, 5])
    my_Sim.load_ml_program()
    my_Sim.execute_program()
    result = my_Sim.get_accumulator()
    assert result == 10
    # my_Sim = [(30, 5), (43,00)]
    # accumulator = 5
    # memory = [0] * 100
    # memory[5] = 5
    # memory, accumulator = execute_my_Sim(my_Sim, memory, accumulator)
    # assert accumulator == 10
    
def test_subtract():
    my_Sim = UVSim()
    my_Sim.set_accumulator(10)
    my_Sim.set_memory(0, 5)
    result = my_Sim.subtract()
    assert result == 5
    
def test_subtract2():
    my_Sim = UVSim()
    my_Sim.set_accumulator(10)
    my_Sim.set_program([3105, 4300, 0000, 0000, 0000, 5])
    my_Sim.load_ml_program()
    my_Sim.execute_program()
    result = my_Sim.get_accumulator()
    assert result == 5
    
def test_execute_my_Sim():
    my_Sim = UVSim()
    my_Sim.set_program([2006, 3006, 3106, 3006, 4300, 0000, 5])
    my_Sim.load_ml_program()
    my_Sim.execute_program()
    result = my_Sim.get_accumulator()
    assert result == 10

def test_execute_my_Sim2():
    my_Sim = UVSim()
    my_Sim.set_memory(5, 10)
    my_Sim.set_memory(10, 5)
    my_Sim.set_program([2005, 3110, 4300, 0000, 0000, 10, 0000, 0000, 0000, 0000, 5])
    my_Sim.load_ml_program()
    my_Sim.execute_program()
    result = my_Sim.get_accumulator()
    assert result == 5
