import pytest
from main import *
from executeProgram import *

def test_always_passes():
    assert True

# def test_always_fail():
#     assert False
   
def test_load():
    program = Program()
    program.set_memory(0, 10)
    accumulator = program.load()
    assert accumulator == 10

def test_neg_load():
    program = Program()
    program.set_memory(0, -5)
    accumulator = program.load()
    assert accumulator == -5
    
def test_store():
    program = Program()
    program.set_memory(0, 10)
    program.set_accumulator(50)
    program.store()
    storing = program.get_memory(0)
    assert storing == 50

def test_neg_store():
    program = Program()
    program.set_memory(0, -10)
    program.set_accumulator(-50)
    program.store()
    storing = program.get_memory(0)
    assert storing == -50

def test_multiply():
    program = Program()
    program.set_accumulator(10)
    program.set_memory(0, 5)
    result = program.multiply()
    assert result == 50

def test_neg_multiply():
    program = Program()
    program.set_accumulator(-10)
    program.set_memory(0, 5)
    result = program.multiply()
    assert result == -50
    
def test_divide():
    program = Program()
    program.set_accumulator(10)
    program.set_memory(0, 5)
    result = program.divide()
    assert result == 2

def test_zero_divide():
    program = Program()
    program.set_accumulator(10)
    program.set_memory(0, 0)
    result = program.divide()
    assert result == 10

def test_neg_divide():
    program = Program()
    program.set_accumulator(-10)
    program.set_memory(0, 5)
    result = program.divide()
    assert result == -2

def test_divide_less_one():
    program = Program()
    program.set_accumulator(1)
    program.set_memory(0, 5)
    result = program.divide()
    assert result == 0
    
def test_branch():
    program = Program()
    program.set_operand(5)
    result = program.branch()
    assert result == 5
    
def test_branch2():
    program = Program()
    program.set_pc(10)
    program.set_operand(15)
    result = program.branch()
    assert result == 15
        
def test_branchNeg():
    program = Program()
    program.set_operand(20)
    program.set_accumulator(-5)
    result = program.branchNeg()
    assert result == 20
    
def test_branchNeg2():
    program = Program()
    program.set_operand(5)
    program.set_accumulator(5)
    result = program.branchNeg()
    assert result == 0

def test_branchZero():
    program = Program()
    program.set_operand(25)
    program.set_pc(5)
    result = program.branchZero()
    assert result == 25
    
def test_branchZero2():
    program = Program()
    program.set_accumulator(5)
    result = program.branchZero()
    assert result == 0
    
def test_add():
    program = Program()
    program.set_accumulator(5)
    program.set_memory(0, 5)
    result = program.add()
    assert result == 10

def test_add2():
    program = Program()
    program.set_accumulator(5)
    program.set_memory(5, 5)
    program.set_program([(30, 5), (43,00)])
    program.execute_program()
    result = program.get_accumulator()
    assert result == 10
    # program = [(30, 5), (43,00)]
    # accumulator = 5
    # memory = [0] * 100
    # memory[5] = 5
    # memory, accumulator = execute_program(program, memory, accumulator)
    # assert accumulator == 10
    
def test_subtract():
    program = Program()
    program.set_accumulator(10)
    program.set_memory(0, 5)
    result = program.subtract()
    assert result == 5
    
def test_subtract2():
    program = Program()
    program.set_accumulator(10)
    program.set_memory(5, 5)
    program.set_program([(31, 5), (43,00)])
    program.execute_program()
    result = program.get_accumulator()
    assert result == 5
    
def test_execute_program():
    program = Program()
    program.set_memory(5, 5)
    program.set_program([(20, 5), (30, 5), (43, 00)])
    program.execute_program()
    result = program.get_accumulator()
    assert result == 10

def test_execute_program2():
    program = Program()
    program.set_memory(5, 10)
    program.set_memory(10, 5)
    program.set_program([(20, 5), (31, 10), (43, 00)])
    program.execute_program()
    result = program.get_accumulator()
    assert result == 5