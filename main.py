class Main:
    def __init__(self):
        self.scales = {
        "major": [0, 2, 4, 5, 7, 9, 11],
        "minor": [0, 2, 3, 5, 7, 8, 10],
        "harmonic minor": [0, 2, 3, 5, 7, 8, 11],
        "melodic minor (ascending)": [0, 2, 3, 5, 7, 9, 11],
        "melodic minor (descending)": [0, 2, 3, 5, 7, 8, 10],
        "ionian": [0, 2, 4, 5, 7, 9, 11],
        "dorian": [0, 2, 3, 5, 7, 9, 10],
        "phrygian": [0, 1, 3, 5, 7, 8, 10],
        "lydian": [0, 2, 4, 6, 7, 9, 11],
        "mixolydian": [0, 2, 4, 5, 7, 9, 10],
        "aeolian": [0, 2, 3, 5, 7, 8, 10],
        "locrian": [0, 1, 3, 5, 6, 8, 10],
        "major pentatonic": [0, 2, 4, 7, 9],
        "minor pentatonic": [0, 3, 5, 7, 10],
        "blues": [0, 3, 5, 6, 7, 10],
        "chromatic": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "whole tone": [0, 2, 4, 6, 8, 10],
        "octatonic (whole-half)": [0, 2, 3, 5, 6, 8, 9, 11],
        "octatonic (half-whole)": [0, 1, 3, 4, 6, 7, 9, 10],
        "enigmatic": [0, 1, 4, 6, 8, 10, 11],
        # Non-Western Scales
        "raga bilawal": [0, 2, 4, 5, 7, 9, 11],  # Equivalent to Ionian
        "raga yaman": [0, 2, 4, 6, 7, 9, 11],  # Similar to Lydian
        "pelog": [0, 1, 3, 7, 8],  # Example of a Pelog scale
        "slendro": [0, 2, 4, 7, 9],  # Example of a Slendro scale
        "maqam rast": [0, 2, 4, 5, 7, 9, 11],  # Similar to Major with microtonal variations
        "maqam hijaz": [0, 1, 4, 5, 7, 8, 11]  # Similar to Phrygian dominant
        }
        self.string1 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
        self.string2 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
        self.string3 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
        self.string4 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
        self.string5 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
        self.string6 = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
        self.notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']*2




