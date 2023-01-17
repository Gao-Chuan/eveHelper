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
        self.components = {cmp:0 for cmp in t2_component_list}
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
        elif self.stock[name] > num:
            self.stock[name] -= num
            return 0
        elif self.stock[name] <= num:
            ret = num - self.stock[name]
            self.stock[name] = 0
            return ret


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
    stock = '''Helium Fuel Block	7878
Hydrogen Fuel Block	6480
Nitrogen Fuel Block	8627
Oxygen Fuel Block	7483
Liquid Ozone	4996
Caesarium Cadmide	3792
Carbon Fiber	2373
Carbon Polymers	107746
Ceramic Powder	55624
Crystallite Alloy	18385
Dysporite	2024
Fernite Alloy	14071
Ferrofluid	8662
Fluxed Condensates	1730
Hexite	42970
Hyperflurite	7102
Neo Mercurite	9383
Oxy-Organic Solvents	405
Platinum Technite	8009
Promethium Mercurite	66822
Prometium	4232
Rolled Tungsten Alloy	80749
Silicon Diborite	14926
Solerium	1094
Sulfuric Acid	109293
Thermosetting Polymer	2173
Thulium Hafnite	32078
Titanium Chromide	22224
Vanadium Hafnite	8355
Atmospheric Gases	90385
Cadmium	45780
Caesium	1845
Chromium	211593
Cobalt	34609
Dysprosium	80279
Evaporite Deposits	69844
Hafnium	7732
Hydrocarbons	732245
Mercury	2515
Neodymium	21918
Platinum	520985
Promethium	31387
Scandium	20987
Silicates	308485
Technetium	112902
Thulium	38917
Titanium	44945
Tungsten	171764
Vanadium	58932
Compressed Otavite	35
Compressed Lavish Otavite	75
Cadmium	26840
Atmospheric Gases	6888
Compressed Monazite	57
Neodymium	46955
Chromium	21343
Tungsten	42686
Evaporite Deposits	42686
Compressed Loparite	48
Compressed Bountiful Loparite	71
Promethium	27779
Platinum	12737
Scandium	25302
Hydrocarbons	25302
R.A.M.- Ammunition Tech	6000
Crystalline Carbonide	3513467
Fermionic Condensates	3863
Fernite Carbide	3954729
Ferrogel	1653
Fullerides	65990
Hypersynaptic Fibers	6318
Nanotransistors	80719
Nonlinear Metamaterials	84663
Phenolic Composites	88898
Photonic Metamaterials	37766
Plasmonic Metamaterials	92209
Pressurized Oxidizers	100
Reinforced Carbon Fiber	49541
Sylramic Fibers	1067516
Terahertz Metamaterials	19802
Titanium Carbide	2456379
Tungsten Carbide	2185435
Bacteria	81174
Chiral Structures	8136
Oxygen	82447
Proteins	87477
Water	122378
Rocket Fuel	5885
Metal Scraps	1
Antimatter Reactor Unit	815
Auto-Integrity Preservation Seal	6389
Core Temperature Regulator	10
Crystalline Carbonide Armor Plate	249939
Deflection Shield Emitter	13
Electrolytic Capacitor Unit	23042
Fernite Carbide Composite Armor Plate	42212
Fusion Reactor Unit	1501
Fusion Thruster	335
Gravimetric Sensor Cluster	6083
Graviton Pulse Generator	600
Graviton Reactor Unit	1589
Ion Thruster	2505
Ladar Sensor Cluster	20562
Life Support Backup Unit	774
Linear Shield Emitter	4903
Magnetometric Sensor Cluster	5787
Magpulse Thruster	2653
Nanoelectrical Microprocessor	14753
Nanomechanical Microprocessor	89602
Nuclear Reactor Unit	767
Oscillator Capacitor Unit	19999
Photon Microprocessor	39990
Plasma Thruster	2708
Pulse Shield Emitter	25270
Quantum Microprocessor	42287
Radar Sensor Cluster	2429
Scalar Capacitor Unit	21140
Sustained Shield Emitter	26772
Tesseract Capacitor Unit	3594
Titanium Diborite Armor Plate	264308
Tungsten Carbide Armor Plate	73612
R.A.M.- Electronics	100
R.A.M.- Shield Tech	100
R.A.M.- Starship Tech	7797
Isogen	4697472
Megacyte	58763
Mexallon	11312685
Morphite	59349
Nocxium	115514
Pyerite	214144403
Tritanium	81381109
Zydrine	1412941
Self-Harmonizing Power Core	30
Construction Blocks	47208
Nanites	42
Apocalypse	1
Megathron	7
Raven	7
Augoror	30
Bellicose	8
Scythe	30
Stabber	36
Vexor	9
Cormorant	10
Punisher	34'''
    # shipname = "Basilisk"
    # ship1 = T2ship("Huginn", 80)
    # ship2 = T2ship("Scimitar", 30)
    # ship3 = T2ship("Guardian", 30)

    # ship_all = merge(ship1, ship2)
    # ship_all = merge(ship_all, ship3)

    ship1 = T2ship()
    ship1.set_stock(stock)
    ship1.addShip("Kronos", 7)
    ship1.addShip("Paladin", 7)
    ship1.addShip('Golem', 7)
    ship1.addShip('Vargur', 10)
    ship1.addShip('Golem', 10)
    ship1.addShip("Paladin", 10)
    ship1.compute()
    
    # ship.set_stock(stock)

    get(ship1, "moon_material")
    get(ship1, "fuel_block")
    get(ship1, "mineral")
    get(ship1, "planet_material")
    get(ship1, "items")

