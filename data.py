fuel_blocks_list = ["Helium Fuel Block",
                "Hydrogen Fuel Block",
                "Nitrogen Fuel Block",
                "Oxygen Fuel Block"]

moon_material_list = ["Atmospheric Gases", "Cadmium", "Caesium", "Chromium", "Cobalt", "Dysprosium", 
                    "Evaporite Deposits", "Hafnium", "Hydrocarbons", "Mercury", "Neodymium", "Platinum", 
                    "Promethium", "Scandium", "Silicates", "Technetium", "Thulium", "Titanium", "Tungsten", 
                    "Vanadium"]

planetary_material_list = ["Construction Blocks", "Water", "Oxygen", "Chiral Structures", "Bacteria", "Proteins"]

mineral_list = ["Tritanium", "Pyerite", "Mexallon", "Isogen", "Nocxium", "Zydrine", "Megacyte", "Morphite"]

intermediate_list = {
	"Caesarium Cadmide":     "output 200\nCadmium 100\nCaesium 100\nOxygen Fuel Block 5",
	"Carbon Fiber":          "output 200\nHydrocarbons 100\nEvaporite Deposits 100\nHydrogen Fuel Block 5",
	"Carbon Polymers":       "output 200\nHydrocarbons 100\nSilicates 100\nHelium Fuel Block 5",
	"Ceramic Powder":        "output 200\nEvaporite Deposits 100\nSilicates 100\nHydrogen Fuel Block 5",
	"Crystallite Alloy":     "output 200\nCobalt 100\nCadmium 100\nHelium Fuel Block 5",
	"Dysporite":             "output 200\nMercury 100\nDysprosium 100\nHelium Fuel Block 5",
	"Fernite Alloy":         "output 200\nScandium 100\nVanadium 100\nHydrogen Fuel Block 5",
	"Ferrofluid":            "output 200\nHafnium 100\nDysprosium 100\nHydrogen Fuel Block 5",
	"Fluxed Condensates":    "output 200\nNeodymium 100\nThulium 100\nOxygen Fuel Block 5",
	"Hexite":                "output 200\nChromium 100\nPlatinum 100\nNitrogen Fuel Block 5",
	"Hyperflurite":          "output 200\nVanadium 100\nPromethium 100\nNitrogen Fuel Block 5",
	"Neo Mercurite":         "output 200\nMercury 100\nNeodymium 100\nHelium Fuel Block 5",
	"Oxy-Organic Solvents":  "output 10\nHydrocarbons 2000\nAtmospheric Gases 2000\nOxygen Fuel Block 5",
	"Platinum Technite":     "output 200\nPlatinum 100\nTechnetium 100\nNitrogen Fuel Block 5",
	"Promethium Mercurite":  "output 200\nMercury 100\nPromethium 100\nHelium Fuel Block 5",
	"Prometium":             "output 200\nCadmium 100\nPromethium 100\nOxygen Fuel Block 5",
	"Rolled Tungsten Alloy": "output 200\nTungsten 100\nPlatinum 100\nNitrogen Fuel Block 5",
	"Silicon Diborite":      "output 200\nEvaporite Deposits 100\nSilicates 100\nOxygen Fuel Block 5",
	"Solerium":              "output 200\nChromium 100\nCaesium 100\nOxygen Fuel Block 5",
	"Sulfuric Acid":         "output 200\nAtmospheric Gases 100\nEvaporite Deposits 100\nNitrogen Fuel Block 5",
	"Thermosetting Polymer": "output 200\nAtmospheric Gases 100\nSilicates 100\nOxygen Fuel Block 5",
	"Thulium Hafnite":       "output 200\nHafnium 100\nThulium 100\nHydrogen Fuel Block 5",
	"Titanium Chromide":     "output 200\nTitanium 100\nChromium 100\nOxygen Fuel Block 5",
	"Vanadium Hafnite":      "output 200\nVanadium 100\nHafnium 100\nHydrogen Fuel Block 5",
}

