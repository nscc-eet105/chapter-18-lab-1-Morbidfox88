#Chad Collard
#Chapter 18 GUI
#7/26/2025



import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Feet and Inches Converter")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Label for the program 
        self.convert_label = tkinter.Label(self.top_frame, text="Feet and Inches Converter", borderwidth=1)

        # Input fields and labels for Feet
        self.feet_label = tkinter.Label(self.top_frame, text="Feet")
        self.feet_entry = tkinter.Entry(self.top_frame, width=5)

        # Input fields and labels for Inches
        self.inches_label = tkinter.Label(self.top_frame, text="Inches")
        self.inches_entry = tkinter.Entry(self.top_frame, width=5)

        # Pack the inputs
        self.convert_label.pack(side="top")
        self.feet_label.pack(side="left")
        self.feet_entry.pack(side="left")
        self.inches_label.pack(side="left")
        self.inches_entry.pack(side="left")

        # Result label 
        self.result_label = tkinter.Label(self.bottom_frame, text="Inches: ")
        self.result_label.pack(side="top", pady=5)

        # Convert and Exit buttons
        self.convert_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert_feet_inches_to_inches)
        self.exit_button = tkinter.Button(self.bottom_frame, text="Exit", command=self.main_window.destroy)

        # Pack the buttons
        self.convert_button.pack(side="left")
        self.exit_button.pack(side="right")

        # Pack the frames into the main window
        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="bottom")

        tkinter.mainloop()

    def convert_feet_inches_to_inches(self):
            feet = float(self.feet_entry.get())
            inches = float(self.inches_entry.get())
            total_inches = feet * 12 + inches
            self.result_label.config(text=f"Inches: {total_inches:.2f}")
        

if __name__ == "__main__":
    my_gui = MyGUI()
