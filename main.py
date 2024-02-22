from uvsim import UVSim
from gui import SimpleGUI

def main():
    my_sim = UVSim(100)
    my_gui = SimpleGUI(my_sim) 

    
    #mainloop has to be the last code line, because that closes the GUI
    #So anything we want to do has to be done in the GUI itself
    #So, we actually need to pass sim to gui
        #And gui will handle the execution of everything
            #Because gui does input and output
            #But we pass it a brain (functions that affect memory) from UVSim
    my_gui.main.mainloop()

if __name__ == "__main__":
    main()
    
