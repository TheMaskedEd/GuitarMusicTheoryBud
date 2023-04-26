import Plot
import main

class Extra():

    #Sets the tuning on the guitar by getting the first note and iterating down the note array
    def settunning(tune):
        stringnote = tune
        print(tune)

        i = 0
        o = 0

        #The for loop iterates over each element in main.string1.
        for parts in main.string1:
            #The index() method is used to find the index of the character..
            # at position 0 of the stringnote string in the main.notes list.
            # This value is assigned to the variable x.
            x = main.notes.index(stringnote[0])
            #The element at position o in main.string1 is assigned a new value
            # based on the sum of i and x indices in the main.notes list.
            main.string1[o] = main.notes[i+x]
            #If i is less than 11 minus x, i is incremented by 1.
            if i < 11 - x:
                i = i + 1
            #If i is not less than 11 minus x, i is set to -x.
            else:
                i = -x
            #o is incremented by 1.
            o = o + 1

        #The same process is repeated for main.string2 through main.string6.

        i = 0
        o = 0

        for parts in main.string2:
            x = main.notes.index(stringnote[1])
            main.string2[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

        i = 0
        o = 0

        for parts in main.string3:
            x = main.notes.index(stringnote[2])
            main.string3[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

        i = 0
        o = 0

        for parts in main.string4:
            x = main.notes.index(stringnote[3])
            main.string4[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

        i = 0
        o = 0

        for parts in main.string5:
            x = main.notes.index(stringnote[4])
            main.string5[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

        i = 0
        o = 0

        for parts in main.string6:
            x = main.notes.index(stringnote[5])
            main.string6[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

    #plots the notes in a key to the fretboard
    def setkey(key):
        print(key)

        i = 0
        #A for loop iterates through each element parts in main.string1.
        for parts in main.string1:
            #The current element in main.string1 is checked to see if it is in the key list.
            if main.string1[i] in key:
                #If it is we skip and go to the next fret
                pass
            #If it isnt...
            else:
                #we replace the note with a blank
                main.string1[i] = ' '
            i = i + 1
        i = 0

        #The same process is repeated for main.string2 through main.string6.

        for parts in main.string2:
            if main.string2[i] in key:
                pass
            else:
                main.string2[i] = ' '
            i = i + 1
        i = 0
        for parts in main.string3:
            if main.string3[i] in key:
                pass
            else:
                main.string3[i] = ' '
            i = i + 1
        i = 0
        for parts in main.string4:
            if main.string4[i] in key:
                pass
            else:
                main.string4[i] = ' '
            i = i + 1
        i = 0
        for parts in main.string5:
            if main.string5[i] in key:
                pass
            else:
                main.string5[i] = ' '
            i = i + 1
        i = 0
        for parts in main.string6:
            if main.string6[i] in key:
                pass
            else:
                main.string6[i] = ' '
            i = i + 1


        #plots our key when done
        Plot.plot()

    #a basic dictionary of tunings
    def tunning(tunning):
        tunnings = {
            "standard":['E','A','D','G','B','E'],
        }
        #sends it over to set tunning
        Extra.settunning(tunnings[tunning])
        print(tunnings[tunning])
        #returns it just incase we need to use later
        return(tunnings[tunning])

    #function that utilises intervals and octives to get notes for a scale
    def getnotes(key, scale):
        # root is assigned the value of the index in main.notes
        # where the value of key is located.
        root = main.notes.index(key)
        # intervals is assigned the interval found within
        # the key of the dictionary main.scales .
        intervals = main.scales[scale]
        # octave is assigned the value of a slice of main.notes
        # from the index root to root+13. This creates a list of
        # the 13 notes in one octave starting from root.
        octave = main.notes[root:root+13]
        # A list comprehension is used to create a new list called temp by
        # iterating through each element i in intervals. For each i,
        # the corresponding element in octave is added to temp.
        temp = [octave[i] for i in intervals]
        return temp

    #basic dictionary with guitar terms stored on a dictionary.txt
    def jeeves(term):
        print(term)
        d ={}
        #opens the file "Dictionary.txt" using the with statement and assigns it to the variable f.
        with open("Dictionary.txt") as f:
           #It iterates through each line in the file using a for loop.
           for line in f:
                #It splits each line by whitespace and assigns
                # the resulting key-value pair to the key and val variables.
                (key, val) = line.split()
                #It adds the key-value pair to the d dictionary.
                d[key] = val
        #It assigns the value of the term key in the d dictionary to the string variable.
        string = d[term]
        #It replaces all occurrences of "_" with " " in the string variable
        # and assigns the result to new_string.
        new_string = string.replace("_"," ")
        return(new_string)