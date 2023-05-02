# AddRecipes
Generate Minecraft EnderIO AlloySmelter recipes for blocks and singularities.

## Introduction
Have you ever found many problems arising during playing a Minecraft modpack with [Avaritia](https://www.curseforge.com/minecraft/mc-mods/avaritia) and its addons or linkages, such as [AOBO Singularities](https://www.curseforge.com/minecraft/mc-mods/aobd-singularities), [Universal Singularities](https://legacy.curseforge.com/minecraft/mc-mods/universal-singularities), [Industrial Upgrade](https://www.curseforge.com/minecraft/mc-mods/industrial-upgrade) and so on, that many singularities can't be crafted because of recipe conflicts or missing recipes of metal blocks? This project is coming to add some [EnderIO](https://www.enderio.com/) AlloySmelter recipes to avoid these problems! Perhaps, it is a good way to make these singularities craftable without other mods focusing on modifying recipes.
There are two Python programs to Add recipes. One, automatically generate recipes that allow 9 ingots to be smelted into a block corresponding to the ingot according to an OreDict CSV file generated by [NEI Integration](https://www.curseforge.com/minecraft/mc-mods/nei-integration) mod; another, automatically generate recipes that can make singularities with recipe conflicts to transform between each other.

## How to use

### Add recipes for blocks
- Use [NEI Integration](https://www.curseforge.com/minecraft/mc-mods/nei-integration) mod to dump `oredict.csv` for your modpack;
- This program imposes Kayakumeshi (Variety Mixed Rice) from [Apple Milk Tea](https://www.curseforge.com/minecraft/mc-mods/applemilktea2) as an additional input in the recipe, change it if you want;
- Run `addblockrecipes.py` with Python and input the entire path of `oredict.csv`;
>`python addblockrecipes.py
- Copy contents in the generated file `blockrecipesoutput.xml` into `config/enderio/AlloySmelterRecipes_User.xml`.

### Add recipes for singularities with recipe conflicts
- Modify correspondences of such singularities in the singularities dictionary in `addsingularityrecipes.py`;
- Run `addsingularityrecipes.py` with Python;
- Copy contents in the generated file `singularityrecipesoutput.xml` into `config/enderio/AlloySmelterRecipes_User.xml`.
