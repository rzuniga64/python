def main():
    grades = {'Cynthia':88, 'David':77, 'Clayton':99}
    for key in grades.keys():
        print(key, grades[key])
        
    # We can have an iterator into the keys
    it = iter(grades)
    print(next(it))
    print(next(it))
    print(next(it))
    
    # Use iterator in a for loop to access each key
    for key in grades:
        print(key, grades[key])
    
main()