# eveHelper
eve online T2 industry helper.

In-game donations are very welcome. If you would like to donate, the receiving account is: 

        phan ii

## Notice

Currently supported ships' name:

        Ishtar
        
        Paladin
        
        Apocalypse
        
        Prospect

## Functionality

Extract the 'moon material', 'low reaction material', 'high reaction material', 'mineral', 'planet material', 'Fuel blocks' comsumed by given ship's name.

Example:

```

if __name__ == "__main__":
    shipname = "Ishtar"
    t = ship(shipname, 5)
    
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

    # print high reaction
    print(cp_str)
    # print fuel blocks
    print(fb_str)
    # print items & minerals
    print(other_str)
    # print planet materials
    print(pm_str)
```

## Usage

1. edit the ship name and the number:
  For example: 
  ```
  if __name__ == "__main__":
    shipname = "Ishtar"
    t = ship(shipname, 5)
  ```
2. Run the script
  ```
  python .\helper.py
  ```


