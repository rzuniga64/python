import sys

import Fridge as Fridge
import Omelet as Omelet


def main():

    print(sys.path)
    f = Fridge.Fridge({'eggs': 6, 'milk': 4, 'cheese': 3})
    f.add_one('grape')
    f.add_many({'mushroom': 5, 'tomato': 3})
    
    o = Omelet.Omelet('cheese')
    o.get_ingredients(f)
    o.mix()
    o.make()
    
    # This isn't any easier or harder to use than making a single omelet was in
    # Ch 5. However, the benefit of using objects becomes obvious when you have
    # many things to work with at the same time - for instance, many omelets
    # being made at the same time."""
    
    f = Fridge.Fridge({'cheese': 5, 'milk': 4, 'eggs': 12, 'mushroom': 6,
                       'onion': 6})
    o = Omelet.Omelet('cheese')
    m = Omelet.Omelet('mushroom')
    c = Omelet.Omelet('onion')
    o.get_ingredients(f)
    o.mix()
    m.get_ingredients(f)
    m.mix()
    c.get_ingredients(f)
    c.mix()
    o.make()
    m.make()
    c.make()
    
main()
