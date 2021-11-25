# eveHelper
eve online T2 制造商助手.

欢迎在游戏内的一切捐赠。接收角色名是：

        phan ii

## Notice

项目还在开发中，目前没有考虑自定义材料的节省效率。

目前支持的船型:

        Ishtar （伊什塔级）
        
        Paladin （帕拉丁级）
        
        Apocalypse （灾难级）
        
        Prospect（掘金者级）

## 功能

给定船型和数目，输出制造所需要的月矿，低反产物，高反产物，矿物，行星产物，燃料块消耗。

例子(helper.py 文件里包含这部分代码):

```

if __name__ == "__main__":
    # 船名Ishtar
    shipname = "Ishtar"
    # 数目5
    t = ship(shipname, 5)
    
    # 获取矿物消耗以及制造所需要的物品
    other_str = t.ship_list[shipname]['mineral'] + '\n\n' + t.ship_list[shipname]['items'] + '\n'
    # 获取月矿数
    mm = t.get_moon_material()
    mm_str = ""
    for k in mm:
        mm_str += k + ' ' + str(mm[k]) + '\n'
    # 获取燃料块消耗
    fb = t.get_fuel_block()
    fb_str = ""
    for k in fb:
        fb_str +=  k + ' ' + str(fb[k]) + '\n'

    # 获取行星产物数据
    pm = t.get_planet_material()
    pm_str = ""
    for k in pm:
        pm_str += k + ' ' + str(pm[k]) + '\n'

    # 获取低反数据
    im = t.get_intermediate()
    im_str = ""
    for k in im:
        im_str += k + " " + str(im[k]) + '\n'

    # 获取高反数据
    cp = t.get_composite()
    cp_str = ""
    for k in cp:
        cp_str += k + ' ' + str(cp[k]) + '\n'
    
    # 获取组件数据
    cpn = t.get_components()
    cpn_str = ""
    for k in cpn:
        cpn_str += k + ' ' + str(cpn[k]) + '\n'

    # 输出高反数据，燃料块消耗，矿物以及所需要的“物品”，还有行星产物。
    print(cp_str)
    print(fb_str)
    print(other_str)
    print(pm_str)
```

## 用法

1. 编辑船型，数目:

  例如，如果需要造5条Ishtar的话，修改helper.py中对应的船名和数目。如下： 
  ```
  if __name__ == "__main__":
    shipname = "Ishtar"
    t = ship(shipname, 5)
  ```
2. 在命令行中运行脚本
  ```
  python .\helper.py
  ```

## 环境

1. 需要安装python

2. 建议使用微软的 Visual Studio Code 编辑器。使用control键加~键可以一键调出/调回命令行终端。可以在vscode的命令行终端里执行`  python .\helper.py `这种命令。
