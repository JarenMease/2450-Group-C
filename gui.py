import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from execute_program import Execute

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
                #execute program with Execute class
                Execute.execute_program(self.sim, self)
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

    def too_long(self):
        messagebox.showerror("Error", "Program too long.")
