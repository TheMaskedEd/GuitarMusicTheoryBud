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

    # ChordDict basic chord dictionary
    def chordDict(self, root, type):
        # Define the intervals for each chord
        intervals = {
            "major": [0, 4, 7],
            "minor": [0, 3, 7],
            "diminished": [0, 3, 6],
            "augmented": [0, 4, 8],
            "major 7th": [0, 4, 7, 11],
            "minor 7th": [0, 3, 7, 10],
            "7": [0, 4, 7, 10],
            "diminished 7th": [0, 3, 6, 9],
            "augmented 7th": [0, 4, 8, 11],
            "sus2": [0, 2, 7],
            "sus4": [0, 5, 7],
            "add9": [0, 4, 7, 14],
            "6": [0, 4, 7, 9],
            "m6": [0, 3, 7, 9],
            "9": [0, 4, 7, 10, 14],
            "m9": [0, 3, 7, 10, 14],
            "11": [0, 4, 7, 10, 14, 17],
            "m11": [0, 3, 7, 10, 14, 17],
            "13": [0, 4, 7, 10, 14, 17, 21],
            "m13": [0, 3, 7, 10, 14, 17, 21]
        }

        # Get the intervals for the chord type
        chord_intervals = intervals[type]

        # Get the notes for the chord using the getnotes function
        chord_notes = self.getnotes(root, type)

        # Get the notes for the chord
        chord_notes = [chord_notes[interval % len(chord_notes)] for interval in chord_intervals]

        return chord_notes

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
