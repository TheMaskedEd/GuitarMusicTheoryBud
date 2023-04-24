import Plot
import main

class Extra():
    def settunning(tune):
        stringnote = tune

        i = 0
        o = 0

        #loop that starts at a value and is ended at a value will soon be replaced
        for parts in main.string1:
            x = main.notes.index(stringnote[0])
            main.string1[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

        i = 0
        o = 0

        for parts in main.string2:
            x = main.notes.index(stringnote[1])
            main.string2[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

        i = 0
        o = 0

        for parts in main.string3:
            x = main.notes.index(stringnote[2])
            main.string3[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

        i = 0
        o = 0

        for parts in main.string4:
            x = main.notes.index(stringnote[3])
            main.string4[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

        i = 0
        o = 0

        for parts in main.string5:
            x = main.notes.index(stringnote[4])
            main.string5[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

        i = 0
        o = 0

        for parts in main.string6:
            x = main.notes.index(stringnote[5])
            main.string6[o] = main.notes[i+x]
            if i < 11 - x:
                i = i + 1
            else:
                i = -x
            o = o + 1

    def setkey(key):
        print(key)

        i = 0
        for parts in main.string1:
            if main.string1[i] in key:
                pass
            else:
                main.string1[i] = ' '
            i = i + 1
        i = 0
        for parts in main.string2:
            if main.string2[i] in key:
                pass
            else:
                main.string2[i] = ' '
            i = i + 1
        i = 0
        for parts in main.string3:
            if main.string3[i] in key:
                pass
            else:
                main.string3[i] = ' '
            i = i + 1
        i = 0
        for parts in main.string4:
            if main.string4[i] in key:
                pass
            else:
                main.string4[i] = ' '
            i = i + 1
        i = 0
        for parts in main.string5:
            if main.string5[i] in key:
                pass
            else:
                main.string5[i] = ' '
            i = i + 1
        i = 0
        for parts in main.string6:
            if main.string6[i] in key:
                pass
            else:
                main.string6[i] = ' '
            i = i + 1

        Plot.plot()

    def tunning(tunning):
        tunnings = {
            "standard":['E','A','D','G','B','E'],
        }
        Extra.settunning(tunnings[tunning])
        print(tunnings[tunning])
        return(tunnings[tunning])

    #function that utilises intervals and octives to get notes for a scale
    def getnotes(key, scale):
        root = main.notes.index(key)
        intervals = main.scales[scale]
        octave = main.notes[root:root+13]
        temp = [octave[i] for i in intervals]
        return temp

    #basic dictionary with guitar terms stored on a dictionary.txt
    def jeeves(term):
        print(term)
        d ={}
        with open("Dictionary.txt") as f:
            for line in f:
                (key, val) = line.split()
                d[key] = val
        string = d[term]
        new_string = string.replace("_"," ")
        return(new_string)