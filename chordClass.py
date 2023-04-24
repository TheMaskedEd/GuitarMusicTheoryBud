import Plot
import main

class Chords():

    def scalecheck(chord):
        clist = chord
        if clist[0] == 'x':
            pass
        elif main.string1[int(clist[0])] == ' ':
            return False
        if clist[1] == 'x':
            pass
        elif main.string2[int(clist[1])] == ' ':
            return False
        if clist[2] == 'x':
            pass
        elif main.string3[int(clist[2])] == ' ':
            return False
        if clist[3] == 'x':
            pass
        elif main.string4[int(clist[3])] == ' ':
            return False
        if clist[4] == 'x':
            pass
        elif main.string5[int(clist[4])] == ' ':
            return False
        if clist[5] == 'x':
            pass
        elif main.string6[int(clist[5])] == ' ':
            return False
        return True
    def Arpeggiate(chord):
        clist = chord
        print(clist)
        cnotes = []
        if clist[0] == 'x':
            pass
        else:
            cnotes.append(main.string1[int(clist[0])])
        if clist[1] == 'x':
            pass
        else:
            cnotes.append(main.string2[int(clist[1])])
        if clist[2] == 'x':
            pass
        else:
            cnotes.append(main.string3[int(clist[2])])
        if clist[3] == 'x':
            pass
        else:
            cnotes.append(main.string4[int(clist[3])])
        if clist[4] == 'x':
            pass
        else:
            cnotes.append(main.string5[int(clist[4])])
        if clist[5] == 'x':
            pass
        else:
            cnotes.append(main.string6[int(clist[5])])
            print(cnotes)

        new = []
        [new.append(x) for x in cnotes if x not in new]
        print(new)
        from etcClass import Extra
        Extra.setkey(new)


    def chordcheck(chord):
        clist = chord
        if clist[0] == 'x':
            pass
        elif main.string1[int(clist[0])] == '-':
            return False
        if clist[1] == 'x':
            pass
        elif main.string2[int(clist[1])] == '-':
            return False
        if clist[2] == 'x':
            pass
        elif main.string3[int(clist[2])] == '-':
            return False
        if clist[3] == 'x':
            pass
        elif main.string4[int(clist[3])] == '-':
            return False
        if clist[4] == 'x':
            pass
        elif main.string5[int(clist[4])] == '-':
            return False
        if clist[5] == 'x':
            pass
        elif main.string6[int(clist[5])] == '-':
            return False
        return True


    # ChordDict basic chord dictionary stored on chord dictionary.txt
    def ChordDict(root, type):
        chord = str(root) + "_" + str(type)
        d = {}
        with open("Chords.txt") as f:
            for line in f:
                (key, val) = line.split()
                d[key] = val
        print(d)
        print(chord)
        chordnotes = d[chord].split(',')
        print(chordnotes)
        return chordnotes


# displays selected chord on fretboard utilises for loops
    def chordView(chord):
        clist = chord
        for i in range(len(main.string1)):
            if clist[0] == str(i):
                pass
            else:
                main.string1[i] = " "
        for i in range(len(main.string2)):
            if clist[1] == str(i):
                pass
            else:
                main.string2[i] = " "
        for i in range(len(main.string3)):
            if clist[2] == str(i):
                pass
            else:
                main.string3[i] = " "
        for i in range(len(main.string4)):
            if clist[3] == str(i):
                pass
            else:
                main.string4[i] = " "
        for i in range(len(main.string5)):
            if clist[4] == str(i):
                pass
            else:
                main.string5[i] = " "
        for i in range(len(main.string6)):
            if clist[5] == str(i):
                pass
            else:
                main.string6[i] = " "

        Plot.plot()