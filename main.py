# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#dictionary of scales and their integers
scales = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "minor": [0, 2, 3, 5, 7, 10, 11],
    "dorian": [0, 2, 3, 5, 7, 9, 10, 12],
    "phrygian": [0, 1, 3, 5, 7, 8, 10, 12],
    "minor pentatonic": [0, 3, 5, 7, 10],
    "major pentatonic": [0, 2, 4, 7, 9],
    "harmonic minor": [0, 2, 3, 5, 7, 8, 10, 12],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "minor blues": [0, 3, 5, 6, 7, 10],
    "locrian": [0, 1, 3, 5, 6, 8, 10, 12],
    "lydian": [0, 2, 4, 6, 7, 9, 11, 12],
}
string1 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
string2 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
string3 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
string4 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
string5 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
string6 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']*3

# function to set tuning utilising for loops
def settunning(tune):
    stringnote = tune

    i = 0
    o = 0

    #loop that starts at a value and is ended at a value will soon be replaced
    for parts in string1:
        x = notes.index(stringnote[0])
        string1[o] = notes[i+x]
        if i < 11 - x:
            i = i + 1
        else:
            i = -x
        o = o + 1

    i = 0
    o = 0

    for parts in string2:
        x = notes.index(stringnote[1])
        string2[o] = notes[i+x]
        if i < 11 - x:
            i = i + 1
        else:
            i = -x
        o = o + 1

    i = 0
    o = 0

    for parts in string3:
        x = notes.index(stringnote[2])
        string3[o] = notes[i+x]
        if i < 11 - x:
            i = i + 1
        else:
            i = -x
        o = o + 1

    i = 0
    o = 0

    for parts in string4:
        x = notes.index(stringnote[3])
        string4[o] = notes[i+x]
        if i < 11 - x:
            i = i + 1
        else:
            i = -x
        o = o + 1

    i = 0
    o = 0

    for parts in string5:
        x = notes.index(stringnote[4])
        string5[o] = notes[i+x]
        if i < 11 - x:
            i = i + 1
        else:
            i = -x
        o = o + 1

    i = 0
    o = 0

    for parts in string6:
        x = notes.index(stringnote[5])
        string6[o] = notes[i+x]
        if i < 11 - x:
            i = i + 1
        else:
            i = -x
        o = o + 1

#uses for loops to setkey with notes generated from get notes
def setkey(key):
    print(key)

    i = 0
    for parts in string1:
        if string1[i] in key:
            pass
        else:
            string1[i] = '-'
        i = i + 1
    i = 0
    for parts in string2:
        if string2[i] in key:
            pass
        else:
            string2[i] = '-'
        i = i + 1
    i = 0
    for parts in string3:
        if string3[i] in key:
            pass
        else:
            string3[i] = '-'
        i = i + 1
    i = 0
    for parts in string4:
        if string4[i] in key:
            pass
        else:
            string4[i] = '-'
        i = i + 1
    i = 0
    for parts in string5:
        if string5[i] in key:
            pass
        else:
            string5[i] = '-'
        i = i + 1
    i = 0
    for parts in string6:
        if string6[i] in key:
            pass
        else:
            string6[i] = '-'
        i = i + 1

    print(string6)
    print(string5)
    print(string4)
    print(string3)
    print(string2)
    print(string1)


#function using for loops to check wether a chord is in a scale
def scalecheck(chord):
    clist = chord
    if clist[0] == 'x':
        pass
    elif string1[int(clist[0])] == '-':
        return False
    if clist[1] == 'x':
        pass
    elif string2[int(clist[1])] == '-':
        return False
    if clist[2] == 'x':
        pass
    elif string3[int(clist[2])] == '-':
        return False
    if clist[3] == 'x':
        pass
    elif string4[int(clist[3])] == '-':
        return False
    if clist[4] == 'x':
        pass
    elif string5[int(clist[4])] == '-':
        return False
    if clist[5] == 'x':
        pass
    elif string6[int(clist[5])] == '-':
        return False
    return True

