import re
    
def getFile(f):
    d = []
    r = []
    i = []
    dLength = 0
    rLength = 0
    iLength = 0
    p = re.compile(r'\t(.+)\s+\((\w+)\)\s+(.+)\t')
    
    file = open(f, 'r')

    for l in file:
        sen = p.split(l.strip())
        sen.append(int(sen[4]) - int(sen[3]))

        if sen[2].lower() == 'r':
            r.append(sen)
            rLength += sen[5]
        elif sen[2].lower() == 'd':
            d.append(sen)
            dLength += sen[5]
        elif sen[2].lower() == 'i':
            i.append(sen)
            iLength += sen[5]

    rLength /= len(r)
    dLength /= len(d)
    iLength /= len(i)

    r.sort(key= lambda x: x[5], reverse=True)
    d.sort(key= lambda x: x[5], reverse=True)
    i.sort(key= lambda x: x[5], reverse=True)

    print('Averages:')
    print('-' * 25)
    print('Republicans:'.ljust(20), round(rLength, 2))
    for x in r:
        if x[5] > rLength:
            print(x[1].ljust(20), x[5])
    print('Democrats:'.ljust(20), round(dLength, 2))
    for x in d:
        if x[5] > dLength:
            print(x[1].ljust(20), x[5])
    print('Independants:'.ljust(20), round(iLength, 2))
    for x in i:
        if x[5] > iLength:
            print(x[1].ljust(20), x[5])
    
    file.close()

def main():

    getFile('senators.txt')

main()
