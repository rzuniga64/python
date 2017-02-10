"""
    Purpose: This class implements a car where the make, model and year
    can be added or modified.

     __init__ (make, model, year) - sets the attributes to default values.
    getmake() - returns the car's make
    getmodel() - returns the car's model
    getyear() - returns the year the car was made
    setmake(make) - sets the make of the car
    setmodel(model) - sets the model of the car
    setyear(model) - sets the year the car was made
"""


class Car:

    def __init__(self, make=" ", model=" ", year=0):
        if not isinstance(make, str) or not isinstance(model, str) \
                or not isinstance(year, int):
            raise TypeError('Car requires make and model as string and year as '
                            'integer but was given %10s %10s %4s'
                            % (type(make), type(model), type(year)))

        self.__make = make
        self.__model = model
        self.__year = year

    def getmake(self):
        return self.__make

    def getmodel(self):
        return self.__model

    def getyear(self):
        return self.__year

    def setmake(self, make):
        self.__make = make

    def setmodel(self, model):
        self.__model = model

    def setyear(self, year):
        self.__year = year


def main():

    # instantiate an object of the car class and set attributes using default
    # constructor
    jetta = Car("Volkswagen", "Jetta", 2012)
    print("Car's make: %10s Model: %10s Year: %4d" % (jetta.getmake(),
                                                      jetta.getmodel(),
                                                      jetta.getyear()))

    # instantiate object of the car class and set attributes using class methods
    prius = Car()
    prius.setmake("Toyota")
    prius.setmodel("Prius")
    prius.setyear(2010)
    print("Car's make: %10s Model: %10s Year: %4d" % (prius.getmake(),
                                                      prius.getmodel(),
                                                      prius.getyear()))

main()
