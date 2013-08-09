
class Student:

    def __init__( self, first, last, major, age ):
        self.firstName = first
        self.lastName = last
        self.age = age
        self.major = major

    def display( self ):
        print( self.firstName, self.lastName, self.major, self.age )

    def __str__(self ):
        return self.firstName + " " + self.lastName + "(" + \
               self.major + ") age =" + str( self.age )

