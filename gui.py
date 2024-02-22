import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class SimpleGUI:
    def __init__(self, sim):
        self.main = tk.Tk()
        self.main.title("UVSIM")
        self.main.geometry("500x500")
        self.sim = sim
        
        self.label = tk.Label(self.main, text="Welcome to the UVUSIM! Please select a text file to run:")
        self.label.pack(pady=10)
        
        self.file_button = tk.Button(self.main, text="Select File", command=self.select_file)
        self.file_button.pack()

        self.memory_text = tk.Text(self.main, height=10, width=40)
        self.memory_text.pack(pady=10)

        self._program = []

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        self._program.append(int(line.strip()))
                #load program into sim on button click
                self.load_file()
                #execute program in sim
                self.execute_program()
                #print accumulator
                self.final_output()
                #exit
                self.main.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Info", "No file selected.")
    
    def load_file(self):
        self.sim.load_ml_program(self._program)
    
    def execute_program(self):
        sim = self.sim
        sim._pc = 0
        while sim._pc < len(sim._memory):

            sim._op = sim._memory[sim._pc] // 100
            sim._operand = sim._memory[sim._pc] % 100  

            match sim._op:
              case 10: #read
                  self.read() # BW GUI.READ THIS HAS TO BE DONE IN FRONT END
              case 11: #write
                  self.write() # BW GUI.WRITE THIS HAS TO BE DONE IN FRONT END
              case 20: #load
                  sim._accumulator = sim.load()
              case 21: #store
                  sim.store()
              case 30: #add
                  sim._accumulator = sim.add(sim._accumulator, sim.load())
              case 31: #subtract
                  sim._accumulator = sim.subtract(sim._accumulator, sim.load())
              case 32: #divide
                  sim._accumulator = sim.divide(sim._accumulator, sim.load())
              case 33: #multiply
                  sim._accumulator = sim.multiply(sim._accumulator, sim.load())
              case 40: #branch
                  sim._pc = sim.branch(sim._operand)
              case 41: #branchNeg
                  sim._pc = sim.branch_neg(sim._accumulator, sim._operand, sim._pc)
              case 42: #branchZero
                  sim._pc = sim.branch_zero(sim._accumulator, sim._operand, sim._pc)
              case 43: #halt
                  my_bool = sim.halt()
                  if my_bool:
                      break
            if sim._op not in (40, 41, 42):
              sim._pc += 1
        if sim._pc > 99:
            messagebox.showerror("Error", "Program too long.")
    
    def final_output(self):
        messagebox.showinfo("Accumulator Value:", f"{self.sim._accumulator}")  

    def read(self):
        entry_window = tk.Toplevel(self.main)
        entry_window.title("Enter Value")
        entry_window.geometry("300x100")

        def submit():
            try:
                value = int(entry.get())
                self.sim._memory[self.sim._operand] = value
                entry_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")

        entry_label = tk.Label(entry_window, text=f"Enter a number for memory location {self.sim._operand}:")
        entry_label.pack(pady=5)
        entry = tk.Entry(entry_window)
        entry.pack(pady=5)
        submit_button = tk.Button(entry_window, text="Submit", command=submit)
        submit_button.pack(pady=5)

        #this is vital when waiting for user input
        entry_window.wait_window()
    
    def write(self):
        value = self.sim._memory[self.sim._operand]
        messagebox.showinfo("Write Operation", f"Value at memory location {self.sim._operand}: {value}")


