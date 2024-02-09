import pytest

from main import *

def test_always_passes():
    assert True

# def test_always_fail():
#     assert False

    
def test_load():
    memory = [0] * 100
    memory[0] = 5
    operand = 0
    accumulator = load(operand, memory)
    assert accumulator == 5

def test_neg_load():
    memory = [0] * 100
    memory[0] = -5
    operand = 0
    accumulator = load(operand, memory)
    assert accumulator == -5
    
def test_store():
    memory = [0] * 100
    accumulator = 50
    operand = 0
    store(accumulator, operand, memory)
    assert memory[0] == 50

def test_neg_store():
    memory = [0] * 100
    accumulator = -50
    operand = 0
    store(accumulator, operand, memory)
    assert memory[0] == -50

def test_multiply():
    memory = [0] * 100
    memory[0] = 4
    accumulator = 10
    operand = 0
    result = multiply(accumulator, operand, memory)
    assert result == 40

def test_neg_multiply():
    memory = [0] * 100
    memory[0] = -4
    accumulator = 10
    operand = 0
    result = multiply(accumulator, operand, memory)
    assert result == -40
    
def test_divide():
    memory = [0] * 100
    memory[0] = 4
    accumulator = 10
    operand = 0
    result = divide(accumulator, operand, memory)
    assert result == 2

def test_zero_divide():
    memory = [0] * 100
    memory[0] = 0
    accumulator = 10
    operand = 0
    result = divide(accumulator, operand, memory)
    assert result == 10 

def test_neg_divide():
    memory = [0] * 100
    memory[0] = -4
    accumulator = 10
    operand = 0
    result = divide(accumulator, operand, memory)
    assert result == -3

def test_divide_less_one():
    memory = [0] * 100
    memory[0] = 10
    accumulator = 4
    operand = 0
    result = divide(accumulator, operand, memory)
    assert result == 0
    
def test_branch():
    operand = 5
    result = branch(operand)
    assert result == 5

def test_branch2():
    program = [(40,3), (00,00), (00,00), (20,00), (43,00)]
    memory = [0] * 100
    memory[0] = 10
    accumulator = 0
    memory, accumulator = execute_program(program, memory, accumulator)
    assert accumulator == 10
    
    
def test_branchNeg():
    operand = 20
    pc = 0
    accumulator = -5
    result = branchNeg(accumulator, operand, pc)
    assert result == 20
    
def test_branchNeg2():
    operand = 5
    pc = 0
    accumulator = 5
    result = branchNeg(accumulator, operand, pc)
    assert result == 0

def test_branchZero():
    operand = 25
    pc = 5
    accumulator = 0
    result = branchZero(accumulator, operand, pc)
    assert result == 25
    
def test_branchZero2():
    operand = 5
    pc = 0
    accumulator = 5
    result = branchZero(accumulator, operand, pc)
    assert result == 0
    
def test_read_program():
    file_path = 'programtest.txt'
    program = read_ml_program(file_path)
    assert program == [(10,00), (11,55), (20,00), (31, 55), (32, 66)]
    
def test_read_program2():
    file_path = 'programtest2.txt'
    with pytest.raises(ValueError):
        program = read_ml_program(file_path)
    assert ValueError(f"Command +29938 is more or less than 4 digits. Please correct the program txt file.")
    
def test_add():
    memory = [0] * 100
    memory[0] = 5
    accumulator = 5
    operand = 0
    result = add(accumulator, operand, memory)
    assert result == 10

def test_add2():
    program = [(30, 5), (43,00)]
    accumulator = 5
    memory = [0] * 100
    memory[5] = 5
    memory, accumulator = execute_program(program, memory, accumulator)
    assert accumulator == 10
    
def test_subtract():
    memory = [0] * 100
    memory[0] = 5
    accumulator = 10
    operand = 0
    result = subtract(accumulator, operand, memory)
    assert result == 5
    
def test_subtract2():
    program = [(31, 5), (43,00)]
    accumulator = 10
    memory = [0] * 100
    memory[5] = 5
    memory, accumulator = execute_program(program, memory, accumulator)
    assert accumulator == 5