import re
from math import ceil

from data import *
from util import pad

class T2ship(object):
    def __init__(self, shipname, number = 1) -> None:
        super().__init__()
        self.ship = None
        if shipname in t2_ship_list.keys():
            self.ship = t2_ship_list[shipname]
        assert self.ship != None, "Not supported T2 ship: {}".format(shipname)
        self.shipname = shipname
        self.number = number
        self.components = {}
        self.mineral = {}
        self.items = {}
        self.planet_material = {}
        for k in ["componentList", "mineral", 'Planetary material', "items"]:
            if self.ship[k] != '':
                for e in self.ship[k].split('\n'):
                    name = re.search(r'[a-zA-Z -.]+', e).group(0)[:-1]
                    num = int(re.search(r'\d+', e).group(0))
                    if "componentList" == k:
                        self.components[name] = num * self.number
                    elif "mineral" == k:
                        self.mineral[name] = num * self.number
                    elif "items" == k:
                        self.items[name] = num * self.number
                    elif "Planetary material" == k:
                        self.planet_material[name] = num * self.number
                    else:
                        raise Exception("unsupported thing in T2ships:>> "+name)

        self.composite = {e:0 for e in composite_list}
        self.intermediate = {im:0 for im in intermediate_list}
        self.moon_material = {mm:0 for mm in moon_material_list}
        self.fuel_block = {fb:0 for fb in fuel_blocks_list}

        for cmpn in self.components.keys():
            output = None
            multiplier = None
            for each in t2_component_list[cmpn].split('\n'):
                name = re.search(r'[a-zA-Z ]+', each).group(0)[:-1]
                num = int(re.search(r'\d+', each).group(0))
                if 'output' == name:
                    output = num
                    multiplier = ceil(self.components[cmpn] / output)
                else:
                    self.composite[name] += num * multiplier
        
        for cps in self.composite.keys():
            output = None
            multiplier = None
            for each in composite_list[cps].split('\n'):
                name = re.search(r'[a-zA-Z -]+', each).group(0)[:-1]
                num = int(re.search(r'\d+', each).group(0))
                if 'output' == name:
                    output = num
                    multiplier = ceil(self.composite[cps] / output)
                elif 'Fuel Block' in name:
                    self.fuel_block[name] += num * multiplier
                else:
                    self.intermediate[name] += num * multiplier
        
        for imd in self.intermediate.keys():
            output = None
            multiplier = None
            for each in intermediate_list[imd].split('\n'):
                name = re.search(r'[a-zA-Z ]+', each).group(0)[:-1]
                num = int(re.search(r'\d+', each).group(0))
                if 'output' == name:
                    output = num
                    multiplier = ceil(self.intermediate[imd] / output)
                elif 'Fuel Block' in name:
                    self.fuel_block[name] += num * multiplier
                else:
                    self.moon_material[name] += num * multiplier
    
    def set_stock(self, str):
        for e in str.split('\n'):
            name = re.search(r'[a-zA-Z -.]+', e).group(0).strip()
            num = int(re.search(r'\d+', e).group(0))
            if name in self.moon_material:
                self.moon_material[name] -= num
            elif name in self.intermediate:
                self.intermediate[name] -= num
            elif name in self.composite:
                self.composite[name] -= num
            elif name in self.components:
                self.components[name] -= num
            elif name in self.mineral:
                self.mineral[name] -= num
            elif name in self.planet_material:
                self.planet_material[name] -= num
            elif name in self.fuel_block:
                self.fuel_block[name] -= num
            elif name in self.items:
                self.items[name] -= num
            
        
    def get(self, key):
        obj = None
        if key == "moon_material":
            obj = self.moon_material
        elif key == "intermediate":
            obj = self.intermediate
        elif key == "composite":
            obj = self.composite
        elif key == "components":
            obj = self.components
        elif key == "fuel_block":
            obj = self.fuel_block
        elif key == "mineral":
            obj = self.mineral
        elif key == "planet_material":
            obj = self.planet_material
        elif key == "items":
            obj = self.items
        else:
            raise Exception("get key error:>>{}".format(key))

        for e in obj:
            if obj[e] > 0:
                print(e + ' ' + str(obj[e]))


        
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
        Huginn -----> 4% BPO
'''
if __name__ == "__main__":
    shipname = "Huginn"
    ship = T2ship(shipname, 80)

    stock = '''Atmospheric Gases	403056
Cadmium	37781
Caesium	13862
Chromium	431567
Cobalt	29297
Dysprosium	12888
Evaporite Deposits	547754
Hafnium	6789
Hydrocarbons	1027150
Mercury	7512
Neodymium	2413
Platinum	815728
Promethium	4849
Scandium	2421
Silicates	803537
Technetium	152965
Thulium	1713
Titanium	7455
Tungsten	19400
Vanadium	303840
Helium Fuel Block	20154
Hydrogen Fuel Block	29045
Nitrogen Fuel Block	22868
Oxygen Fuel Block	23196
Morphite	34801
Construction Blocks	11798
R.A.M.- Starship Tech	9378'''
    ship.set_stock(stock)
    ship.get("moon_material")
    ship.get("fuel_block")
    ship.get("mineral")
    ship.get("planet_material")
    ship.get("items")
