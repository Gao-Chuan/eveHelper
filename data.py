fuel_blocks_list = ["Helium Fuel Block",
                "Hydrogen Fuel Block",
                "Nitrogen Fuel Block",
                "Oxygen Fuel Block"]

moon_material_list = ["Atmospheric Gases", "Cadmium", "Caesium", "Chromium", "Cobalt", "Dysprosium", 
                    "Evaporite Deposits", "Hafnium", "Hydrocarbons", "Mercury", "Neodymium", "Platinum", 
                    "Promethium", "Scandium", "Silicates", "Technetium", "Thulium", "Titanium", "Tungsten", 
                    "Vanadium"]

planetary_material_list = ["Construction Blocks", "Water", "Oxygen", "Chiral Structures", "Bacteria", "Proteins"]

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

component_T1_list = {
	"Auto-Integrity Preservation Seal": "output 1\nReinforced Carbon Fiber 10\nBacteria 72\nProteins 36",
	"Core Temperature Regulator": "output 1\nPressurized Oxidizers 500\nReinforced Carbon Fiber 500\nChiral Structures 86\nWater 2134",
	"Life Support Backup Unit": "output 1\nReinforced Carbon Fiber 10\nWater 129\nOxygen 171"
}

t2_ship_list = {
                "Ishtar":
                {
                    "componentList":"Ion Thruster 75\nMagnetometric Sensor Cluster 398\nPhoton Microprocessor 1350\nCrystalline Carbonide Armor Plate 5625\nFusion Reactor Unit 38\nOscillator Capacitor Unit 450\nPulse Shield Emitter 450",
                    "mineral":"Morphite 150",
                    "Planetary material": "Construction Blocks 150",
                    "items":"Vexor 1\nR.A.M.- Starship Tech 18"
                },
				"Paladin":
				{
					"componentList":"Fusion Thruster 375\nRadar Sensor Cluster 863\nNanoelectrical Microprocessor 6000\nTungsten Carbide Armor Plate 37500\nAntimatter Reactor Unit 225\nTesseract Capacitor Unit 3000\nLinear Shield Emitter 3795",
					"mineral":"Morphite 975",
                    "Planetary material": "Construction Blocks 450",
                    "items":"Apocalypse 1\nR.A.M.- Starship Tech 30"
				},
				"Prospect":
				{
					"componentList": "Ion Thruster 18\nMagnetometric Sensor Cluster 15\nPhoton Microprocessor 170\nCrystalline Carbonide Armor Plate 200\nFusion Reactor Unit 3\nOscillator Capacitor Unit 42\nPulse Shield Emitter 22",
					"mineral":"Morphite 35",
                    "Planetary material": "Construction Blocks 20",
                    "items":"Venture 1\nR.A.M.- Starship Tech 4"
				},
            }

battle_ship_list = {
				"Apocalypse":
				{
					"componentList":"Auto-Integrity Preservation Seal 180\nCore Temperature Regulator 1\nLife Support Backup Unit 90",
					"mineral": "Tritanium 7200000\nPyerite 3600000\nMexallon 540000\nIsogen 360000\nNocxium 10800\nZydrine 5400\nMegacyte 2700",
					"Planetary material": "",
					"items": ""
				}
}