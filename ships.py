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
        self.stock = {}
        
    def set_stock(self, str):
        for e in str.split('\n'):
            name = re.search(r'[a-zA-Z -.]+', e).group(0).strip()
            num = int(re.search(r'\d+', e).group(0))
            self.stock[name] = num
            # if name in self.moon_material:
            #     self.stock[name] = num
            # elif name in self.intermediate:
            #     self.stock[name] = num
            # elif name in self.composite:
            #     self.stock[name] = num
            # elif name in self.components:
            #     self.stock[name] = num
            # elif name in self.mineral:
            #     self.stock[name] = num
            # elif name in self.planet_material:
            #     self.stock[name] = num
            # elif name in self.fuel_block:
            #     self.stock[name] = num
            # elif name in self.items:
            #     self.stock[name] = num
    
    def sub_stock(self, num, name):
        if name not in self.stock:
            return num
        if self.stock[name] > num:
            self.stock[name] -= num
            return 0
        else:
            self.stock[name] = 0
            return num - self.stock[name]


class T2ship(ship):
    def __init__(self, stock = None) -> None:
        super().__init__()
        self.ship = None
        if stock != None:
            self.set_stock(stock)
    
    def addShip(self, shipname, number = 1):
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
                        if name not in self.components:
                            self.components[name] = 0
                        self.components[name] += num * self.number
                        self.components[name] = self.sub_stock(self.components[name], name)
                    elif "mineral" == k:
                        if name not in self.mineral:
                            self.mineral[name] = 0
                        self.mineral[name] += num * self.number
                        self.mineral[name] = self.sub_stock(self.mineral[name], name)
                    elif "items" == k:
                        if name not in self.items:
                            self.items[name] = 0
                        self.items[name] += num * self.number
                        self.items[name] = self.sub_stock(self.items[name], name)
                    elif "Planetary material" == k:
                        if name not in self.planet_material:
                            self.planet_material[name] = 0
                        self.planet_material[name] += num * self.number
                        self.planet_material[name] = self.sub_stock(self.planet_material[name], name)
                    else:
                        raise Exception("unsupported thing in T2ships:>> "+name)

    def compute(self):
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
                    self.composite[name] = self.sub_stock(self.composite[name], name)
        
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
                    self.fuel_block[name] = self.sub_stock(self.fuel_block[name], name)
                else:
                    self.intermediate[name] += num * multiplier
                    self.intermediate[name] = self.sub_stock(self.intermediate[name], name)
        
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
                    self.fuel_block[name] = self.sub_stock(self.fuel_block[name], name)
                else:
                    self.moon_material[name] += num * multiplier
                    self.moon_material[name] = self.sub_stock(self.moon_material[name], name)
        
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
    stock = '''Antimatter Reactor Unit	1126
Auto-Integrity Preservation Seal	1313
Crystalline Carbonide Armor Plate	563
Deflection Shield Emitter	13183
Electrolytic Capacitor Unit	33762
Fernite Carbide Composite Armor Plate	176180
Fusion Reactor Unit	3
Fusion Thruster	3315
Gravimetric Sensor Cluster	343
Graviton Reactor Unit	91
Ion Thruster	6
Ladar Sensor Cluster	23646
Life Support Backup Unit	49
Linear Shield Emitter	10171
Magnetometric Sensor Cluster	47
Magpulse Thruster	154
Nanoelectrical Microprocessor	62984
Nanomechanical Microprocessor	111038
Nuclear Reactor Unit	1571
Oscillator Capacitor Unit	49
Photon Microprocessor	90
Plasma Thruster	4048
Pulse Shield Emitter	28
Quantum Microprocessor	2387
Radar Sensor Cluster	9368
Scalar Capacitor Unit	1190
Sustained Shield Emitter	1530
Tesseract Capacitor Unit	27714
Titanium Diborite Armor Plate	14932
Tungsten Carbide Armor Plate	125663
R.A.M.- Electronics	100
R.A.M.- Shield Tech	100
R.A.M.- Starship Tech	8148
Isogen	4764272
Megacyte	411896
Mexallon	22451467
Morphite	70672
Nocxium	283034
Pyerite	299149334
Tritanium	65141898
Zydrine	1822207
Construction Blocks	52434
Auto-Integrity Preservation Seal	1260
R.A.M.- Ammunition Tech	6000
Crystalline Carbonide	1442520
Fermionic Condensates	2268
Fernite Carbide	3961989
Ferrogel	402
Fullerides	17342
Hypersynaptic Fibers	25746
Nanotransistors	61637
Nonlinear Metamaterials	65942
Phenolic Composites	266985
Photonic Metamaterials	19345
Plasmonic Metamaterials	92209
Pressurized Oxidizers	2617
Reinforced Carbon Fiber	12908
Sylramic Fibers	233988
Terahertz Metamaterials	19802
Titanium Carbide	3385432
Tungsten Carbide	870923
Bacteria	201748
Chiral Structures	10762
Oxygen	228991
Proteins	72765
Water	234913
Rocket Fuel	5885
Pressurized Oxidizers	3600
Reinforced Carbon Fiber	44800
Helium Fuel Block	16034
Hydrogen Fuel Block	2818
Nitrogen Fuel Block	14873
Oxygen Fuel Block	22702
Liquid Ozone	10236
Caesarium Cadmide	7884
Carbon Fiber	12288
Carbon Polymers	116164
Ceramic Powder	48946
Crystallite Alloy	143802
Dysporite	1903
Fernite Alloy	14071
Ferrofluid	7064
Fluxed Condensates	1409
Hexite	55950
Hyperflurite	6360
Neo Mercurite	8922
Oxy-Organic Solvents	408
Platinum Technite	7180
Promethium Mercurite	66822
Prometium	7969
Rolled Tungsten Alloy	188625
Silicon Diborite	12899
Solerium	1094
Sulfuric Acid	119124
Thermosetting Polymer	12088
Thulium Hafnite	30925
Titanium Chromide	8528
Vanadium Hafnite	7968
Atmospheric Gases	156204
Cadmium	38132
Caesium	7200
Chromium	345203
Cobalt	36930
Dysprosium	94777
Evaporite Deposits	225011
Hafnium	62060
Hydrocarbons	833916
Mercury	11473
Neodymium	11300
Platinum	524021
Promethium	34227
Scandium	5141
Silicates	504517
Technetium	119665
Thulium	54666
Titanium	112455
Tungsten	153481
Vanadium	66362'''
    # shipname = "Basilisk"
    # ship1 = T2ship("Huginn", 80)
    # ship2 = T2ship("Scimitar", 30)
    # ship3 = T2ship("Guardian", 30)

    # ship_all = merge(ship1, ship2)
    # ship_all = merge(ship_all, ship3)

    ship1 = T2ship()
    ship1.set_stock(stock)
    # ship1.addShip("Kronos", 7)
    ship1.addShip("Paladin", 7)
    # ship1.addShip('Golem', 7)
    ship1.compute()
    
    # ship.set_stock(stock)

    get(ship1, "composite")
    get(ship1, "fuel_block")
    get(ship1, "mineral")
    get(ship1, "planet_material")
    get(ship1, "items")
