import sys

sys.stdout.write('hello\n')

# redirect stdout to file
sys.stdout = open('text.dat', 'a')
print('hello again')

textfile = open('text1.dat', 'a')
print >> textfile, 'hello'
