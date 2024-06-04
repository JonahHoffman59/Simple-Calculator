# Name: Jonah Hoffman
# Date: February 3, 2023
# Desription: A calculator.

from tkinter import *
from button_data import button_data

WIDTH = 400
HEIGHT = 650

class MainGUI(Frame):
    
    rows = 7
    cols = 4

    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        # parent.attributes("-fullscreen", True)
        self.setupGUI()


    def setupGUI(self):
        # display
        self.display = Label(
            self,       # MainGUI class is parent of this label
            text="",
            anchor=E,
            bg="white",
            fg="black",
            height=1,
            font = ("texGyreAdventor", 50)  # tuple: (font name, size)
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky=NSEW)

        # configuring rows and columns
        for row in range(MainGUI.rows):
            Grid.rowconfigure(self, row, weight=1)

        for col in range(MainGUI.cols):
            Grid.columnconfigure(self, col, weight=1)


        # make buttons
        for button in button_data:
            self.make_button(button["row"], button["col"], button["value"])


        # pack the GUI
        self.pack(fill=BOTH, expand=1)


    def make_button(self, row, col, value):
        column_span = 1
        bg_color = "#dddddd"
        if value == "=":
            bg_color = "blue"
            column_span = 2
        if value in ['(', ')', 'AC', '**', '+', '-', '*', '/']:
            bg_color = "#999999"
        button = Button(
            self,
            font = ("TexGyreAdventor", 30),
            text = value,
            fg="black",
            bg=bg_color,    # for windows
            highlightbackground=bg_color,   # for macs (windows too?)
            borderwidth=0,
            highlightthickness=0,
            width=5,
            activebackground = "white",
            command=lambda: self.process(value)
        )
        button.grid(row=row, column=col, sticky=NSEW, columnspan=column_span)

    def clear_display(self):
        self.display["text"] = ""

    def set_display(self, value):
        self.display["text"] = value

    def append_display(self, value):
        self.display["text"] += value

    def evaluate(self):
            expression = self.display["text"]
            
            # evaluate expression in display
            try:
                # do this until it hits an error
                result = str(eval(expression))
                self.set_display(result)

            except:
                # if try part hits an error, do this
                self.set_display("ERROR")



    def process(self, button):
        
        if self.display["text"] == "ERROR":
            self.clear_display()

        if button == "<--":
            # backspace
            self.display["text"] = self.display["text"][0:len(self.display["text"])-1]
        
        elif button == "AC":
            # clear the display
            self.clear_display()

        elif button == "=":
            self.evaluate()

        else:
            # append to the display
            self.append_display(button)

        # adds functionality of backspace
        if len(self.display["text"]) >= 14:
            self.display["text"] = self.display["text"][0:11] + "..."

# Main
window = Tk()
window.title("The Reckoner")
window.geometry(f"{WIDTH}x{HEIGHT}")

p = MainGUI(window)
window.mainloop()
