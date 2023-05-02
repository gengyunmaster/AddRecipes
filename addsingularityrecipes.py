i = 0
recipes = ''
singularities = {
    'industrialupgrade,avaritia_iu_singularity,0': 'singularityMikhail',
    'industrialupgrade,avaritia_iu_singularity,1': 'universalsingularities,universal.general.singularity,0',
    'industrialupgrade,avaritia_iu_singularity,2': 'singularityVanady',
    'industrialupgrade,avaritia_iu_singularity,3': 'universalsingularities,universal.general.singularity,13',
    'industrialupgrade,avaritia_iu_singularity,4': 'universalsingularities,universal.tinkersConstruct.singularity,3',
    'industrialupgrade,avaritia_iu_singularity,5': 'universalsingularities,universal.general.singularity,6',
    'industrialupgrade,avaritia_iu_singularity,6': 'thermsingul,Thermal Singularity,0',
    'industrialupgrade,avaritia_iu_singularity,7': 'universalsingularities,universal.general.singularity,12',
    'industrialupgrade,avaritia_iu_singularity,8': 'singularityChromium',
    'industrialupgrade,avaritia_iu_singularity,9': 'singularitySpinel',
    'industrialupgrade,avaritia_iu_singularity,10': 'universalsingularities,universal.general.singularity,15',
    'industrialupgrade,avaritia_iu_singularity,11': 'singularityManganese',
    'industrialupgrade,avaritia_iu_singularity,12': 'universalsingularities,universal.general.singularity,5',
    'industrialupgrade,avaritia_iu_singularity,14': 'universalsingularities,universal.general.singularity,4',
    'industrialupgrade,avaritia_iu_singularity,15': 'singularityIridium',
    'industrialupgrade,avaritia_iu_singularity,16': 'singularityGermanium'
}

def generateoredictline(oredict):
    line = 'oreDictionary="' + oredict + '" number="1"'
    return line

def generateitemline(itemori):
    item = itemori.split(',')
    modid = item[0]
    name = item[1]
    meta = item[2]
    line = 'modID="' + modid + '" itemName="' + name + '" itemMeta="' + meta + '" number="1"'
    return line

def generateline(o):
    if ',' in o:
        return generateitemline(o)
    else:
        return generateoredictline(o)

def generaterecipe(inp, outp, index):
    recipe = '    <recipe name="Singularity Transformation ' + str(index) + '" energyCost="10000" >\n      <input>\n        <itemStack ' + generateline(inp) + ' />\n        <itemStack modID="Thaumcraft" itemName="FocusTrade" itemMeta="0" number="1" />\n      </input>\n      <output>\n        <itemStack ' + generateline(outp) + ' exp="0.5" />\n      </output>\n    </recipe>\n'
    return recipe

def exchangedict(d):
    return {d[key]: key for key in d.keys()}

for key in singularities:
    i += 1
    recipes += generaterecipe(key, singularities[key], i)

singularities_new = exchangedict(singularities)

for key in singularities_new:
    i += 1
    recipes += generaterecipe(key, singularities_new[key], i)

with open(file = 'singularityrecipesoutput.xml', mode = 'a', encoding = 'utf-8') as fileobj:
    fileobj.write('<!--\n  Added ' + str(i) + ' recipes! Please copy them into "config/enderio/AlloySmelterRecipes_User.xml".\n-->\n' + recipes)
