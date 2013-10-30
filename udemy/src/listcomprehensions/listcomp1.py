def main():

    grades = [71, 81, 77, 84]
    
    for i in range(len(grades)):
        grades[i] += 5
    print(grades)
    
    grades = [grade + 5 for grade in grades]
    print(grades)
    
    words = ['NOW', 'IS', 'THE', 'TIME']
    word = [word.lower() for word in words]
    print(word)
    
main()