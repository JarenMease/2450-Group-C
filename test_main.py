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
    
    
def test_store():
    memory = [0] * 100
    accumulator = 50
    operand = 0
    store(accumulator, operand, memory)
    assert memory[0] == 50

def test_multiply():
    memory = [0] * 100
    memory[0] = 4
    accumulator = 10
    operand = 0
    result = multiply(accumulator, operand, memory)
    assert result == 40
    
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
    
def test_branchNeg():
    operand = -5
    pc = 0
    result = branchNeg(operand, pc)
    assert result == -5
    
def test_branchNeg2():
    operand = 5
    pc = 0
    result = branchNeg(operand, pc)
    assert result == 0

def test_branchZero():
    operand = 0
    pc = 0
    result = branchZero(operand, pc)
    assert result == 0
    
def test_branchZero2():
    operand = 5
    pc = 0
    result = branchZero(operand, pc)
    assert result == 0
    
def test_read_program():
    file_path = 'programtest.txt'
    program = read_program(file_path)
    assert program == [(78,00), (79,00), (80,00), (47, 55), (57, 66)]
    
def test_memory():
    memory = [0] * 100
    memory[0] = 5
    assert memory[0] == 5
