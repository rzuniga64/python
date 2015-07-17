
def in_fridge(some_fridge, desired_item):
    """This is a function to see if the fridge has food.
    fridge has to be a dictionary defined outside of the 
    function. The food to be searched for is in the string 
    wanted_food"""
    try:
        count = some_fridge[desired_item]
    except KeyError:
        count = 0 
    return count


def make_new_sauce():
    """ This function makes a new special sauce all its own"""
    special_sauce = ['mustard', 'yogurt']
    return special_sauce


def make_omelet(omelet_type):
    """This will make an omelet. You can either pass in a 
    dictionary that contains all of the ingredients for
    your omelt, or provide a string to select a type of
    omelet this function already knows about"""
    def get_omelet_ingredients(omelet_name):
#    """This contains a dictionary of omelet names that can be produced, and their ingredients"""
        # all of our omelets need eggs and milk
        ingredients = {'eggs': 2, 'milk': 1}
        if omelet_name == 'cheese':
            ingredients['cheddar'] = 2
        elif omelet_name == 'western':
            ingredients['jack cheese'] = 2
            ingredients['ham'] = 1
            ingredients['pepper'] = 1
            ingredients['onion'] = 1
        elif omelet_name == 'greek':
            ingredients['feta_cheese'] = 1
            ingredients['spinach'] = 1
        else:
            print("That's not on the menu, sorry!")
            return None
        return ingredients

    if type(omelet_type) == type({}):
        print('omelet_type is a dictionary with ingredients')
        return make_food(omelet_type, 'omelet')
    elif type(omelet_type) == type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        raise TypeError("no such omelet type: %s" % omelet_type)


def make_food(ingredients_needed, food_name):
    """make_food(ingredients_needed, food_name) 
       Takes the ingredients from ingredients_needed and makes
       food_name"""
    for ingredient in ingredients_needed.keys():
        print("adding %d of %s to make a %s omelet" % (ingredients_needed[ingredient], ingredient, food_name))
    print("Made %s omelet" % food_name)
    return food_name
