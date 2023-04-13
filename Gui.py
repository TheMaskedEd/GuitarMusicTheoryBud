#The following code uses tkinter and PILLOW modules
#install guide to pillow https://pillow.readthedocs.io/en/stable/installation.html

import main
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Guitar app')
root.maxsize(700, 350)
root.config(bg="white")

#row 1
a_frame = Frame(root, width=650, height=50, bg='light grey')
a_frame.grid(row=0, column=0, padx=10, pady=5)

#guitar neck
neck = Image.open("neck.png")
image = ImageTk.PhotoImage(neck)

#row 2
f_frame = Label(root,image=image,borderwidth=0)
f_frame.image = image
f_frame.grid(row=1, column=0,padx=10, pady=10)

#row 3
b_frame = Frame(root, width=650, height=100, bg='grey')
b_frame.grid(row=2, column=0, padx=10, pady=5)

#row 4
c_frame = Frame(root, width=650, height=50, bg='light grey')
c_frame.grid(row=3, column=0, padx=10, pady=5)

#option menus
options =["standard",
        "drop d",
        "drop c",
        "B standard"]
options1 = ['C',
            'C#',
            'D',
            'D#',
            'E',
            'F',
            'F#',
            'G',
            'G#',
            'A',
            'A#',
            'B']
options2 =["major",
        "minor",
        "dorian",
        "phrygian",
        "minor pentatonic",
        "major pentatonic",
        "harmonic minor",
        "mixolydian",
        "minor blues",
        "locrian",
        "lydian"]
options3 = ["pick"]
options4 = ["major","minor"]


#change
#button functions are present here they are used so that when app is started they dont all activate at once
def Tune():
   main.tunning(a1clicked.get())
def jeeves():
   print(main.jeeves(a1clicked3.get()))
def scale():
    main.setkey(main.getnotes(a1clicked1.get(), a1clicked2.get()))
def Arp():
    chordAry = [b1str6_input.get(), b1str5_input.get(), b1str4_input.get(), b1str3_input.get(), b1str2_input.get(),
                b1str1_input.get()]
    print(chordAry)
    main.Arpeggiate(chordAry)
def Check():
    chordAry = [b1str6_input.get(), b1str5_input.get(), b1str4_input.get(), b1str3_input.get(), b1str2_input.get(),
                b1str1_input.get()]

    print(main.scalecheck(chordAry))
def Chorddict():
    chord =(main.ChordDict(b2clicked.get(),b2clicked1.get()))
    b1str6.set(chord[0])
    b1str5.set(chord[1])
    b1str4.set(chord[2])
    b1str3.set(chord[3])
    b1str2.set(chord[4])
    b1str1.set(chord[5])

def Cview():
    chordAry = [b1str6_input.get(), b1str5_input.get(), b1str4_input.get(), b1str3_input.get(), b1str2_input.get(),
                b1str1_input.get()]
    main.chordView(chordAry)
def hellocallback():
    print("hello this button is under construction")

#dropdown sets and var holders for row 2
clicked = StringVar()
clicked.set("null")
a1clicked = StringVar()
a1clicked.set("standard")
a1clicked1 = StringVar()
a1clicked1.set("A")
a1clicked2 = StringVar()
a1clicked2.set("major")
a1clicked3 = StringVar()
a1clicked3.set("pick")

#string input sets and var holders for row 2
b1str6 = StringVar()
b1str6.set('')
b1str5 = StringVar()
b1str5.set('')
b1str4 = StringVar()
b1str4.set('')
b1str3 = StringVar()
b1str3.set('')
b1str2 = StringVar()
b1str2.set('')
b1str1 = StringVar()
b1str1.set('')

#chord dictionary sets and var holders for row 3
b2clicked = StringVar()
b2clicked.set("Root")
b2clicked1 = StringVar()
b2clicked1.set("Type")

