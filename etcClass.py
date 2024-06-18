from main import Main
class extra(Main):

    #Sets the tuning on the guitar by getting the first note and iterating down the note array
    def setTunning(tune):
        print(tune)

        # List of all strings
        strings = [Main.string1, Main.string2, Main.string3, Main.string4, Main.string5, Main.string6]

        # Iterate over each string
        for string_index, string in enumerate(strings):
            note_index = 0
            fret_index = 0

            # Get the note for the current string from the tune
            stringnote = tune[string_index]

            # Iterate over each note in the string
            for _ in string:
                x = Main.notes.index(stringnote)
                string[fret_index] = Main.notes[note_index + x]
                if note_index < 11 - x:
                    note_index = note_index + 1
                else:
                    note_index = -x
                fret_index = fret_index + 1

    #plots the notes in a key to the fretboard
    def setkey(self, key, fret_range, strings_to_display):
        print(key)

        # List of all strings
        strings = {
            'E': Main.string1,
            'A': Main.string2,
            'D': Main.string3,
            'G': Main.string4,
            'B': Main.string5,
            'e': Main.string6
        }

        # Create a dictionary to map notes to their positions
        note_positions = {note: i + 1 for i, note in enumerate(key)}

        # Iterate over each string
        for string_name, string in strings.items():
            if string_name not in strings_to_display:
                continue  # Skip strings not in strings_to_display

            # Create a blank string for the specified fret range
            string_range = [' '] * (fret_range[1] - fret_range[0] + 1)

            # Iterate over each note in the string within the fret range
            for i in range(fret_range[0], fret_range[1] + 1):
                # If the note is in the key, annotate it with its position
                if string[i] in key:
                    string_range[i - fret_range[0]] = f"{string[i]}({note_positions[string[i]]})"

            # Print the annotated string
            print(f"{string_name}: {string_range}")

    #a basic dictionary of tunings
    def tunning(self, tuning_notes):
        # Convert the string of notes to a list
        tuning_notes = list(tuning_notes)

        # Set the tuning
        extra.setTunning(tuning_notes)

        print(tuning_notes)
        return tuning_notes

    #function that utilises intervals and octives to get notes for a scale
    def getnotes(self, key, scale):
        # root is assigned the value of the index in Main.notes
        # where the value of key is located.
        root = Main.notes.index(key)
        # intervals is assigned the interval found within
        # the key of the dictionary Main.scales .
        intervals = Main.scales[scale]
        # octave is assigned the value of a slice of Main.notes
        # from the index root to root+13. This creates a list of
        # the 13 notes in one octave starting from root.
        octave = Main.notes[root:root+13]
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