"""ID: alex.go2
LANG: PYTHON3
TASK: palsquare
"""
f = open('palsquare.in', 'r')
g = open('palsquare.out', 'w')
readfile = f.readlines()
base  = int(readfile[0])
newnumber = []
allintegers = []
allsquares = []
integersquares = []
finaloutput = []
finaloutputy = []
append = True
def convert (number):
    if number < base :
        if number < 10:
            newnumber.append(number)
            return number
        if number == 10:
            newnumber.append('A')
            return 'A'
        if number == 11:
            newnumber.append('B')
            return 'B'
        if number == 12:
            newnumber.append('C')
            return 'C'
        if number == 13:
            newnumber.append('D')
            return 'D'
        if number == 14:
            newnumber.append('E')
            return 'E'
        if number == 15:
            newnumber.append('F')
            return 'F'
        if number == 16:
            newnumber.append('G')
            return 'G'
        if number == 17:
            newnumber.append('H')
            return 'H'
        if number == 18:
            newnumber.append('I')
            return 'I'
        if number == 19:
            newnumber.append('J')
            return 'J'
    else:
        if number % base < 10:
            newnumber.append(number % base)
        elif number % base == 10:
            newnumber.append('A')
        elif number % base == 11:
            newnumber.append('B')
        elif number % base == 12:
            newnumber.append('C')
        elif number % base == 13:
            newnumber.append('D')
        elif number % base == 14:
            newnumber.append('E')
        elif number % base == 15:
            newnumber.append('F')
        elif number % base == 16:
            newnumber.append('G')
        elif number % base == 17:
            newnumber.append('H')
        elif number % base == 18:
            newnumber.append('I')
        elif number % base == 19:
            newnumber.append('J')
        return convert(int(number / base))



for x in range (1, 301):
    append = True
    del newnumber[:]
    convert(x**2)
    for y in range (0, len(newnumber)):
        if newnumber[y] != newnumber[len(newnumber) - 1 - y]:
            append = False
    if append:
        allintegers.append(x)
allsquares = allintegers.copy()
for x in range (0, len(allintegers)):
    del finaloutput [:]
    del newnumber [:]
    del finaloutputy [:]
    convert(allintegers[x])  
    for y in range (0, len(newnumber)):
        finaloutput.append(str(newnumber[len(newnumber)- 1 - y]))
    del newnumber [:]
    convert(allsquares[x] ** 2)
    for z in range (0, len(newnumber)):
        finaloutputy.append(str(newnumber[len(newnumber)- 1 - z]))
    g.write("".join(finaloutput) + " " + "".join(finaloutputy) + "\n")
    

g.close()

    

    

            