#row 1 columss grids and other settings
a1_text = Label(a_frame, text = "Tuning")
a1_text.grid(row=0, column=0, padx=5, pady=5)
a1_Menu = OptionMenu(a_frame, a1clicked , *options)
a1_Menu.grid(row=0, column=1, padx=5, pady=5)
a1_Button = Button(a_frame, text ="enter", command=Tune)
a1_Button.grid(row=0, column=2, padx=5, pady=5)
a1_text = Label(a_frame, text = "Scales")
a1_text.grid(row=0, column=3, padx=5, pady=5)
a1_Menu1 = OptionMenu(a_frame, a1clicked1 , *options1)
a1_Menu1.grid(row=0, column=4, padx=5, pady=5)
a1_Menu2 = OptionMenu(a_frame, a1clicked2 , *options2)
a1_Menu2.grid(row=0, column=5, padx=5, pady=5)
a1_Button1 = Button(a_frame, text ="enter", command = scale)
a1_Button1.grid(row=0, column=6, padx=5, pady=5)
a1_text = Label(a_frame, text = "Ask Jeeves")
a1_text.grid(row=0, column=7, padx=5, pady=5)
a1_Menu3 = OptionMenu(a_frame, a1clicked3 , *options3)
a1_Menu3.grid(row=0, column=8, padx=5, pady=5)
a1_Button2 = Button(a_frame, text ="enter", command = jeeves)
a1_Button2.grid(row=0, column=9, padx=5, pady=5)

#row 2 columss grids and other settings
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
b1str6_input = Entry(b1l_frame,textvariable= b1str6, width = 5)
b1str6_input.grid(row=1, column=1, padx=5, pady=5)
b1str5_text = Label(b1l_frame, text = "string 5 Note")
b1str5_text.grid(row=2, column=0, padx=5, pady=5)
b1str5_input = Entry(b1l_frame,textvariable= b1str5, width = 5)
b1str5_input.grid(row=2, column=1, padx=5, pady=5)
b1str4_text = Label(b1l_frame, text = "string 4 Note")
b1str4_text.grid(row=3, column=0, padx=5, pady=5)
b1str4_input = Entry(b1l_frame,textvariable= b1str4, width = 5)
b1str4_input.grid(row=3, column=1, padx=5, pady=5)
b1str3_text = Label(b1l_frame, text = "string 3 Note")
b1str3_text.grid(row=1, column=2, padx=5, pady=5)
b1str3_input = Entry(b1l_frame,textvariable=  b1str3, width = 5)
b1str3_input.grid(row=1, column=3, padx=5, pady=5)
b1str2_text = Label(b1l_frame, text = "string 2 Note")
b1str2_text.grid(row=2, column=2, padx=5, pady=5)
b1str2_input = Entry(b1l_frame,textvariable=  b1str2, width = 5)
b1str2_input.grid(row=2, column=3, padx=5, pady=5)
b1str1_text = Label(b1l_frame, text = "string 1 Note")
b1str1_text.grid(row=3, column=2, padx=5, pady=5)
b1str1_input = Entry(b1l_frame,textvariable=  b1str1, width = 5)
b1str1_input.grid(row=3, column=3, padx=5, pady=5)
b2_text = Label(b2l_frame, text = "Root Note")
b2_text.grid(row=0, column=0, padx=5, pady=5)
b2_Menu = OptionMenu(b2l_frame, b2clicked , *options1)
b2_Menu.grid(row=0, column=1, padx=5, pady=5)
b2_text1 = Label(b2l_frame, text = "Chord type")
b2_text1.grid(row=1, column=0, padx=5, pady=5)
b2_Menu1 = OptionMenu(b2l_frame, b2clicked1 , *options4)
b2_Menu1.grid(row=1, column=1, padx=5, pady=5)
b2_Button = Button(b2l_frame, text ="set", command = Chorddict)
b2_Button.grid(row=2, column=0, padx=10, pady=5)



#row 3 columss grids and other settings
c1_Button = Button(c_frame, text ="Arppegiate", command = Arp)
c1_Button.grid(row=0, column=0, padx=10, pady=5)
c1_Button1 = Button(c_frame, text ="Scale Check", command = Check)
c1_Button1.grid(row=0, column=1, padx=10, pady=5)
c1_Button2 = Button(c_frame, text ="Chord View", command = Cview)
c1_Button2.grid(row=0, column=2, padx=10, pady=5)


root.mainloop()