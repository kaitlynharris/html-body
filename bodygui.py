from tkinter import *
from tkinter import ttk
import htmlgenerator

def makeWindow():

    def submit():
        newtext = body.get(1.0, END)
        htmlgenerator.createPage(newtext)
        body.delete(1.0, END)
        body.insert(1.0, 'Web page created.  If you would like to change the body again, please enter new text here.')

    root = Tk()
    root.wm_title("Webpage Text Entry")

    frame = ttk.Frame(root, relief = RAISED, padding=10)
    frame.pack()

    ttk.Label(frame, text = 'Enter new body text here:').grid(row = 0, column = 0)
    body = Text(frame, width = 50, height = 10)
    body.grid(row = 1, column = 0, columnspan = 2)

    submitbutton = ttk.Button(frame, text = 'Create Page', command = submit)
    submitbutton.grid(row = 2, column = 1)

    return root

def test():
    pass

def main():

    root = makeWindow()
    root.mainloop()


if __name__ == '__main__':
    main()
