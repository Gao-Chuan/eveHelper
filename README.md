# eveHelper
eve online T2 industry helper.

[中文说明](README_zh_cn.md)

In-game donations are very welcome. If you would like to donate, the receiving account is: 

        phan ii

## Notice

The development has not finished yet. Currently this project does not consider the material efficiency. Plase double check the coresponding data with your own blueprint in [data.py](data.py)

Currently supported ships' name:

        Check t2_ship_list in ./data.py

## Functionality

Extract the 'moon material', 'low reaction material', 'high reaction material', 'mineral', 'planet material', 'Fuel blocks' comsumed by given ship's name.

Set up your current stock, and output what else materials you need to buy. Use the api ship.get("what you want to see")

Example(the code is included in helper.py):

```

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

```

## Usage

1. edit the ship name and the number in ./ships.py:

  For example, if you want to build 80 Huginn, edit the helper.py like this: 
  ```
  if __name__ == "__main__":
    shipname = "Huginn"
    ship = T2ship(shipname, 80)
  ```

2. Run the script
  ```
  python .\ships.py
  ```


