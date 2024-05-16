import main

class extra():

    #Sets the tuning on the guitar by getting the first note and iterating down the note array
    def setTunning(tune):
        print(tune)

        # List of all strings
        strings = [main.string1, main.string2, main.string3, main.string4, main.string5, main.string6]

        # Iterate over each string
        for string_index, string in enumerate(strings):
            note_index = 0
            fret_index = 0

            # Get the note for the current string from the tune
            stringnote = tune[string_index]

            # Iterate over each note in the string
            for _ in string:
                x = main.notes.index(stringnote)
                string[fret_index] = main.notes[note_index + x]
                if note_index < 11 - x:
                    note_index = note_index + 1
                else:
                    note_index = -x
                fret_index = fret_index + 1

    #plots the notes in a key to the fretboard
    def setkey(self, key):
        print(key)

        # List of all strings
        strings = [main.string1, main.string2, main.string3, main.string4, main.string5, main.string6]

        # Create a dictionary to map notes to their positions
        note_positions = {note: i + 1 for i, note in enumerate(key)}

        # Iterate over each string
        for string in strings:
            # Iterate over each note in the string
            for i in range(len(string)):
                # If the note is in the key, annotate it with its position
                if string[i] in key:
                    string[i] = f"{string[i]}({note_positions[string[i]]})"
                else:
                    # If the note is not in the key, replace it with a blank space
                    string[i] = ' '

        # Print the annotated strings
        for string in strings:
            print(string)

    #a basic dictionary of tunings
    def tunning(self, tunning):
        tunnings = {
            "standard":['E','A','D','G','B','E'],
        }
        #sends it over to set tunning
        extra.setTunning(tunnings[tunning])
        print(tunnings[tunning])
        #returns it just incase we need to use later
        return(tunnings[tunning])

    #function that utilises intervals and octives to get notes for a scale
    def getnotes(self, key, scale):
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