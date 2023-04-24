import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import main
def plot():
    # Define the positions of the guitar strings and frets
    string_pos = [1, 2, 3, 4, 5, 6]  # E, B, G, D, A, E
    fret_pos = list(range(0, 13))

    # Define the notes you want to plot
    fretboard= [main.string1,main.string2,main.string3,main.string4,main.string5,main.string6]
    print(fretboard)


    # Plot Strings
    fig, ax = plt.subplots(figsize=(10, 6))
    background = ['white', 'black']
    for i in range(1, 7):
        ax.plot([i for a in range(14)])

    # Plotting Frets
    for i in range(1, 13):
        ax.axvline(x=i, color= 'k', linewidth=0.5)
        ax.set_axisbelow(True)

    # setting height and width of displayed guitar
    ax.set_xlim([0, 13])
    ax.set_ylim([0.4, 6.5])

    # setting the circle properties
    circleRadius = 0.2
    circleColour = 'red'
    for string_num, string in enumerate(fretboard):
        for fret_num, fret in enumerate(string):
            if fret != " ":
                note_pos = main.notes.index(fret)
                note_string_pos = string_pos[string_num]
                note_fret_pos = fret_pos[fret_num]
                circle = mpatches.Circle((note_fret_pos + 0.5, note_string_pos), circleRadius, facecolor=circleColour,edgecolor='black',zorder= 10)
                ax.add_patch(circle)
                ax.text(fret_num + 0.5, string_num+1,fret, ha='center', va='center', color='black',zorder = 20)

    plt.yticks(range(1,7), ['6', '5', '4', '3', '2', '1'])
    plt.xticks(range(13))
    plt.show()