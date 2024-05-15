#Dictionary of scales and their intervals
scales = {
        "major": [0, 2, 4, 5, 7, 9, 11],
        "minor": [0, 2, 3, 5, 7, 8, 10, 12],
        "dorian": [0, 2, 3, 5, 7, 9, 10, 12],
        "phrygian": [0, 1, 3, 5, 7, 8, 10, 12],
        "minor pentatonic": [0, 3, 5, 7, 10],
        "major pentatonic": [0, 2, 4, 7, 9],
        "harmonic minor": [0, 2, 3, 5, 7, 10, 11],
        "mixolydian": [0, 2, 4, 5, 7, 9, 10],
        "minor blues": [0, 3, 5, 6, 7, 10],
        "locrian": [0, 1, 3, 5, 6, 8, 10, 12],
        "lydian": [0, 2, 4, 6, 7, 9, 11, 12],
    }
#String arrays
string1 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
string2 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
string3 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
string4 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
string5 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
string6 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
#notes arrays the *3 is used speecifically for getnotes in order to stay within index
notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']*3

# Import the necessary classes
import chordClass
import etcClass

def main():
    # Create instances of the classes
    chordClass_instance = chordClass
    etcClass_instance = etcClass

    prompt = """
Please select an option from the menu:
1. Scales
2. Chord check

"""
    func = input(prompt)

    if func == "scales":
        # Get the tuning from the user
        etcClass_instance.tunning()

        # Get the scale and key from the user
        scale = input("Please select your scale")
        key = input("Please select your key")

        # Get the notes for the scale using the etcClass
        scale_notes = etcClass_instance.getnotes(key, scales[scale])
        # Set these notes as the key on the guitar using the etcClass
        etcClass_instance.setkey(scale_notes)

    elif func == "Chord check":
        # Get the tuning from the user
        tunning = input("Please select your tuning")
        # Set the tuning using the etcClass
        etcClass_instance.tunning(tunning)

        # Get the root note, chord type, and root string from the user
        root = input("Root note of chord")
        type = input("Chord Type")
        rootString = input("Which string is the root note at")

        # Get the notes for the chord using the chordClass
        chordnotes = chordClass_instance.chordDict(root, type)
        print(chordnotes)

        # Check if the chord fits in the scale using the chordClass
        fits_in_scale = chordClass_instance.scaleCheck(chordnotes)
        print(f"Chord fits in scale: {fits_in_scale}")

        # View the chord using the chordClass
        chordClass_instance.chordView(chordnotes)

    else:
        print("Command not recognised")

main()




