import re
from math import ceil

from data import *
from util import pad

class fuel_block(object):
    def __init__(self, name, number) -> None:
        super().__init__()
        assert name in fuel_blocks_list, "Invalid fuel block name {}".format(name)
        self.name = name
        self.number = number

class moon_material(object):
    def __init__(self, name, number) -> None:
        super().__init__()
        assert name in moon_material_list, "Invalid moon material name {}".format(name)
        self.name = name
        self.number = number

class intermediate(object):
    def __init__(self, name, number) -> None:
        super().__init__()
        assert name in intermediate_list.keys(), "Invalid intermediate name {}".format(name)
        self.name = name
        self.number = number
        self.moon_material = {}
        self.fuel_block = {}
        for e in intermediate_list[name].split('\n'):
            name = re.search(r'[a-zA-Z ]+', e).group(0)[:-1]
            num = int(re.search(r'\d+', e).group(0))
            if name == 'output':
                self.output = num
                continue
            if 'Fuel Block' in name:
                self.fuel_block[name] = fuel_block(name, num)
            else:
                self.moon_material[name] = moon_material(name, num)

class composite(object):
    def __init__(self, name, number) -> None:
        super().__init__()
        assert name in composite_list.keys(), "Invalid composit name {}".format(name)
        self.name = name
        self.number = number
        self.intermediate = {}
        self.fuel_block = {}
        for e in composite_list[name].split('\n'):
            name = re.search(r'[a-zA-Z -]+', e).group(0)[:-1]
            num = int(re.search(r'\d+', e).group(0))
            if name == 'output':
                self.output = num
                continue
            if 'Fuel Block' in name:
                self.fuel_block[name] = fuel_block(name, num)
            else:
                self.intermediate[name] = intermediate(name, num)

class component(object):
    def __init__(self, name, number) -> None:
        super().__init__()
        component_list = None
        if name in component_gallent_list.keys():
            component_list = component_gallent_list.copy()
        elif name in component_amarr_list.keys():
            component_list = component_amarr_list.copy()
        elif name in component_T1_list.keys():
            component_list = component_T1_list.copy()
        elif name in component_caldari_list.keys():
            component_list = component_caldari_list.copy()
        elif name in component_minmatar_list.keys():
            component_list = component_minmatar_list.copy()
        assert component_list != None, "Invalid component name {}".format(name)

        self.name = name
        self.number = number
        self.composite = {}
        self.planet_material = {}
        for e in component_list[name].split('\n'):
            name = re.search(r'[a-zA-Z ]+', e).group(0)[:-1]
            num = int(re.search(r'\d+', e).group(0))
            if name == 'output':
                self.output = num
            # If it's a planetary material, add it to component's planet_material dict.
            elif name in planetary_material_list:
                if name in self.planet_material.keys():
                    self.planet_material[name] += num
                else:
                    self.planet_material[name] = num
            # If it's a normal high reaction material, create a composite object.
            else:
                self.composite[name] = composite(name, num)

