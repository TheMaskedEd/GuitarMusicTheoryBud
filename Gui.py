#The following code uses tkinter and PILLOW modules
#install guide to pillow https://pillow.readthedocs.io/en/stable/installation.html

import main
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Guitar app')
root.maxsize(700, 350)
root.config(bg="white")

a_frame = Frame(root, width=650, height=50, bg='light grey')
a_frame.grid(row=0, column=0, padx=10, pady=5)

neck = Image.open("neck.png")
image = ImageTk.PhotoImage(neck)

f_frame = Label(root,image=image,borderwidth=0)
f_frame.image = image
f_frame.grid(row=1, column=0,padx=10, pady=10)

b_frame = Frame(root, width=650, height=100, bg='grey')
b_frame.grid(row=2, column=0, padx=10, pady=5)

c_frame = Frame(root, width=650, height=50, bg='light grey')
c_frame.grid(row=3, column=0, padx=10, pady=5)

options =["standard",
        "drop d",
        "drop c",
        "B standard"]

def Button(func):
   match func:
      case "tune":
         main.tunning(a1clicked.get())
      case"tune":
         main.tunning(a1clicked.get())
      case "tune":
         main.tunning(a1clicked.get())
      case "tune":
         main.tunning(a1clicked.get())
      case "tune":
         main.tunning(a1clicked.get())
      case "tune":
         main.tunning(a1clicked.get())


clicked = StringVar(root)
clicked.set("null")
a1clicked = StringVar(root)
a1clicked.set("standard")
a1clicked1 = StringVar(root)
a1clicked1.set("A")
a1clicked2 = StringVar(root)
a1clicked2.set("Major")
a1clicked3 = StringVar(root)
a1clicked3.set("pick")

a1_text = Label(a_frame, text = "Tuning")
a1_text.grid(row=0, column=0, padx=5, pady=5)
a1_Menu = OptionMenu(a_frame, a1clicked , *options)
a1_Menu.grid(row=0, column=1, padx=5, pady=5)
a1_Button = Button(a_frame, text ="enter", command=Button("tune"))
a1_Button.grid(row=0, column=2, padx=5, pady=5)
a1_text = Label(a_frame, text = "Scales")
a1_text.grid(row=0, column=3, padx=5, pady=5)
a1_Menu1 = OptionMenu(a_frame, a1clicked1 , *options)
a1_Menu1.grid(row=0, column=4, padx=5, pady=5)
a1_Menu2 = OptionMenu(a_frame, a1clicked2 , *options)
a1_Menu2.grid(row=0, column=5, padx=5, pady=5)
a1_Button1 = Button(a_frame, text ="enter", command = Button("tune"))
a1_Button1.grid(row=0, column=6, padx=5, pady=5)
a1_text = Label(a_frame, text = "Ask Jeeves")
a1_text.grid(row=0, column=7, padx=5, pady=5)
a1_Menu3 = OptionMenu(a_frame, a1clicked3 , *options)
a1_Menu3.grid(row=0, column=8, padx=5, pady=5)
a1_Button2 = Button(a_frame, text ="enter", command = Button("tune"))
a1_Button2.grid(row=0, column=9, padx=5, pady=5)


b1l_frame = Frame(b_frame, width=200, height=70, bg='light grey')
b1l_frame.grid(row=1, column=0, padx=5, pady=5)
b1t_text = Label(b_frame, text = "Custom Chord")
b1t_text.grid(row=0, column=0, padx=5, pady=5)
b2l_frame = Frame(b_frame, width=200, height=70, bg='light grey')
b2l_frame.grid(row=1, column=1, padx=5, pady=5)
b2t_text = Label(b_frame, text = "Chord Menu")
b2t_text.grid(row=0, column=1, padx=5, pady=5)
b1str6_text = Label(b1l_frame, text = "string 6 Note")
b1str6_text.grid(row=1, column=0, padx=5, pady=5)
b1str6_input = Entry(b1l_frame, width = 5)
b1str6_input.grid(row=1, column=1, padx=5, pady=5)
b1str5_text = Label(b1l_frame, text = "string 5 Note")
b1str5_text.grid(row=2, column=0, padx=5, pady=5)
b1str5_input = Entry(b1l_frame, width = 5)
b1str5_input.grid(row=2, column=1, padx=5, pady=5)
b1str4_text = Label(b1l_frame, text = "string 4 Note")
b1str4_text.grid(row=3, column=0, padx=5, pady=5)
b1str4_input = Entry(b1l_frame, width = 5)
b1str4_input.grid(row=3, column=1, padx=5, pady=5)
b1str3_text = Label(b1l_frame, text = "string 3 Note")
b1str3_text.grid(row=1, column=2, padx=5, pady=5)
b1str3_input = Entry(b1l_frame, width = 5)
b1str3_input.grid(row=1, column=3, padx=5, pady=5)
b1str2_text = Label(b1l_frame, text = "string 2 Note")
b1str2_text.grid(row=2, column=2, padx=5, pady=5)
b1str2_input = Entry(b1l_frame, width = 5)
b1str2_input.grid(row=2, column=3, padx=5, pady=5)
b1str1_text = Label(b1l_frame, text = "string 1 Note")
b1str1_text.grid(row=3, column=2, padx=5, pady=5)
b1str2_input = Entry(b1l_frame, width = 5)
b1str2_input.grid(row=3, column=3, padx=5, pady=5)
b2_text = Label(b2l_frame, text = "Root Note")
b2_text.grid(row=0, column=0, padx=5, pady=5)
b2_Menu = OptionMenu(b2l_frame, clicked , *options)
b2_Menu.grid(row=0, column=1, padx=5, pady=5)
b2_text1 = Label(b2l_frame, text = "Chord type")
b2_text1.grid(row=1, column=0, padx=5, pady=5)
b2_Menu1 = OptionMenu(b2l_frame, clicked , *options)
b2_Menu1.grid(row=1, column=1, padx=5, pady=5)


c1_Button = Button(c_frame, text ="Arppegiate", command = Button("tune"))
c1_Button.grid(row=0, column=0, padx=10, pady=5)
c1_Button1 = Button(c_frame, text ="Scale Check", command = Button("tune"))
c1_Button1.grid(row=0, column=1, padx=10, pady=5)
c1_Button2 = Button(c_frame, text ="Chord View", command = Button("tune"))
c1_Button2.grid(row=0, column=2, padx=10, pady=5)


root.mainloop()