composite_list = {
    "Crystalline Carbonide":   "output 10000\nCrystallite Alloy 100\nCarbon Polymers 100\nHelium Fuel Block 5",
	"Fermionic Condensates":   "output 200\nCaesarium Cadmide 100\nDysporite 100\nFluxed Condensates 100\nPrometium 100\nHelium Fuel Block 5",
	"Fernite Carbide":         "output 10000\nFernite Alloy 100\nCeramic Powder 100\nHydrogen Fuel Block 5",
	"Ferrogel":                "output 400\nHexite 100\nHyperflurite 100\nFerrofluid 100\nPrometium 100\nHydrogen Fuel Block 5",
	"Fullerides":              "output 3000\nCarbon Polymers 100\nPlatinum Technite 100\nNitrogen Fuel Block 5",
	"Hypersynaptic Fibers":    "output 750\nSolerium 100\nDysporite 100\nVanadium Hafnite 100\nOxygen Fuel Block 5",
	"Nanotransistors":         "output 1500\nSulfuric Acid 100\nPlatinum Technite 100\nNeo Mercurite 100\nNitrogen Fuel Block 5",
	"Nonlinear Metamaterials": "output 300\nTitanium Chromide 100\nFerrofluid 100\nNitrogen Fuel Block 5",
	"Phenolic Composites":     "output 2200\nSilicon Diborite 100\nCaesarium Cadmide 100\nVanadium Hafnite 100\nOxygen Fuel Block 5",
	"Photonic Metamaterials":  "output 300\nCrystallite Alloy 100\nThulium Hafnite 100\nOxygen Fuel Block 5",
	"Plasmonic Metamaterials": "output 300\nFernite Alloy 100\nNeo Mercurite 100\nHydrogen Fuel Block 5",
	"Pressurized Oxidizers":   "output 200\nCarbon Polymers 200\nSulfuric Acid 200\nOxy-Organic Solvents 1",
	"Reinforced Carbon Fiber": "output 200\nCarbon Fiber 200\nOxy-Organic Solvents 1\nThermosetting Polymer 200",
	"Sylramic Fibers":         "output 6000\nCeramic Powder 100\nHexite 100\nHelium Fuel Block 5",
	"Terahertz Metamaterials": "output 300\nRolled Tungsten Alloy 100\nPromethium Mercurite 100\nHelium Fuel Block 5",
	"Titanium Carbide":        "output 10000\nTitanium Chromide 100\nSilicon Diborite 100\nOxygen Fuel Block 5",
	"Tungsten Carbide":        "output 10000\nRolled Tungsten Alloy 100\nSulfuric Acid 100\nNitrogen Fuel Block 5",
}

component_minmatar_list = {
	"Deflection Shield Emitter":				"output 1\nFernite Carbide 22\nSylramic Fibers 9\nFerrogel 1",
	"Electrolytic Capacitor Unit":				"output 1\nFernite Carbide 27\nFullerides 11\nNanotransistors 1\nPlasmonic Metamaterials 2",
	"Fernite Carbide Composite Armor Plate":	"output 1\nFernite Carbide 44\nSylramic Fibers 11",
	"Ladar Sensor Cluster":						"output 1\nFernite Carbide 22\nNanotransistors 1\nHypersynaptic Fibers 2",
	"Nanomechanical Microprocessor":			"output 1\nFernite Carbide 17\nPhenolic Composites 6\nNanotransistors 2\nPlasmonic Metamaterials 2",
	"Nuclear Reactor Unit":						"output 1\nFernite Carbide 9\nFermionic Condensates 2",
	"Plasma Thruster":							"output 1\nFernite Carbide 13\nPhenolic Composites 3\nFerrogel 1",
	"Thermonuclear Trigger Unit":				"output 1\nFernite Carbide 31\nFullerides 11\nHypersynaptic Fibers 1"
}

component_caldari_list = {
	"Gravimetric Sensor Cluster": 	"output 1\nTitanium Carbide 20\nNanotransistors 1\nHypersynaptic Fibers 2",
	"Graviton Reactor Unit": 		"output 1\nTitanium Carbide 9\nFermionic Condensates 2",
	"Magpulse Thruster": 			"output 1\nTitanium Carbide 12\nPhenolic Composites 3\nFerrogel 1",
	"Quantum Microprocessor":		"output 1\nTitanium Carbide 16\nPhenolic Composites 6\nNanotransistors 2\nNonlinear Metamaterials 2",
	"Scalar Capacitor Unit": 		"output 1\nTitanium Carbide 25\nFullerides 10\nNanotransistors 1\nNonlinear Metamaterials 2",
	"Sustained Shield Emitter": 	"output 1\nTitanium Carbide 20\nSylramic Fibers 9\nFerrogel 1",
	"Titanium Diborite Armor Plate": "output 1\nTitanium Carbide 40\nSylramic Fibers 10",
}

