ints1 = [1,2,3,4,5,6]
ints2 = [2,3,4,5,6,7]
ints3 = [2,3,4,5,6,7]
ints4 = ['E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E']

str1 = ['E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E']
str2 = ['B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
str3 = ['G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G']
str4 = ['D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D']
str5 = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A']
str6 = ['E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E']
intsnew = []

intsQ = ['C','E','G']
root = 'C'
rootString = '5'


for i in str1:
    if int(rootString) >= 1:
        if i in intsQ:
            intsnew.append(str1.index(i))
            break
    else:
        intsnew.append('x')
        break

for i in str2:
    if int(rootString) >= 2:
        if i in intsQ:
            intsnew.append(str2.index(i))
            break
    else:
        intsnew.append('x')
        break

for i in str3:
    if int(rootString) >= 3:
        if i in intsQ:
            intsnew.append(str3.index(i))
            break
    else:
        intsnew.append('x')
        break

for i in str4:
    if int(rootString) >= 4:
        if i in intsQ:
            intsnew.append(str4.index(i))
            break
    else:
        intsnew.append('x')
        break

for i in str5:
    if int(rootString) >= 5:
        if i in intsQ:
            intsnew.append(str5.index(i))
            break
    else:
        intsnew.append('x')
        break

for i in str6:
    if int(rootString) >= 6:
        if i in intsQ:
            intsnew.append(str6.index(i))
            break
    else:
        intsnew.append('x')
        break





for i in intsnew:
    print(i)
