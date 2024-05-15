import main

class chords():

    def scaleCheck(self, chord):
        clist = chord
        #The function checks if the first character of the clist variable is 'x',
        # which would indicate a muted string, and does nothing if it is.
        if clist[0] == 'x':
            pass
        #If the corresponding note on the first string is a space,
        # which would indicate that it is not a valid note in the current scale.
        elif main.string1[int(clist[0])] == ' ':
            #return false to the user
            return False

        # The same process is repeated for main.string2 through main.string6.
        if clist[1] == 'x':
            pass
        elif main.string2[int(clist[1])] == ' ':
            return False
        if clist[2] == 'x':
            pass
        elif main.string3[int(clist[2])] == ' ':
            return False
        if clist[3] == 'x':
            pass
        elif main.string4[int(clist[3])] == ' ':
            return False
        if clist[4] == 'x':
            pass
        elif main.string5[int(clist[4])] == ' ':
            return False
        if clist[5] == 'x':
            pass
        elif main.string6[int(clist[5])] == ' ':
            return False

        # If the functions reaches all the way to the end without hitting False then
        # it will indicate that the chord does fit within the scale thus returning True
        return True
    def arpeggiate(self, chord):
        clist = chord
        print(clist)
        cnotes = []
        # The function checks if the first character of the clist variable is 'x',
        # which would indicate a muted string, and does nothing if it is.
        if clist[0] == 'x':
            pass
        #if there is a note, append the note at the index of the first element of clist in main.string1 to cnotes.
        else:
            cnotes.append(main.string1[int(clist[0])])

        # The same process is repeated for main.string2 through main.string6.
        if clist[1] == 'x':
            pass
        else:
            cnotes.append(main.string2[int(clist[1])])
        if clist[2] == 'x':
            pass
        else:
            cnotes.append(main.string3[int(clist[2])])
        if clist[3] == 'x':
            pass
        else:
            cnotes.append(main.string4[int(clist[3])])
        if clist[4] == 'x':
            pass
        else:
            cnotes.append(main.string5[int(clist[4])])
        if clist[5] == 'x':
            pass
        else:
            cnotes.append(main.string6[int(clist[5])])
            print(cnotes)

        new = []
        [new.append(x) for x in cnotes if x not in new]
        return new

    # ChordDict basic chord dictionary stored on chord dictionary.txt
    def chordDict(self, root, type):
        chord = str(root) + "_" + str(type)
        d = {}
        #opens the file "Chords.txt" using the with statement and assigns it to the variable f.
        with open("Chords.txt") as f:
            ##It iterates through each line in the file using a for loop.
            for line in f:
                #Split each line into two parts: the key and the value.
                (key, val) = line.split()
                #Add the key-value pair to the dictionary d.
                d[key] = val
        print(d)
        print(chord)
        #Splits our value and creates an Array Chordnotes
        chordnotes = d[chord].split(',')
        return chordnotes


# displays selected chord on fretboard utilises for loops
    def chordView(self, chord):
        clist = chord
        #Loop over the indices of main.string1
        for i in range(len(main.string1)):
            # Check if the first element in clist is equal to the current index.
            if clist[0] == str(i):
                # If so skip
                pass
            # If not...
            else:
                # replace with a blank value
                main.string1[i] = " "
        for i in range(len(main.string2)):
            if clist[1] == str(i):
                pass
            else:
                main.string2[i] = " "
        for i in range(len(main.string3)):
            if clist[2] == str(i):
                pass
            else:
                main.string3[i] = " "
        for i in range(len(main.string4)):
            if clist[3] == str(i):
                pass
            else:
                main.string4[i] = " "
        for i in range(len(main.string5)):
            if clist[4] == str(i):
                pass
            else:
                main.string5[i] = " "
        for i in range(len(main.string6)):
            if clist[5] == str(i):
                pass
            else:
                main.string6[i] = " "