component_gallent_list = {
    "Crystalline Carbonide Armor Plate": "output 1\nCrystalline Carbonide 44\nSylramic Fibers 11",
	"Fusion Reactor Unit":               "output 1\nCrystalline Carbonide 9\nFermionic Condensates 2",
	"Ion Thruster":                      "output 1\nCrystalline Carbonide 13\nPhenolic Composites 3\nFerrogel 1",
	"Magnetometric Sensor Cluster":      "output 1\nCrystalline Carbonide 22\nNanotransistors 1\nHypersynaptic Fibers 2",
	"Oscillator Capacitor Unit":         "output 1\nCrystalline Carbonide 27\nFullerides 11\nNanotransistors 1\nPhotonic Metamaterials 2",
	"Particle Accelerator Unit":         "output 1\nCrystalline Carbonide 31\nFullerides 11\nHypersynaptic Fibers 1",
	"Photon Microprocessor":             "output 1\nCrystalline Carbonide 17\nPhenolic Composites 6\nNanotransistors 2\nPhotonic Metamaterials 2",
	"Plasma Pulse Generator":            "output 1\nCrystalline Carbonide 22\nPhenolic Composites 7\nNanotransistors 2",
	"Pulse Shield Emitter":              "output 1\nCrystalline Carbonide 22\nSylramic Fibers 9\nFerrogel 1",
}

component_amarr_list = {
	"Fusion Thruster": 					"output 1\nTungsten Carbide 12\nPhenolic Composites 3\nFerrogel 1",
	"Radar Sensor Cluster": 			"output 1\nTungsten Carbide 20\nNanotransistors 1\nHypersynaptic Fibers 2",
	"Nanoelectrical Microprocessor": 	"output 1\nTungsten Carbide 16\nPhenolic Composites 6\nNanotransistors 2\nTerahertz Metamaterials 2",
	"Tungsten Carbide Armor Plate": 	"output 1\nTungsten Carbide 40\nSylramic Fibers 10",
	"Antimatter Reactor Unit":	 		"output 1\nTungsten Carbide 9\nFermionic Condensates 2",
	"Tesseract Capacitor Unit": 		"output 1\nTungsten Carbide 25\nFullerides 10\nNanotransistors 1\nTerahertz Metamaterials 2",
	"Linear Shield Emitter": 			"output 1\nTungsten Carbide 20\nSylramic Fibers 9\nFerrogel 1"
}

t2_component_list = dict(component_amarr_list, **component_caldari_list, **component_gallent_list, **component_minmatar_list)

component_T1_list = {
	"Auto-Integrity Preservation Seal": "output 1\nReinforced Carbon Fiber 10\nBacteria 72\nProteins 36",
	"Core Temperature Regulator": "output 1\nPressurized Oxidizers 500\nReinforced Carbon Fiber 500\nChiral Structures 86\nWater 2134",
	"Life Support Backup Unit": "output 1\nReinforced Carbon Fiber 10\nWater 129\nOxygen 171"
}

