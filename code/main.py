from execute_program import *
from uvsim import *
from GUI import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def main():
    my_Sim = UVSim()
    root = tk.Tk()
    my_program = SimpleGUI(root, my_Sim)
    my_program.select_file()
    root.mainloop()

if __name__ == "__main__":
    main()


# elephant code Graveyard
    # my_Sim.read_ml_program() #should rename to read_ml_program BW Need to go to the front end