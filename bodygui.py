from tkinter import *
from tkinter import ttk
import htmlgenerator

class Window():

    def __init__(self, master):

        def submit():
            newtext = self.body.get(1.0, END)
            htmlgenerator.createPage(newtext)
            self.body.delete(1.0, END)
            self.body.insert(1.0, 'Web page created.  If you would like to change the body again, please enter new text here.')

        self.frame = ttk.Frame(master, relief = RAISED, padding=10)
        self.frame.pack()

        ttk.Label(self.frame, text = 'Enter new body text here:').grid(row = 0, column = 0)
        self.body = Text(self.frame, width = 50, height = 10)
        self.body.grid(row = 1, column = 0, columnspan = 2)

        self.submitbutton = ttk.Button(self.frame, text = 'Create Page', command = submit)
        self.submitbutton.grid(row = 2, column = 1)




def main():

    root = Tk()
    root.wm_title("Webpage Text Entry")
    win = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