t2_ship_list = {
				"Marshal":{
					"componentList":"Plasma Thruster 225 \nGravimetric Sensor Cluster 900 \nPhoton Microprocessor 6300 \nTungsten Carbide Armor Plate 18750 \nFusion Reactor Unit 150 \nTesseract Capacitor Unit 2250 \nSustained Shield Emitter 1634",
					"mineral":"Tritanium 11000000 \nPyerite 2500000 \nMexallon 680000 \nIsogen 180000 \nNocxium 40000 \nZydrine 19000 \nMegacyte 7300 \nMorphite 1500",
					"Planetary material": "Construction Blocks 450",
					"items":"Capital Jump Drive 3"
				},
                "Ishtar":
                {
                    "componentList":"Ion Thruster 75\nMagnetometric Sensor Cluster 398\nPhoton Microprocessor 1350\nCrystalline Carbonide Armor Plate 5625\nFusion Reactor Unit 38\nOscillator Capacitor Unit 450\nPulse Shield Emitter 450",
                    "mineral":"Morphite 150",
                    "Planetary material": "Construction Blocks 150",
                    "items":"Vexor 1\nR.A.M.- Starship Tech 18"
                },
				"Kronos":{
					"componentList":"Ion Thruster 357\nMagnetometric Sensor Cluster 820\nPhoton Microprocessor 5700\nCrystalline Carbonide Armor Plate 35625\nFusion Reactor Unit 214\nOscillator Capacitor Unit 2850\nPulse Shield Emitter 3606",
                    "mineral":"Morphite 927",
                    "Planetary material":"Construction Blocks 428",
                    "items":"Megathron 1\nR.A.M.- Starship Tech 29"
				},
				"Sin":{
					"componentList":"Ion Thruster 357\nMagnetometric Sensor Cluster 820\nPhoton Microprocessor 5700\nCrystalline Carbonide Armor Plate 35625\nFusion Reactor Unit 214\nOscillator Capacitor Unit 2850\nPulse Shield Emitter 3606",
                    "mineral":"Morphite 927",
                    "Planetary material":"Construction Blocks 428",
                    "items":"Dominix 1\nR.A.M.- Starship Tech 29"
				},
				"Paladin":
				{
					"componentList":"Fusion Thruster 357\nRadar Sensor Cluster 820\nNanoelectrical Microprocessor 5700\nTungsten Carbide Armor Plate 35625\nAntimatter Reactor Unit 214\nTesseract Capacitor Unit 2850\nLinear Shield Emitter 3606",
					"mineral":"Morphite 975",
                    "Planetary material": "Construction Blocks 450",
                    "items":"Apocalypse 1\nR.A.M.- Starship Tech 30"
				},
				"Redeemer":
				{
					"componentList":"Fusion Thruster 214\nRadar Sensor Cluster 855\nNanoelectrical Microprocessor 5985\nTungsten Carbide Armor Plate 17813\nAntimatter Reactor Unit 143\nTesseract Capacitor Unit 2138\nLinear Shield Emitter 1553",
					"mineral":"Morphite 855",
					"Planetary material":"Construction Blocks 428",
					"items":"Armageddon 1\nR.A.M.- Starship Tech 29",
				},
				"Golem":
				{
					"componentList": "Magpulse Thruster 357\nGravimetric Sensor Cluster 820\nQuantum Microprocessor 5700\nTitanium Diborite Armor Plate 35625\nGraviton Reactor Unit 214\nScalar Capacitor Unit 2850\nSustained Shield Emitter 3606",
					"mineral":"Morphite 927",
					"Planetary material": "Construction Blocks 428",
                    "items":"Raven 1\nR.A.M.- Starship Tech 30"
				},
				"Widow":
				{
					"componentList":"Magpulse Thruster 214\nGravimetric Sensor Cluster 855\nQuantum Microprocessor 5985\nTitanium Diborite Armor Plate 17813\nGraviton Reactor Unit 143\nScalar Capacitor Unit 2138\nSustained Shield Emitter 1553",
					"mineral":"Morphite 855",
					"Planetary material":"Construction Blocks 428",
					"items":"Scorpion 1\nR.A.M.- Starship Tech 29",
				},
				"Prospect":
				{
					"componentList": "Ion Thruster 18\nMagnetometric Sensor Cluster 15\nPhoton Microprocessor 170\nCrystalline Carbonide Armor Plate 200\nFusion Reactor Unit 3\nOscillator Capacitor Unit 42\nPulse Shield Emitter 22",
					"mineral":"Morphite 35",
                    "Planetary material": "Construction Blocks 20",
                    "items":"Venture 1\nR.A.M.- Starship Tech 4"
				},
				"Vargur":
				{
					"componentList": "Plasma Thruster 375\nLadar Sensor Cluster 863\nNanomechanical Microprocessor 6000\nFernite Carbide Composite Armor Plate 37500\nNuclear Reactor Unit 225\nElectrolytic Capacitor Unit 3000\nDeflection Shield Emitter 3795",
					"Planetary material": "Construction Blocks 450",
					"mineral":"Morphite 975",
					"items":"Tempest 1\nR.A.M.- Starship Tech 30"
				},
				"Panther":
				{
					"componentList": "Plasma Thruster 214\nLadar Sensor Cluster 855\nNanomechanical Microprocessor 5985\nFernite Carbide Composite Armor Plate 17813\nNuclear Reactor Unit 143\nElectrolytic Capacitor Unit 2138\nDeflection Shield Emitter 1553",
					"Planetary material": "Construction Blocks 428",
					"mineral":"Morphite 855",
					"items":"Typhoon  1\nR.A.M.- Starship Tech 29"
				},
				"Vagabond":
				{
					"componentList": "Plasma Thruster 75\nLadar Sensor Cluster 398\nNanomechanical Microprocessor 1350\nFernite Carbide Composite Armor Plate 5625\nNuclear Reactor Unit 38\nElectrolytic Capacitor Unit 450\nDeflection Shield Emitter 450",
					"mineral":"Morphite 150",
					"Planetary material": "Construction Blocks 150",
					"items":"Stabber 1\nR.A.M.- Starship Tech 18"
				},      
				"Huginn":
				{
					"componentList": "Plasma Thruster 58\nLadar Sensor Cluster 476\nNanomechanical Microprocessor 1728\nFernite Carbide Composite Armor Plate 3600\nNuclear Reactor Unit 29\nElectrolytic Capacitor Unit 360\nDeflection Shield Emitter 288",
					"mineral": "Morphite 144",
					"Planetary material":"Construction Blocks 72",
					"items":"Bellicose 1\nR.A.M.- Starship Tech 18"
				},
				"Cerberus":
				{
					"componentList":"Magpulse Thruster 75\nGravimetric Sensor Cluster 398\nQuantum Microprocessor 1350\nTitanium Diborite Armor Plate 5625\nGraviton Reactor Unit 38\nScalar Capacitor Unit 450\nSustained Shield Emitter 450",
					"mineral":"Morphite 150",
					"Planetary material":"Construction Blocks 150",
					"items":"Caracal 1\nR.A.M.- Starship Tech 18"
				},
				"Scimitar":
				{
					"componentList":"Plasma Thruster 75\nLadar Sensor Cluster 263\nNanomechanical Microprocessor 1800\nFernite Carbide Composite Armor Plate 2250\nNuclear Reactor Unit 23\nElectrolytic Capacitor Unit 750\nDeflection Shield Emitter 150",
					"Planetary material":"Construction Blocks 75",
					"mineral":"Morphite 90",
					"items":"Scythe 1\nR.A.M.- Starship Tech 12",
				},
				"Retribution":
				{
					"componentList":"Fusion Thruster 23\nRadar Sensor Cluster 30\nNanoelectrical Microprocessor 135\nTungsten Carbide Armor Plate 900\nAntimatter Reactor Unit 8\nTesseract Capacitor Unit 90\nLinear Shield Emitter 30",
					"Planetary material":"Construction Blocks 38",
					"mineral":"Morphite 45",
					"items":"Punisher 1\nR.A.M.- Starship Tech 6",

				},
				"Sabre":
				{
					"componentList":"Plasma Thruster 60\nLadar Sensor Cluster 75\nNanomechanical Microprocessor 360\nFernite Carbide Composite Armor Plate 1500\nNuclear Reactor Unit 15\nElectrolytic Capacitor Unit 150\nDeflection Shield Emitter 38",
					"mineral":"Morphite 15",
					"Planetary material":"Construction Blocks 23",
					"items":"R.A.M.- Starship Tech 9\nThrasher 1",
				},
				"Arazu":{
					"componentList":"Ion Thruster 57\nMagnetometric Sensor Cluster 495\nPhoton Microprocessor 1800\nCrystalline Carbonide Armor Plate 3750\nFusion Reactor Unit 30\nOscillator Capacitor Unit 375\nPulse Shield Emitter 300",
					"Planetary material":"Construction Blocks 75",
					"mineral":"Morphite 150",
					"items":"Celestis 1\nR.A.M.- Starship Tech 18",
				},
				"Guardian":{
					"componentList":"Fusion Thruster 75\nRadar Sensor Cluster 263\nNanoelectrical Microprocessor 1800\nTungsten Carbide Armor Plate 2250\nAntimatter Reactor Unit 23\nTesseract Capacitor Unit 750\nLinear Shield Emitter 150",
					"mineral":"Morphite 90",
					"Planetary material":"Construction Blocks 75",
					"items":"Augoror 1\nR.A.M.- Starship Tech 12",
				},
				"Basilisk":
				{
					"componentList":"Magpulse Thruster 75\nGravimetric Sensor Cluster 263\nQuantum Microprocessor 1800\nTitanium Diborite Armor Plate 2250\nGraviton Reactor Unit 23\nScalar Capacitor Unit 750\nSustained Shield Emitter 150",
					"mineral":"Morphite 90",
					"Planetary material":"Construction Blocks 75",
					"items":"Osprey 1\nR.A.M.- Starship Tech 12",
				},


}

battle_ship_list = {
				"Apocalypse":
				{
					"componentList":"Auto-Integrity Preservation Seal 180\nCore Temperature Regulator 1\nLife Support Backup Unit 90",
					"mineral": "Tritanium 7200000\nPyerite 3600000\nMexallon 540000\nIsogen 360000\nNocxium 10800\nZydrine 5400\nMegacyte 2700",
					"Planetary material": "",
					"items": ""
				},
				"Raven":
				{
					"componentList":"Auto-Integrity Preservation Seal 180\nCore Temperature Regulator 1\nLife Support Backup Unit 90",
					"mineral": "Tritanium 7200000\nPyerite 3600000\nMexallon 540000\nIsogen 360000\nNocxium 10800\nZydrine 5400\nMegacyte 2700",
					"Planetary material": "",
					"items": ""
				},
				"Tempest":
				{
					"componentList":"Auto-Integrity Preservation Seal 180\nCore Temperature Regulator 1\nLife Support Backup Unit 90",
					"mineral": "Tritanium 7200000\nPyerite 3600000\nMexallon 540000\nIsogen 360000\nNocxium 10800\nZydrine 5400\nMegacyte 2700",
					"Planetary material": "",
					"items": ""
				}
}