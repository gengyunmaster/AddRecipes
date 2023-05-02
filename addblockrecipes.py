import codecs
import chardet
import csv


input_file = input("OreDict CSV File: ")

with open(input_file, 'rb') as fo:
    rawdata = fo.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

with codecs.open(input_file, 'r', encoding, errors='ignore') as fo:
    content = fo.read()

content = content.encode('utf-8').decode('utf-8-sig').replace('\r\n','\n')

if '.' in input_file:
    file_name_d = input_file.split('.')
    file_name_c = ''
    for ele in file_name_d[:-2]:
        file_name_c += ele + '.'
    file_name_c += file_name_d[-2]
    output_file = file_name_c + '_converted.' + file_name_d[-1]
else:
    output_file = input_file + '_converted'

with open(output_file, 'w', encoding='utf-8') as fo:
    fo.write(content)

with open(output_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    column1 = [row[0] for row in reader]

i = 0
recipes = ''
odlist = list(set(column1))

for od in odlist:
    btest = od[:5]
    if btest == 'block':
        stem = od[5:]
        coingot = 'ingot' + stem
        if coingot in odlist:
            i += 1
            recipes += '    <recipe name="' + stem + ' Block" energyCost="1000" >\n      <input>\n        <itemStack oreDictionary="' + coingot + '" number="9" />\n        <itemStack oreDictionary="foodBlockKayakumeshi" number="1" />\n      </input>\n      <output>\n        <itemStack oreDictionary="' + od + '" number="1" exp="0.5" />\n      </output>\n    </recipe>\n'
        else:
            pass
    else:
        pass

with open(file = 'blockrecipesoutput.xml', mode = 'a', encoding = 'utf-8') as fo:
    fo.write('<!--\n  Added ' + str(i) + ' recipes! Please copy them into "config/enderio/AlloySmelterRecipes_User.xml".\n-->\n' + recipes)
