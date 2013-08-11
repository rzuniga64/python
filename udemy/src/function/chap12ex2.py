# Let's create an  acronym: in my humble opinion
#IMHO

def first(word):
   return word[0]

def acronym(words):
   acro = ''
   acro = acro.join(list(map(first, words))).upper()
   return acro

def main():
    words = ['in','my','humble','opinion']
    acro = acronym(words)
    print(acro)
    
main()