class ship(object):
    def __init__(self, shipname, number = 1) -> None:
        super().__init__()
        self.ship_list = None
        if shipname in t2_ship_list.keys():
            self.ship_list = t2_ship_list.copy()
        elif shipname in battle_ship_list.keys():
            self.ship_list = battle_ship_list.copy()
        assert self.ship_list != None, "Not supported ship: {}".format(shipname)
        self.shipname = shipname
        self.number = number
        self.components = {}
        self.planet_material = {}
        if self.ship_list[shipname]['Planetary material'] != '':
            for e in self.ship_list[shipname]["Planetary material"].split('\n'):
                name = re.search(r'[a-zA-Z -]+', e).group(0)[:-1]
                num = int(re.search(r'\d+', e).group(0))
                assert name in planetary_material_list, "Invalid planetary material name: {}".format(name)
                self.planet_material[name] = num
        for e in self.ship_list[shipname]["componentList"].split('\n'):
            name = re.search(r'[a-zA-Z -]+', e).group(0)[:-1]
            num = int(re.search(r'\d+', e).group(0))
            self.components[name] = component(name, num)
            for each_planet_material in self.components[name].planet_material:
                if each_planet_material in self.planet_material.keys():
                    self.planet_material[each_planet_material] += (self.components[name].planet_material[each_planet_material] * self.components[name].number)
                else:
                    self.planet_material[each_planet_material] = (self.components[name].planet_material[each_planet_material] * self.components[name].number)
        self.composite = {}
        self.intermediate = {}
        self.moon_material = {}
        self.fuel_block = {}
    
    def get_components(self):
        ret = {}
        for name in self.components:
            obj = self.components[name]
            ret[name] = (obj.number)*self.number
        return ret 

    def get_composite(self):
        if self.composite == {}:
            for _name in self.components:
                e_component = self.components[_name]
                for name in e_component.composite:
                    obj = e_component.composite[name]
                    if name not in self.composite.keys():
                        self.composite[name] = composite(name, ceil((obj.number*e_component.number)/e_component.output))
                    else:
                        self.composite[name].number += ceil((obj.number*e_component.number)/e_component.output)
        ret = {}
        for k in self.composite:
            obj = self.composite[k]
            ret[k] = pad((obj.number)*self.number)
        return ret
    
    def get_intermediate(self):
        self.get_composite()
        if self.intermediate == {}:
            for _name in self.composite:
                e_composite = self.composite[_name]
                for name in e_composite.intermediate:
                    obj = e_composite.intermediate[name]
                    if name not in self.intermediate.keys():
                        self.intermediate[name] = intermediate(name, ceil((obj.number*e_composite.number)/e_composite.output))
                    else:
                        self.intermediate[name].number += ceil((obj.number*e_composite.number)/e_composite.output)
                for name in e_composite.fuel_block:
                    obj = e_composite.fuel_block[name]
                    if name in self.fuel_block.keys():
                        self.fuel_block[name].number += ceil((obj.number * e_composite.number)/e_composite.output)
                    else:
                        self.fuel_block[name] = fuel_block(name, ceil((obj.number * e_composite.number)/e_composite.output))
        ret = {}
        for k in self.intermediate:
            obj = self.intermediate[k]
            ret[k] = pad((obj.number)*self.number)
        return ret
    
    def get_moon_material(self):
        self.get_intermediate()
        if self.moon_material == {}:
            for _name in self.intermediate:
                e_intermediate = self.intermediate[_name]
                for name in e_intermediate.moon_material:
                    obj = e_intermediate.moon_material[name]
                    if name not in self.moon_material.keys():
                        self.moon_material[name] = moon_material(name, ceil(obj.number*e_intermediate.number/e_intermediate.output))
                    else:
                        self.moon_material[name].number += ceil(obj.number*e_intermediate.number/e_intermediate.output)
                for name in e_intermediate.fuel_block:
                    obj = e_intermediate.fuel_block[name]
                    if name in self.fuel_block.keys():
                        self.fuel_block[name].number += ceil(obj.number * e_intermediate.number/e_intermediate.output)
                    else:
                        self.fuel_block[name] = fuel_block(name, ceil(obj.number * e_intermediate.number/e_intermediate.output))
        ret = {}
        for k in self.moon_material:
            assert k in moon_material_list, "wrong K"
            obj = self.moon_material[k]
            ret[k] = pad((obj.number)*self.number)
        return ret
    
    def get_fuel_block(self):
        self.get_moon_material()
        ret = {}
        for k in self.fuel_block:
            assert k in fuel_blocks_list
            obj = self.fuel_block[k]
            ret[k] = pad((obj.number)*self.number)
        return ret
    
    def get_planet_material(self):
        ret = {}
        for name in self.planet_material:
            num = self.planet_material[name]
            ret[name] = (num)*self.number
        return ret 

'''
    Usage example:
    Supported ships:
        Ishtar
        Paladin -----> under 0% BPO
        Golem ------> under 5% BPO
        Apocalypse -----> under 10% BPO & 4.5% Sotiyo
        Prospect
        Vargur
        Vagabond
'''
if __name__ == "__main__":
    shipname = "Apocalypse"
    t = ship(shipname, 7)
    
    other_str = t.ship_list[shipname]['mineral'] + '\n\n' + t.ship_list[shipname]['items'] + '\n'
    # Moon material
    mm = t.get_moon_material()
    mm_str = ""
    for k in mm:
        mm_str += k + ' ' + str(mm[k]) + '\n'
    # Fuel blocks
    fb = t.get_fuel_block()
    fb_str = ""
    for k in fb:
        fb_str +=  k + ' ' + str(fb[k]) + '\n'

    # Planet material
    pm = t.get_planet_material()
    pm_str = ""
    for k in pm:
        pm_str += k + ' ' + str(pm[k]) + '\n'

    # Low reaction
    im = t.get_intermediate()
    im_str = ""
    for k in im:
        im_str += k + " " + str(im[k]) + '\n'

    # High reaction
    cp = t.get_composite()
    cp_str = ""
    for k in cp:
        cp_str += k + ' ' + str(cp[k]) + '\n'
    
    # Conponents
    cpn = t.get_components()
    cpn_str = ""
    for k in cpn:
        cpn_str += k + ' ' + str(cpn[k]) + '\n'

    print(mm_str)
    print(fb_str)
    print(other_str)
    print(pm_str)