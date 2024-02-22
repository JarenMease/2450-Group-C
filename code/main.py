from execute_program import *
from uvsim import *
from GUI import *
<<<<<<< Updated upstream

def main():
    my_Sim = execute_program()
    root = tk.Tk()
    my__gui = SimpleGUI(root)
    my_Sim._memory.load_ml_program(my__gui.select_file())
    my_Sim.execute(my__gui)
    root.mainloop()

=======
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def main():
    my_Sim = UVSim()
    root = tk.Tk()
    my_program = SimpleGUI(root, my_Sim)
    my_program.select_file()
    root.mainloop()
>>>>>>> Stashed changes

if __name__ == "__main__":
    main()


# elephant code Graveyard
    # my_Sim.read_ml_program() #should rename to read_ml_program BW Need to go to the front end