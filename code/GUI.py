import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
<<<<<<< Updated upstream
from main import *
from execute_program import *
from uvsim import *
from main import *
=======
from execute_program import Execute
>>>>>>> Stashed changes

class SimpleGUI:
    def __init__(self, master, uvsim):
        self.master = master
        self.master.title("UVSIM")
        self.master.geometry("400x400")
        self.uvsim = uvsim
        
<<<<<<< Updated upstream
# Clean is above
=======
        self.label = tk.Label(master, text="Welcome to the UVUSIM! Please select a text file to run:")
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_button.pack()

        self.op_operand_text = tk.Text(master, height=10, width=40)
        self.op_operand_text.pack(pady=10)

        self.memory_text = tk.Text(master, height=10, width=40)
        self.memory_text.pack(pady=10)

        self._pc = 0
        self._op = 0
        self._operand = 0
        self._program = []
        self._file = ""
>>>>>>> Stashed changes

        # self._memory = [0] * 100
        # self._accumulator = 0
        # self._pc = 0
        # self._operand = 0
        # self._program = []
        # self._file = ""
#clean is below
    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.operations = [int(line.strip()) for line in file]
                return self.operations
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Info", "No file selected.")

    def process_next_operation(self, value):
        if self.operations:
            if self._op not in (40, 41 , 41):
                    self._pc += 1
            if self._op > 99:
                messagebox.showerror("Error", "Program too long. Program Halted.")
            self._op, self._operand = self.operations.pop(0)
<<<<<<< Updated upstream
            return value
=======
            Execute.execute(self._op, self._operand, self._pc, self.uvsim, self)
>>>>>>> Stashed changes

    # def execute_program(self):
    #     if self._op == 10:  # read
    #         self.read_input()
    #     elif self._op == 11:  # write
    #         self.write()
    #     elif self._op == 20:  # load
    #         self._accumulator = self.load()
    #     elif self._op == 21: #store
    #         self.store()
    #     elif self._op == 30: #add
    #         self._accumulator = self.add()
    #     elif self._op == 31: #subtract
    #         self._accumulator = self.subtract()
    #     elif self._op == 32: #divide
    #         self._accumulator = self.divide()
    #     elif self._op == 33: #multiply
    #         self._accumulator = self.multiply()
    #     elif self._op == 40: #branch
    #         self._pc = self.branch()
    #     elif self._op == 41: #branchNeg
    #         self._pc = self.branchNeg()
    #     elif self._op == 42: #branchZero
    #         self._pc = self.branchZero()
    #     elif self._op == 43: #halt
    #         messagebox.showinfo("Halt Operation", f"Result: {self._accumulator}")
<<<<<<< Updated upstream
    def read_input(self, operand):
=======

    def read_input(self):
>>>>>>> Stashed changes
        entry_window = tk.Toplevel(self.master)
        entry_window.title("Enter Value")
        entry_window.geometry("300x100")

        def submit():
            try:
                value = int(entry.get())
<<<<<<< Updated upstream
=======
                self.uvsim._memory.store(self._operand, value)
>>>>>>> Stashed changes
                entry_window.destroy()
                self.handle_input(value)  # Call the callback function with the input value
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")

        entry_label = tk.Label(entry_window, text=f"Enter a number for memory location {operand}:")
        entry_label.pack(pady=5)
        entry = tk.Entry(entry_window)
        entry.pack(pady=5)
        submit_button = tk.Button(entry_window, text="Submit", command=submit)
        submit_button.pack(pady=5)
        
    def handle_input(self, value):
    # You can call your processing function here or do any further processing
        self.process_next_operation(value)

<<<<<<< Updated upstream
    def process_next_operation(self, value):
        # This function should handle the next operation after receiving the input value
        print("Input value:", value)

    def write(self, value):
        # self._accumulator = value  # Update accumulator after writing
        messagebox.showinfo(f"Write Operation: {value}")
        # self.process_next_operation()  # Process the next operation after writing


    

#Elephant Code Graveyard
# Clean is above

        # self._memory = [0] * 100
        # self._accumulator = 0
        # self._pc = 0
        # self._operand = 0
        # self._program = []
        # self._file = ""
#     def load(self):
#         value = self._memory[self._operand]
#         self._accumulator = value  # Update accumulator after loading
#         messagebox.showinfo("Load Operation", f"Loaded value: {value}")
#         self.process_next_operation()  # Process the next operation after loading