# function made to arpeggiate a chord over the fretboard
def Arpeggiate(chord):
    clist = chord
    print(clist)
    cnotes = []
    if clist[0] == 'x':
        pass
    else:
        cnotes.append(string1[int(clist[0])])
    if clist[1] == 'x':
        pass
    else:
       cnotes.append(string2[int(clist[1])])
    if clist[2] == 'x':
        pass
    else:
        cnotes.append(string3[int(clist[2])])
    if clist[3] == 'x':
        pass
    else:
        cnotes.append(string4[int(clist[3])])
    if clist[4] == 'x':
        pass
    else:
        cnotes.append(string5[int(clist[4])])
    if clist[5] == 'x':
        pass
    else:
        cnotes.append(string6[int(clist[5])])
    print(cnotes)

    new = []
    [new.append(x) for x in cnotes if x not in new]
    print(new)
    setkey(new)


#def main():
 #   prompt = "Please select an option from menu"
  #  func = input(prompt)

   # if func == "scales":
    #    tunning()
     #   scalekey()
   # elif func == "chord enter":
    #    tunning()
     #   chord()
   # elif func == "chord check":
    #    tunning()
     #   print(setchord())
    #elif func == "arp":
     #   arpeggiate()
    #elif func == "jeeves":
     #   print(jeeves())
    #else:
     #   print("Command not recognised")

#Function to check whether chord is compatibilty
def chordcheck(chord):
    clist = chord
    if clist[0] == 'x':
        pass
    elif string1[int(clist[0])] == '-':
        return False
    if clist[1] == 'x':
        pass
    elif string2[int(clist[1])] == '-':
        return False
    if clist[2] == 'x':
        pass
    elif string3[int(clist[2])] == '-':
        return False
    if clist[3] == 'x':
        pass
    elif string4[int(clist[3])] == '-':
        return False
    if clist[4] == 'x':
        pass
    elif string5[int(clist[4])] == '-':
        return False
    if clist[5] == 'x':
        pass
    elif string6[int(clist[5])] == '-':
        return False
    return True
#change

#dictionary of tuning
def tunning(tunning):
    tunnings = {
        "standard":['E','A','D','G','B','E'],
        "drop d":['D','A','D','G','B','E'],
        "drop c": ['C','G','C','F','A','D'],
        "B standard": ['B','E','A','D','F#','B'],
    }
    settunning(tunnings[tunning])
    print(tunning)
    return(tunnings[tunning])

#function that utilises intervals and octives to get notes for a scale
def getnotes(key, scale):
    root = notes.index(key)
    intervals = scales[scale]
    octave = notes[root:root+13]
    temp = [octave[i] for i in intervals]
    return temp

#basic dictionary with guitar terms stored on a dictionary.txt
def jeeves(term):
    print(term)
    d ={}
    with open("Dictionary.txt") as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
    print(d[term])
    string = d[term]
    new_string = string.replace("_"," ")
    return(new_string)

#ChordDict basic chord dictionary stored on chord dictionary.txt
def ChordDict(root,type):
    chord = str(root)+"_"+str(type)
    d = {}
    with open("Chords.txt") as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
    print(d)
    print(chord)
    chordnotes = d[chord].split(',')
    print(chordnotes)
    return chordnotes

#displays selected chord on fretboard utilises for loops
def chordView(chord):
    clist = chord
    for i in range(len(string1)):
        if clist[0] == str(i):
            pass
        else:
            string1[i] = "-"
    for i in range(len(string2)):
        if clist[1] == str(i):
            pass
        else:
            string2[i] = "-"
    for i in range(len(string3)):
        if clist[2] == str(i):
            pass
        else:
            string3[i] = "-"
    for i in range(len(string4)):
        if clist[3] == str(i):
            pass
        else:
            string4[i] = "-"
    for i in range(len(string5)):
        if clist[4] == str(i):
            pass
        else:
            string5[i] = "-"
    for i in range(len(string6)):
        if clist[5] == str(i):
            pass
        else:
            string6[i] = "-"

    print(string6)
    print(string5)
    print(string4)
    print(string3)
    print(string2)
    print(string1)







#main()





