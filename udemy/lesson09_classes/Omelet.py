class Omelet:
    """This class creates an omelet object.  An omelet can be in one
    of two states: ingredients or cooked.  An omelet object has the 
    following interfaces:
    get_kind() - returns a string with the type type of omelet
    set_kind() - sets teh omelet to be the type named
    set_new_kind(kind, ingredients) - lets you create an omelet
    mix() - gets called after all the ingredients are gathered from the fridge
    cook() - cooks the omelet 
    """

    """
    This initializes the Omelet class to default to a cheese omelet.
    """
    def __init__(self, kind='cheese'):
        self.cooked = True
        self.mixed = True
        self.from_fridge = dict()
        self.needed_ingredients = dict()
        self.set_kind(kind)
        return

    """
    Internal method to be called on by a fridge or other objects that need to
    act on ingredients
    """
    def __ingredients__(self):
        return self.needed_ingredients

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        possible_ingredients = self.__known_kinds(kind)
        if possible_ingredients is False:
            return False
        else:
            self.kind = kind
            self.needed_ingredients = possible_ingredients

    def set_new_kind(self, name, ingredients):
        self.kind = name
        self.needed_ingredients = ingredients
        return

    def __known_kinds(self, kind):
        if kind == 'cheese':
            return {'eggs': 2, 'milk': 1, 'cheese': 1}
        elif kind == 'mushroom':
            return {'eggs': 2, 'cheese': 1, 'mushroom': 2}
        elif kind == 'onion':
            return {'eggs': 2, 'milk': 1, 'cheese': 1, 'onion': 1}
        else:
            return False

    def get_ingredients(self, fridge):
        self.from_fridge = fridge.get_ingredients(self.__ingredients__())

    def mix(self):
        for ingredient in self.from_fridge.keys():
            print('Mixing %d %s for the %s omelet' %
                  (self.from_fridge[ingredient], ingredient, self.kind))
        self.mixed = True

    def make(self):
        if self.mixed is True:
            print("Cooking the %s omelet!" % self.kind)
        self.cooked = True