#     def store(self):
#         value = self._memory[self._operand] = self._accumulator
#         self._accumulator = value  # Update accumulator after storing
#         messagebox.showinfo("Store Operation", f"Stored value: {value}")
#         self.process_next_operation()  # Process the next operation after storing

#     def add(self):
#         value = self._accumulator + self._memory[self._operand]
#         self._accumulator = value  # Update accumulator after adding
#         messagebox.showinfo("Add Operation", f"Added value: {value}")   
#         self.process_next_operation()  # Process the next operation after adding

#     def subtract(self):
#         value = self._accumulator - self._memory[self._operand]
#         self._accumulator = value  # Update accumulator after subtracting
#         messagebox.showinfo("Subtract Operation", f"Subtracted value: {value}")
#         self.process_next_operation()  # Process the next operation after subtracting

#     def divide(self):
#         if self._memory[self._operand] == 0:
#             messagebox.showinfo("Error", "Cannot divide by zero.")
#         value = self._accumulator // self._memory[self._operand]
#         self._accumulator = value  # Update accumulator after dividing
#         messagebox.showinfo("Divide Operation", f"Divided value: {value}")
#         self.process_next_operation()  # Process the next operation after dividing

#     def multiply(self):
#         value = self._accumulator * self._memory[self._operand]
#         self._accumulator = value  # Update accumulator after multiplying
#         messagebox.showinfo("Multiply Operation", f"Multiplied value: {value}")
#         self.process_next_operation()  # Process the next operation after multiplying

#     def branch(self):
#         value = self._operand
#         self._accumulator = value  # Update accumulator after branching
#         messagebox.showinfo("Branch Operation", f"Branching to: {value}")
#         self.process_next_operation()  # Process the next operation after branching
=======
    def write(self):
        value = self.uvsim._memory.load(self._operand)
        messagebox.showinfo("Write Operation", f"Value at memory location {self._operand}: {value}")
        self.process_next_operation()  # Process the next operation after writing

    def load(self, value):
        messagebox.showinfo("Load Operation", f"Loaded value: {value}")
        self.process_next_operation()  # Process the next operation after loading

    def store(self, value):
        # Update accumulator after storing
        messagebox.showinfo("Store Operation", f"Stored value: {value}")
        self.process_next_operation()  # Process the next operation after storing

    def add(self, value): # Update accumulator after adding
        messagebox.showinfo("Add Operation", f"Added value: {value}")   
        self.process_next_operation()  # Process the next operation after adding

    def subtract(self, value):
        messagebox.showinfo("Subtract Operation", f"Subtracted value: {value}")
        self.process_next_operation()  # Process the next operation after subtracting

    def divide(self, value):
        messagebox.showinfo("Divide Operation", f"Divided value: {value}")
        self.process_next_operation()  # Process the next operation after dividing

    def multiply(self, value):
        messagebox.showinfo("Multiply Operation", f"Multiplied value: {value}")
        self.process_next_operation()  # Process the next operation after multiplying

    def branch(self, value):
        messagebox.showinfo("Branch Operation", f"Branching to: {value}")
        self._pc = value
        self.process_next_operation()  # Process the next operation after branching

    def branchNeg(self, value):
        self._pc = value
        messagebox.showinfo("Branch Negative Operation", f"Branching to: {self._pc}")
        self.process_next_operation()  # Process the next operation after branching negative
        # print(f"self._pc after branching negative: {self._pc}")
>>>>>>> Stashed changes

#     def branchNeg(self):
#         # print(f"self._pc before branching negative: {self._pc}")
#         if self._accumulator < 0:
#             value = self._operand
#         else:
#             if self._pc is None:
#                 self._pc = 0
#             value = self._pc + 1
#         self._accumulator = value  # Update accumulator after branching negative
#         messagebox.showinfo("Branch Negative Operation", f"Branching to: {self._operand}")
#         self.process_next_operation()  # Process the next operation after branching negative
#         # print(f"self._pc after branching negative: {self._pc}")

<<<<<<< Updated upstream
#     def branchZero(self):
#         if self._accumulator == 0:
#             value = self._operand
#         else:
#             value = self._pc + 1
#         self._accumulator = value  # Update accumulator after branching zero
#         messagebox.showinfo("Branch Zero Operation", f"Branching to: {self._operand}")
#         self.process_next_operation()  # Process the next operation after branching zero

# def main():
#     root = tk.Tk()
#     app = SimpleGUI(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()
=======
    def halt(self):
        messagebox.showinfo("Halt Operation", f"Result: {self.uvsim.get_accumulator()}")
        
>>>>>>> Stashed changes
