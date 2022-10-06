from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Password_Generator


class MyProgram:
    def __init__(self, root1):
        self.label1 = Label(root1, text="Size of Password")
        self.label2 = Label(root1, text='''Password Restrictions: 

        A. At least one uppercase
        B. At least one number
        C. At least one special character
        
        Example: ABC, AB, CB''')
        self.label3 = Label(root1, text="Your Password")

        self.e1 = Entry()
        self.e2 = Entry()
        self.e3 = Entry()
    
        self.label1.place(x=60,y=50)
        self.e1.place(x=200,y=50)
        self.label2.place(x=10,y=100)
        self.e2.place(x=200,y=100)
        self.label3.place(x=100, y=250)
        self.e3.place(x=200,y=250)

        self.button = Button(root1, text="Generate Password", command=self.generator)
        self.button.place(x=240,y=150)

    def generator(self):
        self.error()
        self.e3.delete(0,'end')
        size1 = int(self.e1.get())
        restrictions = str(self.e2.get())
        x = Password_Generator.restrictions(restrictions)
        result = Password_Generator.codeGenerator(size1, x)
        self.e3.insert(END, str(result))
    
    def error(self):
        size1 = int(self.e1.get())
        restrictions = str(self.e2.get())
        x = Password_Generator.error(size1, restrictions)
        if x[0] == True:
            messagebox.showerror("Error", x[1])


root = Tk()
frame = MyProgram(root)
root.title("Sona Keshishyan's Secure Password Generator!")
root.geometry("420x300")
root.mainloop()






