from execute_program import *
from uvsim import *

def main():
    my_Sim = execute_program()
    my_Sim.read_ml_program() #should rename to read_ml_program BW Need to go to the front end
    my_Sim._memory.load_ml_program(my_Sim._program)
    my_Sim.execute()

if __name__ == "__main__":
    main()
    
