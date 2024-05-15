import Plot
import main

class etcClass():

    # Sets the tuning on the guitar by getting the first note and iterating down the note array
    def setTunning(self, tune):
        stringnote = tune
        print(tune)

        # The for loop iterates over each element in main.string1.
        for o in range(len(main.string1)):
            # The index() method is used to find the index of the character..
            # at position 0 of the stringnote string in the main.notes list.
            # This value is assigned to the variable x.
            x = main.notes.index(stringnote[0])
            # The element at position o in main.string1 is assigned a new value
            # based on the sum of i and x indices in the main.notes list.
            main.string1[o] = main.notes[(o + x) % len(main.notes)]

        # The same process is repeated for main.string2 through main.string6.
        for o in range(len(main.string2)):
            x = main.notes.index(stringnote[1])
            main.string2[o] = main.notes[(o + x) % len(main.notes)]
        for o in range(len(main.string3)):
            x = main.notes.index(stringnote[2])
            main.string3[o] = main.notes[(o + x) % len(main.notes)]
        for o in range(len(main.string4)):
            x = main.notes.index(stringnote[3])
            main.string4[o] = main.notes[(o + x) % len(main.notes)]
        for o in range(len(main.string5)):
            x = main.notes.index(stringnote[4])
            main.string5[o] = main.notes[(o + x) % len(main.notes)]
        for o in range(len(main.string6)):
            x = main.notes.index(stringnote[5])
            main.string6[o] = main.notes[(o + x) % len(main.notes)]

    # Plots the notes in a key to the fretboard
    def setkey(self, key):
        print(key)

        # A for loop iterates through each element parts in main.string1.
        for i in range(len(main.string1)):
            # The current element in main.string1 is checked to see if it is in the key list.
            if main.string1[i] not in key:
                # If it isn't, we replace the note with a blank
                main.string1[i] = ' '

        # The same process is repeated for main.string2 through main.string6.
        for i in range(len(main.string2)):
            if main.string2[i] not in key:
                main.string2[i] = ' '
        for i in range(len(main.string3)):
            if main.string3[i] not in key:
                main.string3[i] = ' '
        for i in range(len(main.string4)):
            if main.string4[i] not in key:
                main.string4[i] = ' '
        for i in range(len(main.string5)):
            if main.string5[i] not in key:
                main.string5[i] = ' '
        for i in range(len(main.string6)):
            if main.string6[i] not in key:
                main.string6[i] = ' '

        # Plots our key when done
        Plot.plot()

    # A basic dictionary of tunings
    def tunning(self):
        tunnings = {
            "standard": ['E', 'A', 'D', 'G', 'B', 'E'],
        }

        # Display the available tunings to the user
        print("Available tunings:")
        for tuning_name in tunnings.keys():
            print(tuning_name)

        # Get the tuning from the user
        tuning_name = input("Please select your tuning: ")

        # Check if the selected tuning is valid
        if tuning_name not in tunnings:
            print("Invalid tuning selected.")
            return

        # Get the selected tuning
        tuning = tunnings[tuning_name]

        # Print the selected tuning
        print(f"Selected tuning: {tuning}")

        # Set the tuning
        self.setTunning(tuning)

    # Function that utilises intervals and octaves to get notes for a scale
    def getnotes(self, key, scale):
        # Root is assigned the value of the index in main.notes
        # where the value of key is located.
        root = main.notes.index(key)
        # Intervals is assigned the interval found within
        # the key of the dictionary main.scales.
        intervals = main.scales[scale]
        # Octave is assigned the value of a slice of main.notes
        # from the index root to root+13. This creates a list of
        # the 13 notes in one octave starting from root.
        octave = main.notes[root:root+13]
        # A list comprehension is used to create a new list called temp by
        # iterating through each element i in intervals. For each i,
        # the corresponding element in octave is added to temp.
        temp = [octave[i] for i in intervals]
        return temp

    # Basic dictionary with guitar terms stored on a dictionary.txt
    def jeeves(self, term):
        print(term)
        d = {}
        # Opens the file "Dictionary.txt" using the with statement and assigns it to the variable f.
        with open("Dictionary.txt") as f:
           # It iterates through each line in the file using a for loop.
           for line in f:
                # It splits each line by whitespace and assigns
                # the resulting key-value pair to the key and val variables.
                (key, val) = line.split()
                # It adds the key-value pair to the d dictionary.
                d[key] = val
        # It assigns the value of the term key in the d dictionary to the string variable.
        string = d[term]
        # It replaces all occurrences of "_" with " " in the string variable
        # and assigns the result to new_string.
        new_string = string.replace("_", " ")
        return new_string
