# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import main
from etcClass import extra
from chordClass import chords


def terminal():
    # Create instances of the classes
    chords_instance = chords()
    extra_instance = extra()

    # Define the options
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    scales = [
        "major",
        "minor",
        "harmonic minor",
        "melodic minor (ascending)",
        "melodic minor (descending)",

        "ionian",
        "dorian",
        "phrygian",
        "lydian",
        "mixolydian",
        "aeolian",
        "locrian",

        "major pentatonic",
        "minor pentatonic",

        "blues",

        "chromatic",

        "whole tone",

        "octatonic (whole-half)",
        "octatonic (half-whole)",

        "enigmatic",

        # Non-Western Scales
        "raga bilawal",
        "raga yaman",
        "pelog",
        "slendro",
        "maqam rast",
        "maqam hijaz"
    ]
    tunings = ["Standard"]
    chord_types = ["major", "minor"]

    while True:
        prompt = "Please select an option from the menu:\n" \
                 "Scales\n" \
                 "Chord view\n" \
                 "Chord check\n" \
                 "Arp\n" \
                 "Type 'exit' to quit\n" \
                 "Your choice: "
        func = input(prompt)

        if func.lower() == "exit":
            break

        if func == "1":
            # Get the tuning from the user
            tunning = input(f"Please select your tuning:\n{tunings}\n")
            # Set the tuning using the extra class
            extra_instance.tunning(tunning)

            # Get the scale and key from the user
            scale = input(f"Please select your scale:\n{scales}\n")
            key = input("Please select your key")

            # Get the notes for the scale using the extra class
            scale_notes = extra_instance.getnotes(key, scale)
            # Set these notes as the key on the guitar using the extra class
            extra_instance.setkey(scale_notes)
            for i in (main.string1,main.string2,main.string3,main.string4,main.string5,main.string6):
                print(i)

        elif func == "2":
            # Get the tuning from the user
            tunning = input("Please select your tuning")
            # Set the tuning using the extra class
            extra_instance.tunning(tunning)

            # Get the root note, chord type,from the user
            root = input("Root note of chord")
            type = input("Chord Type")

            # Get the notes for the chord using the chords class
            chordnotes = chords_instance.chordDict(root, type)

            # View the chord using the chords class
            chords_instance.chordView(chordnotes)
            for i in (main.string1,main.string2,main.string3,main.string4,main.string5,main.string6):
                print(i)

        elif func == "3":
            # Get the tuning from the user
            tunning = input("Please select your tuning")
            # Set the tuning using the extra class
            extra_instance.tunning(tunning)

            # Get the root note, chord type, and root string from the user
            root = input("Root note of chord")
            type = input("Chord Type")

            # Get the notes for the chord using the chords class
            chordnotes = chords_instance.chordDict(root, type)
            print(chordnotes)

            # Get the scale and key from the user
            scale = input("Please select your scale")
            key = input("Please select your key")

            # Get the notes for the scale using the extra class
            scale_notes = extra_instance.getnotes(key, scale)
            # Set these notes as the key on the guitar using the extra class
            extra_instance.setkey(scale_notes)

            # Check if the chord fits in the scale using the chords class
            fits_in_scale = chords_instance.scaleCheck(chordnotes)
            print(f"Chord fits in scale: {fits_in_scale}")

        elif func == "4":
            # Get the tuning from the user
            tunning = input("Please select your tuning")
            # Set the tuning using the extra class
            extra_instance.tunning(tunning)

            # Get the root note, chord type, and root string from the user
            root = input("Root note of chord")
            type = input("Chord Type")

            # Get the notes for the chord using the chords class
            chordnotes = chords_instance.chordDict(root, type)
            print(chordnotes)

            # Arpeggiate chord using the chords class arpegiate function
            extra_instance.setkey(chords_instance.arpeggiate(chordnotes))
            for i in (main.string1,main.string2,main.string3,main.string4,main.string5,main.string6):
                print(i)

        else:
            print("Command not recognised")

terminal()




