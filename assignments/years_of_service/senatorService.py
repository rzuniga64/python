debug = True


class Senator:

    def __init__(self, first, last, districtNo, party, office, yrStarted):

        self.first = first
        self.last = last
        self.districtNo = districtNo
        self.party = party
        self.office = office
        self.yrStarted = yrStarted

    def getService(self, current=2013):

        return current - self.yrStarted

    def getFirst(self):

        return self.first

    def getLast(self):

        return self.last

    def getFullName(self):

        return self.first + " " + self.last

    def getDistrictNo(self):

        return self.districtNo

    def getParty(self):

        return self.party

    def getOffice(self):

        return self.office

    def getYearStarted(self):

        return self.yrStarted

    def setFirst(self, first):

        self.first = first

    def setLast(self, last):

        self.last = last

    def setFullName(self, fullname):

        names = fullname.split()
        self.first = names[0]
        self.last = names[1]

    def setDistrictNo(self, districtNo):

        self.districtNo = districtNo

    def setParty(self, party):

        self.party = party

    def setOffice(self, office):

        self.office = office

    def setYearStarted(self, yrStarted):

        self.yrStarted = yrStarted

    def display(self):
        print(
            self.first + " " + self.last + " from Texas " + str(self.districtNo) +
            " (" + self.party + ") started service in " + str(self.yrStarted))

    def __str__(self):
        return self.first + " " + self.last+" from Texas " + str(self.districtNo)+ \
            " (" + self.party + ") started service in " + str(self.yrStarted) + \
            " and has served " + str(self.getService()) + " years."


def test():
    # Create one senator.
    senator = Senator('Donna', 'Campbell', '25', 'Republican', 'New Braunfels', 2013)
    senator.display()
    print(senator.getFullName())
    print(senator.getDistrictNo())
    print(senator.getParty())
    print(senator.getYearStarted())
    print()
    senator.setFullName("Fred Flintstone")
    print(senator.getFullName())
    print(senator.getDistrictNo())
    print(senator.getParty())
    print(senator.getYearStarted())

test()


def DetermineAvgByParty(senators):
    # Determine the average years of service by party.
    totalService = 2 * [0]
    partyMembers = 2 * [0]
    for senator in senators:
        service = senator.getService()
        if senator.getParty() == "Democratic":
            totalService[0] += service
            partyMembers[0] += 1
        elif senator.getParty() == "Republican":
            totalService[1] += service
            partyMembers[1] += 1

    demAvgService = totalService[0] / partyMembers[0]
    repAvgService = totalService[1] / partyMembers[1]

    print("Average Democrat service is " + str(demAvgService) + " years")
    print("Average Republican service is " + str(repAvgService) + " years")
    print()
    return demAvgService, repAvgService


def DetermineExceedsAvgByParty( demAvgService, repAvgService, senators):
    # Determine which senators exceed the average years of service by party.
    print("These Texas senators have service years exceeding their party average:")
    for senator in senators:
        service = senator.getService()
        if senator.getParty() == "Democratic":
            if senator.getService() > demAvgService:
                print(senator)
        elif senator.getParty() == "Republican":
            if senator.getService() > repAvgService:
                print(senator)


def DetermineService():

    senators = [
        Senator('Kevin', 'Eltife', '1', 'Republican', 'Tyler', 2004),
        Senator('Bob', 'Deuell', '2', 'Republican', 'Greenville', 2003),
        Senator('Robert', 'Nichols', '3', 'Republican', 'Jacksonville', 2007),
        Senator('Tommy', 'Williams', '4', 'Republican', 'The Woodlands', 2003),
        Senator('Charles', 'Schwertner', '5', 'Republican', 'Georgetown', 2013),
        Senator('Sylvia', 'Garcia', '6', 'Democratic', 'Houston', 2013),
        Senator('Dan', 'Patrick', '7', 'Republican', 'Houston', 2007),
        Senator('Ken', 'Paxton', '8', 'Republican', 'McKinney', 2013),
        Senator('Kelly', 'Hancock', '9', 'Republican', 'Fort Worth', 2013),
        Senator('Wendy', 'Davis', '10', 'Democratic', 'Fort Worth', 2009),
        Senator('Larry', 'Taylor', '11', 'Republican', 'Friendswood', 2013),
        Senator('Jane', 'Nelson', '12', 'Republican', 'Flower Mound', 1993),
        Senator('Rodney', 'Ellis', '13', 'Democratic', 'Houston', 1990),
        Senator('Kirk', 'Watson', '14', 'Democratic', 'Austin', 2007),
        Senator('John', 'Whitmire', '15', 'Democratic', 'Houston', 1983),
        Senator('John', 'Carona', '16', 'Republican', 'Dallas', 1996),
        Senator('Joan', 'Huffman', '17', 'Republican', 'Southside Place', 2008),
        Senator('Glenn', 'Hegar', '18', 'Republican', 'Katy', 2007),
        Senator('Carlos', 'Uresti', '19', 'Democratic', 'San Antonio', 2006),
        Senator('Juan', 'Hinojosa', '20', 'Democratic', 'McAllen', 2002),
        Senator('Judith', 'Zaffirini', '21', 'Democratic', 'Laredo', 1987),
        Senator('Brian', 'Birdwell', '22', 'Republican', 'Granbury', 2010),
        Senator('Royce', 'West', '23', 'Democratic', 'Dallas', 1993),
        Senator('Troy', 'Fraser', '24', 'Republican', 'Horseshoe Bay', 1997),
        Senator('Donna', 'Campbell', '25', 'Republican', 'New Braunfels', 2013),
        Senator('Leticia', 'Putte', '26', 'Democratic', 'San Antonio', 1999),
        Senator('Eddie', 'Lucio', '27', 'Democratic', 'Brownsville', 1991),
        Senator('Robert', 'Duncan', '28', 'Republican', 'Lubbock', 1997),
        Senator('Jose', 'Rodriguez', '29', 'Democratic', 'El Paso', 2011),
        Senator('Craig', 'Estes', '30', 'Republican', 'Wichita Falls', 2001),
        Senator('Kel', 'Seliger', '31', 'Republican', 'Amarillo', 2004)]

    demAvg, repAvg = DetermineAvgByParty(senators)
    DetermineExceedsAvgByParty(demAvg, repAvg, senators)


def main():

    senators = DetermineService()

# main()
