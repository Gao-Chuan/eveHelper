from ships import ship, T2ship

def pad(i):
    ret = i
    if i % 100 != 0:
        i = i + 100 - (i%100)
    return i


# for dict whose value is int.
def dict_add(a, b):
    a = a.copy()
    b = b.copy()

    ret = {}
    for e in list(a.keys()):
        if e in b:
            ret[e] = a.pop(e) + b.pop(e)
        else:
            ret[e] = a.pop(e)
    ret.update(b)
    return ret

# for dict whose value is int.
def dict_sub(a, b):
    a = a.copy()
    b = b.copy()

    ret = {}
    for e in list(a.keys()):
        if e in b:
            ret[e] = a.pop(e) + b.pop(e)
        else:
            ret[e] = a.pop(e)
    ret.update(b)
    return ret

def get(ship, key):
    obj = None
    if key == "moon_material":
        obj = ship.moon_material
    elif key == "intermediate":
        obj = ship.intermediate
    elif key == "composite":
        obj = ship.composite
    elif key == "components":
        obj = ship.components
    elif key == "fuel_block":
        obj = ship.fuel_block
    elif key == "mineral":
        obj = ship.mineral
    elif key == "planet_material":
        obj = ship.planet_material
    elif key == "items":
        obj = ship.items
    else:
        raise Exception("get key error:>>{}".format(key))

    if obj is not None:
        for e in obj:
            if obj[e] > 0:
                print(e + ' ' + str(obj[e]))
    else:
        print('')


def merge(a:ship, b: ship):
    retVal = ship()
    retVal.composite = dict_add(a.composite, b.composite)
    retVal.intermediate = dict_add(a.intermediate, b.intermediate)
    retVal.moon_material = dict_add(a.moon_material, b.moon_material)
    retVal.fuel_block = dict_add(a.fuel_block, b.fuel_block)
    retVal.components = dict_add(a.components, b.components)
    retVal.mineral = dict_add(a.mineral, b.mineral)
    retVal.items = dict_add(a.items, b.items)
    retVal.planet_material = dict_add(a.planet_material, b.planet_material)

    return retVal