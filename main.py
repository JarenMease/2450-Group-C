from execute_program import UVSim

def main():
    my_Sim = UVSim()
    my_Sim.read_ml_program()
    my_Sim.load_ml_program()
    my_Sim.execute_program()

if __name__ == "__main__":
    main()
    
