from execute_program import *
from uvsim import *
from GUI import *

def main():
    my_Sim = execute_program()
    root = tk.Tk()
    my__gui = SimpleGUI(root)
    my_Sim._memory.load_ml_program(my__gui.select_file())
    my_Sim.execute(my__gui)
    root.mainloop()


if __name__ == "__main__":
    main()


# elephant code Graveyard
    # my_Sim.read_ml_program() #should rename to read_ml_program BW Need to go to the front end