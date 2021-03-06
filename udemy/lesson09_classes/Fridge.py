"""
    This class implements a fridge where ingredients
    can be added and removed individually, or in groups.
    The fridge will retain a count of every ingredient
    added or removed, and it will raise an error if a sufficient
    quantity of an ingredient isn't present.
    Methods:
    has(food_name [, quantity]) - checks if the string food_name is in  fridge.
    Quantity will be set to 1 if you don't specify a number.
    has_various(foods) - checks if enough of every food in dict is in the fridge
    add_one(food_name) - adds a single food_name to the fridge
    add_many(food_dict) - adds a whole dictionary filled with food
    get_one(food_name) - takes out a single food_name from the fridge
    get_many(food_dict) - takes out a whole dictionary worth of food.
    get_ingredients(food) - If passed an object that has the __ingredients__
            method, get_many will invoke this to get the list of ingredients.
"""


class Fridge:

    # Optionally pass in an initial dictionary of items
    def __init__(self, items):
        if type(items) != type(dict()):
            raise TypeError(
                "Fridge requires a dictionary but was given %s" % type(items))
        self.foods_removed = dict()
        self.items = items
        return

    # Internal method to be called on by objects that need to act on ingredients
    def __ingredients__(self):
        return self.items

    """
    Adds more than one food item. Returns the number of items added.
    This should only be used internally, after the type checking has been
    done
    """
    def __add_multi(self, food_name, quantity):

        if food_name not in self.items:
            self.items[food_name] = 0

        self.items[food_name] = self.items[food_name] + quantity

    """
    Removes more than one of a food_item. Returns number of items removed.
    Returns False if there isn't enough food_name in the fridge.  This
    should only be used internally, after the type checking has been done
    """
    def __get_multi(self, food_name, quantity):

        try:
            if self.items[food_name] is None:
                return False
            if quantity > self.items[food_name]:
                return False
            self.items[food_name] -= quantity
        except KeyError:
            return False
        return quantity

    """
    Adds a singe food_name to the fridge. Returns True.
    Raises a TypeError if food_name is not a string
    """
    def add_one(self, food_name):

        if type(food_name) != type(' '):
            raise TypeError(
                "add_one requires a string, given a %s" % type(food_name))
        else:
            self.__add_multi(food_name, 1)

        return True

    """
    Adds a whole dictionary filled with food as keys and quantities as values.
    Returns a dictionary with the removed food.  Raises a TypeError if food_dict
    is not a dictionary.Returns False if there is not enough food in the fridge
    """
    def add_many(self, food_dict):

        if type(food_dict) != type(dict()):
            raise TypeError(
                "add_many requires a dictionary, got a %s" % food_dict)

        for item in food_dict.keys():
            self.__add_multi(item, food_dict[item])
        return

    """
    Checks if the string food_name is in the fridge. Quantity will be set to 1
    if you don't specify a number. Returns True if there is enough, False
    otherwise.
    """
    def has(self, food_name, quantity=1):

        return self.has_various({food_name: quantity})

    """
    Checks if the dictionary food_name has enough of every element to
    satisfy a request.  Returns True if there's enough, False if there's
    not or if an element does not exist
    """
    def has_various(self, foods):

        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False
                return True
        except KeyError:
            return False

    """
    Takes out a single food_name from the fridge. Returns a dictionary with
    the food: 1 as a result, or False if there wasn't enough in the fridge.
    """
    def get_one(self, food_name):

        if isinstance(food_name, str):
            raise TypeError(
                "get_one requires a string, given a %s" % type(food_name))
        else:
            result = self.__get_multi(food_name, 1)
        return result

    """
    takes out a whole dictionary worth of food. Returns a dictionary
    with all of the ingredients. Returns False if there are not enough
    ingredients or if a dictionary isn't provided
    """
    def get_many(self, food_dict):

        if self.has_various(food_dict):
            for item in food_dict.keys():
                self.foods_removed[item] = \
                    self.__get_multi(item, food_dict[item])
        return self.foods_removed

    """
    if passed an object that has the __ingredients__ method, get_many will
    invoke this to get the list of ingredients.
    """
    def get_ingredients(self, food):

        try:
            ingredients = self.get_many(food)
        except AttributeError:
            return False

        if ingredients is not False:
            return ingredients
