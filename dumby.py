class GuitarTab:
    def __init__(self, composition_name):
        super().__init__()
        self.composition_name = composition_name
        self.strings = ['e', 'B', 'G', 'D', 'A', 'E']
        self.tabs = {}

    def create_tab(self, tab_name, time_signature=4):
        self.tabs[tab_name] = {
            'time_signature': time_signature,
            'remaining_beats': time_signature,
            'notes': {string: [] for string in self.strings}
        }

    def edit_column(self, tab_name, column, new_notes):
        for string, note in zip(self.strings, new_notes):
            while len(self.tabs[tab_name]['notes'][string]) <= column:
                self.tabs[tab_name]['notes'][string].append(None)
            self.tabs[tab_name]['notes'][string][column] = str(note) if note is not None else note

    def interval(self, tab_name, column, new_notes, note_duration):
        self.edit_column(tab_name, column, new_notes)
        self.tabs[tab_name]['remaining_beats'] -= note_duration
        if self.tabs[tab_name]['remaining_beats'] == 0:
            self.edit_column(tab_name, column + 1, ['|' for _ in self.strings])
            self.tabs[tab_name]['remaining_beats'] = self.tabs[tab_name]['time_signature']

    def modifier(self, tab_name, column, string, mod):
        if string in self.strings and column < len(self.tabs[tab_name]['notes'][string]):
            self.tabs[tab_name]['notes'][string][column] += mod

    def remove_tab(self, tab_name):
        del self.tabs[tab_name]

    def display_tab(self, tab_name):
        print(f"Displaying tab: {tab_name} from the composition: {self.composition_name}")
        max_length = max(len(notes) for notes in self.tabs[tab_name]['notes'].values())
        for string, notes in self.tabs[tab_name]['notes'].items():
            for _ in range(max_length - len(notes)):
                notes.append(None)
            print(string + " | " + " ".join(note if note is not None else '-' for note in notes))





#Usage
guitar_tab = GuitarTab("mary had a little lamb")
guitar_tab.create_tab('intro', 4)  # 4 is the time signature

# Assuming each '-' or 'x' is a quarter note
guitar_tab.interval('intro', 0, [3, 2, 0, None, None, None], 1)  # 1 is the note duration
guitar_tab.interval('intro', 1, [None, None, None, None, None, None], 1)
guitar_tab.interval('intro', 2, [5, 3, 0, None, None, None], 1)
guitar_tab.interval('intro', 3, [5, 7, 0, None, None, None], 1)
guitar_tab.interval('intro', 5, [3, 2, 0, None, None, None], 1)  # 1 is the note duration
guitar_tab.interval('intro', 6, [None, None, None, None, None, None], 1)
guitar_tab.interval('intro', 7, [5, 3, 0, None, None, None], 1)
guitar_tab.interval('intro', 8, [5, 7, 0, None, None, None], 1)


guitar_tab.modifier('intro',14,'e','')
guitar_tab.display_tab('intro')

  # Outputs: Displaying tab: intro, E | 3 -, B | 2 -, G | 0 -, D | -, A | -, E | -"


class GuitarTb:
    def __init__(self, composition_name):
        super().__init__()
        self.composition_name = composition_name
        self.strings = ['e', 'B', 'G', 'D', 'A', 'E']
        self.tabs = {}

    def create_tab(self, tab_name):
        self.tabs[tab_name] = {string: [] for string in self.strings}

    def edit_column(self, tab_name, column, new_notes):
        for string, note in zip(self.strings, new_notes):
            while len(self.tabs[tab_name][string]) <= column:
                self.tabs[tab_name][string].append(None)
            self.tabs[tab_name][string][column] = str(note) if note is not None else note

    def modifier(self, tab_name, column, string, mod):
        if string in self.strings and column < len(self.tabs[tab_name][string]):
            self.tabs[tab_name][string][column] += mod

    def remove_tab(self, tab_name):
        del self.tabs[tab_name]

    def display_tab(self, tab_name):
        print(f"Displaying tab: {tab_name} from the composition: {self.composition_name}")
        max_length = max(len(notes) for notes in self.tabs[tab_name].values())
        for string, notes in self.tabs[tab_name].items():
            for _ in range(max_length - len(notes)):
                notes.append(None)
            print(string + " | " + " ".join(note if note is not None else '-' for note in notes))
class timingWIP:
    @staticmethod
    def calculate_remaining_space(note_counts, tuplet_counts):
        # Durations of standard notes in beats
        note_durations = {
            'whole_notes': 4,
            'half_notes': 2,
            'quarter_notes': 1,
            'eighth_notes': 0.5,
            'sixteenth_notes': 0.25
        }

        # Durations for all tuplets
        tuplet_durations = {
            'quarter_notes_triplets': 2 / 3,
            'quarter_notes_quadruplets': 3 / 4,
            'quarter_notes_quintuplets': 4 / 5,
            'quarter_notes_sextuplets': 4 / 6,
            'quarter_notes_septuplets': 4 / 7,
            'eighth_notes_triplets': 1 / 3, #1.5
            'eighth_notes_quadruplets': 1 / 2,
            'eighth_notes_quintuplets': 1 / 2.5,
            'eighth_notes_sextuplets': 1 / 3,
            'eighth_notes_septuplets': 1 / 3.5,
            'sixteenth_notes_triplets': 0.5 / 3,
            'sixteenth_notes_quadruplets': 0.5 / 2,
            'sixteenth_notes_quintuplets': 0.5 / 2.5,
            'sixteenth_notes_sextuplets': 0.5 / 3,
            'sixteenth_notes_septuplets': 0.5 / 3.5
        }

        # Calculate the total space used by the standard notes and tuplets
        total_used_space = sum(note_counts.get(note, 0) * duration for note, duration in note_durations.items())
        total_used_space += sum(tuplet_counts.get(tuplet, 0) * duration for tuplet, duration in tuplet_durations.items())

        # Total measure space in beats for 4/4 time signature
        total_measure_space = 4

        # Calculate the remaining space
        remaining_space = total_measure_space - total_used_space

        return remaining_space








# Example usage
note_counts = {
    'whole_notes': 0,
    'half_notes': 0,
    'quarter_notes': 0,
    'eighth_notes': 0,
    'sixteenth_notes': 0
}

tuplet_counts = {
    'quarter_notes_triplets': 0,
    'quarter_notes_quadruplets': 0,
    'quarter_notes_quintuplets': 0,
    'quarter_notes_sextuplets': 0,
    'quarter_notes_septuplets': 0,
    'eighth_notes_triplets': 0,
    'eighth_notes_quadruplets': 0,
    'eighth_notes_quintuplets': 0,
    'eighth_notes_sextuplets': 0,
    'eighth_notes_septuplets': 0,
    'sixteenth_notes_triplets': 12,
    'sixteenth_notes_quadruplets': 0,
    'sixteenth_notes_quintuplets': 0,
    'sixteenth_notes_sextuplets': 0,
    'sixteenth_notes_septuplets': 0
}













