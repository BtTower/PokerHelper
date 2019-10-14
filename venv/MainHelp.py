from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("Poker Helper")

        self.pack(fill=BOTH, expand=1)

        #quitButton = Button(self, text="Quit", command=self.my_function)
        #quitButton.place(x=0,y=0)

        myMenu = Menu(self.master)
        self.master.config(menu = myMenu)

        file = Menu(myMenu)

        file.add_command(label="Exit", command=self.my_function)
        file.add_command(label="2ndCommand")

        myMenu.add_cascade(label="File", menu = file)

        edit = Menu(myMenu)
        edit.add_command(label="undo")
        edit.add_command(label="Show image", command=self.show_Image)
        edit.add_command(label="SHOOOW text", command=self.show_text)


        myMenu.add_cascade(label="Ranges", menu = edit)



    def my_function(self):
        exit()

    def show_Image(self):
        load = Image.open("utg-17.png")
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def show_text(self):
        text = Label(self, text="Hello world")
        text.pack()



root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
