import re
from math import ceil

from data import *
from util import *

class ship(object):
    def __init__(self) -> None:
        self.composite = {e:0 for e in composite_list}
        self.intermediate = {im:0 for im in intermediate_list}
        self.moon_material = {mm:0 for mm in moon_material_list}
        self.fuel_block = {fb:0 for fb in fuel_blocks_list}
        self.components = {}
        self.mineral = {}
        self.items = {}
        self.planet_material = {}
        
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


class T2ship(ship):
    def __init__(self, shipname, number = 1, stock = None) -> None:
        super().__init__()
        self.ship = None
        if shipname in t2_ship_list.keys():
            self.ship = t2_ship_list[shipname]
        assert self.ship != None, "Not supported T2 ship: {}".format(shipname)
        self.shipname = shipname
        self.number = number
        
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
        
        if stock != None:
            self.set_stock(stock)

        for cmpn in self.components.keys():
            if self.components[cmpn] <= 0:
                continue
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
            if self.composite[cps] <= 0:
                continue
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
            if self.intermediate[imd] <=0 :
                continue
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
    stock = '''Helium Fuel Block	6202
Hydrogen Fuel Block	2903
Nitrogen Fuel Block	8844
Oxygen Fuel Block	14931
Caesarium Cadmide	7884
Carbon Fiber	10518
Carbon Polymers	2869
Ceramic Powder	16682
Crystallite Alloy	4802
Dysporite	1903
Fernite Alloy	14071
Ferrofluid	4799
Fluxed Condensates	1409
Hexite	8421
Hyperflurite	1295
Neo Mercurite	8922
Oxy-Organic Solvents	198
Platinum Technite	7570
Promethium Mercurite	23850
Prometium	2104
Rolled Tungsten Alloy	28671
Silicon Diborite	12899
Solerium	1094
Sulfuric Acid	10257
Thermosetting Polymer	10318
Thulium Hafnite	2725
Titanium Chromide	8528
Vanadium Hafnite	7968
Atmospheric Gases	361287
Cadmium	1140
Caesium	1145
Chromium	379671
Cobalt	29297
Dysprosium	98867
Evaporite Deposits	325565
Hafnium	1335
Hydrocarbons	1014298
Mercury	3410
Neodymium	2546
Platinum	691296
Promethium	42330
Scandium	5141
Silicates	610265
Technetium	119665
Thulium	68395
Titanium	7455
Tungsten	1256
Vanadium	71816
Crystalline Carbonide	1442520
Fermionic Condensates	4934
Fernite Carbide	3961989
Ferrogel	4017
Fullerides	200790
Hypersynaptic Fibers	35969
Nanotransistors	159750
Nonlinear Metamaterials	65942
Phenolic Composites	492576
Photonic Metamaterials	19345
Plasmonic Metamaterials	92209
Pressurized Oxidizers	1341
Reinforced Carbon Fiber	14201
Sylramic Fibers	1823373
Terahertz Metamaterials	49910
Titanium Carbide	3385432
Tungsten Carbide	3359699
Bacteria	315464
Chiral Structures	11948
Oxygen	300063
Proteins	129624
Water	289403
Rocket Fuel	5885'''
    # shipname = "Basilisk"
    # ship1 = T2ship("Huginn", 80)
    # ship2 = T2ship("Scimitar", 30)
    # ship3 = T2ship("Guardian", 30)

    # ship_all = merge(ship1, ship2)
    # ship_all = merge(ship_all, ship3)

    ship1 = T2ship('Paladin', 7, stock)
    # ship2 = T2ship("Paladin", 10)
    # ship_all = merge(ship1, ship2)

    get(ship1, "composite")
    get(ship1, "fuel_block")
    get(ship1, "mineral")
    get(ship1, "planet_material")
    get(ship1, "items")
