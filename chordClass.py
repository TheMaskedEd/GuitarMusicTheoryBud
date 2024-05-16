import main

class chords():

    def scaleCheck(self, chord):
        clist = chord

        # List of all strings
        strings = [main.string1, main.string2, main.string3, main.string4, main.string5, main.string6]

        # Iterate over each string
        for string_index, string in enumerate(strings):
            # If the note is 'x', continue to the next string
            if clist[string_index] == 'x':
                continue
            # If the note is not in the scale, return False
            elif string[int(clist[string_index])] == ' ':
                return False

        # If the function reaches all the way to the end without hitting False,
        # it will indicate that the chord does fit within the scale thus returning True
        return True

    def arpeggioMaker(self, chord):
        print(chord)

        # List of all strings
        strings = [main.string1, main.string2, main.string3, main.string4, main.string5, main.string6]

        cnotes = []

        # Iterate over each string
        for string_index, string in enumerate(strings):
            # If the note is 'x', continue to the next string
            if chord[string_index] == 'x':
                continue
            # If there is a note, append the note at the index of the current element of chord in the current string to cnotes
            else:
                cnotes.append(string[int(chord[string_index])])

        # Remove duplicates from cnotes
        new = []
        [new.append(x) for x in cnotes if x not in new]
        return new

    def arpeggiate(self, chord):
        print(chord)

        # List of all strings
        strings = [main.string1, main.string2, main.string3, main.string4, main.string5, main.string6]

        cnotes = []

        # Iterate over each string
        for string_index, string in enumerate(strings):
            # If the note is 'x', continue to the next string
            if chord[string_index] == 'x':
                continue
            # If there is a note, append the note at the index of the current element of chord in the current string to cnotes
            else:
                cnotes.append(string[int(chord[string_index])])

        # Remove duplicates from cnotes
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
        #Splits our value and creates an Array Chordnotes
        chordnotes = d[chord].split(',')
        return chordnotes

    def chordDict2(self, root, type):
        chords = {
            "F Major": [0, 4, 7],
            "F Minor": [0, 3, 7],
            "F Diminished": [0, 3, 6],
            "F Augmented": [0, 4, 8],
            "F Major 7th": [0, 4, 7, 11],
            "F Minor 7th": [0, 3, 7, 10],
            "F7": [0, 4, 7, 10],
            "F Diminished 7th": [0, 3, 6, 9],
            "F Augmented 7th": [0, 4, 8, 11],
            "Fsus2": [0, 2, 7],
            "Fsus4": [0, 5, 7],
            "Fadd9": [0, 4, 7, 14],
            "F6": [0, 4, 7, 9],
            "Fm6": [0, 3, 7, 9],
            "F9": [0, 4, 7, 10, 14],
            "Fm9": [0, 3, 7, 10, 14],
            "F11": [0, 4, 7, 10, 14, 17],
            "Fm11": [0, 3, 7, 10, 14, 17],
            "F13": [0, 4, 7, 10, 14, 17, 21],
            "Fm13": [0, 3, 7, 10, 14, 17, 21]
        }

        print(chords)

    def chordmaker(self, root, type):
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
        #Splits our value and creates an Array Chordnotes
        chordnotes = d[chord].split(',')
        return chordnotes


# displays selected chord on fretboard utilises for loops
    def chordView(self, chord):
        # List of all strings
        strings = [main.string1, main.string2, main.string3, main.string4, main.string5, main.string6]

        # Iterate over each string
        for string_index, string in enumerate(strings):
            # Loop over the indices of the current string
            for i in range(len(string)):
                # Check if the current element in chord is equal to the current index
                if chord[string_index] == str(i):
                    # If so, skip
                    continue
                # If not, replace with a blank value
                else:
                    string[i] = " "
