import time
TIME1 = time.perf_counter()

from itertools import *
import pandas as pd
from transliterate.base import TranslitLanguagePack, registry
from transliterate import translit, get_available_language_codes
from transliterate.discover import autodiscover


#creating dictionaries for transliteration
autodiscover()
class MainPack(TranslitLanguagePack):
    language_code = "main"
    language_name = "main"
    mapping = (
        u"абвгдезийклмнопрстуфхцыАБВГДЕЗИЙКЛМНОПРСТУФХЦЫ",
        u"abvgdezijklmnoprstufhcyABVGDEZIJKLMNOPRSTUFHCY",
    )
    pre_processor_mapping = {
    u"ё": u"jo",
    u"ж": u"zh",
    u"ч": u"ch",
    u"ш": u"sh",
    u"щ": u"shh",
    u"ъ": u"#",
    u"ь": u"\'",
    u"э": u"je",
    u"ю": u"ju",
    u"я": u"ja",
    u"Ё": u"Jo",
    u"Ж": u"Zh",
    u"Ч": u"Ch",
    u"Ш": u"Sh",
    u"Щ": u"Shh",
    u"Ъ": u"##",
    u"Ь": u"\'\'",
    u"Э": u"Je",
    u"Ю": u"Ju",
    u"Я": u"Ja"
    }
registry.register(MainPack)

class Gost779Pack(TranslitLanguagePack):
    language_code = "779"
    language_name = "gost779"
    mapping = (
        u"абвгдезийклмнопрстуфхцыАБВГДЕЗИЙКЛМНОПРСТУФХЦЫ",
        u"abvgdezijklmnoprstufhcyABVGDEZIJKLMNOPRSTUFHCY",
    )
    pre_processor_mapping = {
    u"ё": u"yo",
    u"ж": u"zh",
    u"ч": u"ch",
    u"ш": u"sh",
    u"щ": u"shh",
    u"ъ": u"\"",
    u"ь": u"\'",
    u"э": u"e\'",
    u"ю": u"yu",
    u"я": u"ya",
    u"Ё": u"Yo",
    u"Ж": u"Zh",
    u"Ч": u"Ch",
    u"Ш": u"Sh",
    u"Щ": u"Shh",
    u"Ъ": u"\"\"",
    u"Ь": u"\'\'",
    u"Э": u"E\'",
    u"Ю": u"Yu",
    u"Я": u"Ya"
    }
registry.register(Gost779Pack)

class Gost16876Pack(TranslitLanguagePack):
    language_code = "16876"
    language_name = "gost16876"
    mapping = (
        u"абвгдезиклмнопрстуфцыАБВГДЕЗИКЛМНОПРСТУФЦЫ",
        u"abvgdeziklmnoprstufcyABVGDEZIKLMNOPRSTUFCY",
    )
    pre_processor_mapping = {
    u"ё": u"jo",
    u"ж": u"zh",
    u"й": u"jj",
    u"х": u"kh",
    u"ч": u"ch",
    u"ш": u"sh",
    u"щ": u"shh",
    u"ъ": u"\"",
    u"ь": u"\'",
    u"э": u"eh",
    u"ю": u"ju",
    u"я": u"ja",
    u"Ё": u"Jo",
    u"Ж": u"Zh",
    u"Й": u"Jj",
    u"Х": u"Kh",
    u"Ч": u"Ch",
    u"Ш": u"Sh",
    u"Щ": u"Shh",
    u"Ъ": u"\"\"",
    u"Ь": u"\'\'",
    u"Э": u"Eh",
    u"Ю": u"Ju",
    u"Я": u"Ja"
    }
registry.register(Gost16876Pack)

class Sev1362Pack(TranslitLanguagePack):
    language_code = "1362"
    language_name = "sev1362"
    mapping = (
        u"абвгдезийклмнопрстуфцыАБВГДЕЗИЙКЛМНОПРСТУФЦЫ",
        u"abvgdezijklmnoprstufcyABVGDEZIJKLMNOPRSTUFCY",
    )
    pre_processor_mapping = {
    u"ё": u"jo",
    u"ж": u"zh",
    u"х": u"kh",
    u"ч": u"ch",
    u"ш": u"sh",
    u"щ": u"shh",
    u"ъ": u"\"",
    u"ь": u"\'",
    u"э": u"eh",
    u"ю": u"ju",
    u"я": u"ja",
    u"Ё": u"Jo",
    u"Ж": u"Zh",
    u"Х": u"Kh",
    u"Ч": u"Ch",
    u"Ш": u"Sh",
    u"Щ": u"Shh",
    u"Ъ": u"\"\"",
    u"Ь": u"\'\'",
    u"Э": u"Eh",
    u"Ю": u"Ju",
    u"Я": u"Ja"
    }
registry.register(Sev1362Pack)

class MvdPack(TranslitLanguagePack):
    language_code = "mvd"
    language_name = "mvd"
    mapping = (
        u"абвгдеёзийклмнопрстуфыэАБВГДЕЁЗИЙКЛМНОПРСТУФЫЭ",
        u"abvgdeeziiklmnoprstufyeABVGDEEZIIKLMNOPRSTUFYE",
    )
    pre_processor_mapping = {
    u"ж": u"zh",
    u"х": u"kh",
    u"ц": u"ts",
    u"ч": u"ch",
    u"ш": u"sh",
    u"щ": u"shch",
    u"ъ": u"ie",
    u"ь": u"",
    u"э": u"eh",
    u"ю": u"iu",
    u"я": u"ia",
    u"Ж": u"Zh",
    u"Х": u"Kh",
    u"Ц": u"Ts",
    u"Ч": u"Ch",
    u"Ш": u"Sh",
    u"Щ": u"Shch",
    u"Ъ": u"Ie",
    u"Ь": u"",
    u"Э": u"Eh",
    u"Ю": u"Iu",
    u"Я": u"Ia"
    }
registry.register(MvdPack)

class LCPack(TranslitLanguagePack):
    language_code = "lc"
    language_name = "lc"
    mapping = (
        u"абвгдеёзийклмнопрстуфыэАБВГДЕЁЗИЙКЛМНОПРСТУФЫЭ",
        u"abvgdeeziiklmnoprstufyeABVGDEEZIIKLMNOPRSTUFYE",
    )
    pre_processor_mapping = {
    u"ж": u"zh",
    u"х": u"kh",
    u"ц": u"ts",
    u"ч": u"ch",
    u"ш": u"sh",
    u"щ": u"shch",
    u"ъ": u"\"",
    u"ь": u"\'",
    u"э": u"eh",
    u"ю": u"iu",
    u"я": u"ia",
    u"Ж": u"Zh",
    u"Х": u"Kh",
    u"Ц": u"Ts",
    u"Ч": u"Ch",
    u"Ш": u"Sh",
    u"Щ": u"Shch",
    u"Ъ": u"\"\"",
    u"Ь": u"\'\'",
    u"Э": u"Eh",
    u"Ю": u"Iu",
    u"Я": u"Ia"
    }
registry.register(LCPack)

class BGNPack(TranslitLanguagePack):
    language_code = "bgn"
    language_name = "bgn"
    mapping = (
        u"абвгдеёзийклмнопрстуфыэАБВГДЕЁЗИЙКЛМНОПРСТУФЫЭ",
        u"abvgdeeziyklmnoprstufyeABVGDEEZIYKLMNOPRSTUFYE",
    )
    pre_processor_mapping = {
    u"ж": u"zh",
    u"х": u"kh",
    u"ц": u"ts",
    u"ч": u"ch",
    u"ш": u"sh",
    u"щ": u"shch",
    u"ъ": u"\"",
    u"ь": u"\'",
    u"э": u"eh",
    u"ю": u"yu",
    u"я": u"ya",
    u"Ж": u"Zh",
    u"Х": u"Kh",
    u"Ц": u"Ts",
    u"Ч": u"Ch",
    u"Ш": u"Sh",
    u"Щ": u"Shch",
    u"Ъ": u"\"\"",
    u"Ь": u"\'\'",
    u"Э": u"Eh",
    u"Ю": u"Yu",
    u"Я": u"Ya"
    }
registry.register(BGNPack)

class BSIPack(TranslitLanguagePack):
    language_code = "bsi"
    language_name = "bsi"
    mapping = (
        u"абвгдеёзийклмнопрстуфыэАБВГДЕЁЗИЙКЛМНОПРСТУФЫЭ",
        u"abvgdeeziiklmnoprstufyeABVGDEEZIIKLMNOPRSTUFYE",
    )
    pre_processor_mapping = {
    u"ж": u"zh",
    u"х": u"kh",
    u"ц": u"ts",
    u"ч": u"ch",
    u"ш": u"sh",
    u"щ": u"shch",
    u"ъ": u"\"",
    u"ь": u"\'",
    u"э": u"eh",
    u"ю": u"yu",
    u"я": u"ya",
    u"Ж": u"Zh",
    u"Х": u"Kh",
    u"Ц": u"Ts",
    u"Ч": u"Ch",
    u"Ш": u"Sh",
    u"Щ": u"Shch",
    u"Ъ": u"\"\"",
    u"Ь": u"\'\'",
    u"Э": u"Eh",
    u"Ю": u"Yu",
    u"Я": u"Ya"
    }
registry.register(BSIPack)

class ZagranPack(TranslitLanguagePack):
    language_code = "zagr"
    language_name = "zagran"
    mapping = (
        u"абвгдеёзийклмнопрстуфыэАБВГДЕЁЗИЙКЛМНОПРСТУФЫЭ",
        u"abvgdeeziiklmnoprstufyeABVGDEEZIIKLMNOPRSTUFYE",
    )
    pre_processor_mapping = {
    u"ж": u"zh",
    u"х": u"kh",
    u"ц": u"tc",
    u"ч": u"ch",
    u"ш": u"sh",
    u"щ": u"shch",
    u"ъ": u"",
    u"ь": u"",
    u"э": u"eh",
    u"ю": u"iu",
    u"я": u"ia",
    u"Ж": u"Zh",
    u"Х": u"Kh",
    u"Ц": u"Tc",
    u"Ч": u"Ch",
    u"Ш": u"Sh",
    u"Щ": u"Shch",
    u"Ъ": u"",
    u"Ь": u"",
    u"Э": u"Eh",
    u"Ю": u"Iu",
    u"Я": u"Ia"
    }
registry.register(ZagranPack)

#dont forget to change directory
df = pd.read_csv('C:\\Users\\Lenovo\\Desktop\\fl\\3\\db_names.csv')

#with open('C:\\Users\\Lenovo\\Desktop\\fl\\3\\dictionary.txt') as file:
dictionary = {'А':['A'], 'а':['a'],
'Б':['B'], 'б':['b'],
'В':['V', 'W'], 'в':['v', 'w'],
'Г':['G'], 'г':['g'],
'Д':['D'], 'д':['d'],
'Е':['E', 'Ye'], 'е':['e', 'ye'],
'Ё':['E', 'Io', 'Jo', 'Yo'], 'ё':['e', 'io', 'jo', 'yo'],
'Ж':['J', 'G', 'Zh'], 'ж':['j', 'g', 'zh'],
'З':['Z'], 'з':['z'],
'И':['I'], 'и':['i'],
'Й':['J', 'I', "`", "'"], 'й':['j', 'i', "`", "'"],
'К':['Ck', 'K', 'C'], 'к':['ck', 'k', 'c'],
'Л':['L'], 'л':['l'],
'М':['M'], 'м':['m'],
'Н':['N'], 'н':['n'],
'О':['O'], 'о':['o'],
'П':['P'], 'п':['p'],
'Р':['R'], 'р':['r'],
'С':['S', 'C'], 'с':['s', 'c'],
'Т':['T'], 'т':['t'],
'У':['U', 'Y', 'Oo'], 'у':['u', 'y', 'oo'],
'Ф':['F', 'Ph'], 'ф':['f', 'ph'],
'Х':['Kh', 'H'], 'х':['kh', 'h'],
'Ц':['Ts', 'C'], 'ц':['ts', 'c'],
'Ч':['Ch'], 'ч':['ch'],
'Ш':['Sh'], 'ш':['sh'],
'Щ':['Shch'], 'щ':['shch'],
'Ъ':['', '`', "'", 'Ie'], 'ъ':['', '`', "'", 'ie'],
'Ы':['I', 'Y'], 'ы':['i', 'y'],
'Ь':['', '`', "'"], 'ь':['', '`', "'"],
'Э':['E'], 'э':['e'],
'Ю':['Ju', 'Y', 'U', 'Iu', 'Jy', 'Yu'], 'ю':['ju', 'y', 'u', 'iu', 'jy', 'yu'],
'Я':['Ia', 'Ja', 'Ya'], 'я':['ia', 'ja', 'ya']}

dictionary1 = {'ИЙ':'y', 'ий':'y', 'иЙ':'y', 'Ий':'y', 'КС':'x', 'кс':'x', 'Кс':'x', 'кС':'x'}

#opening file
#dont forget to change directory
with open('C:\\Users\\Lenovo\\Desktop\\fl\\3\\db_lat_names.csv', 'w'):
    pass
res_names = pd.DataFrame({'kir_name':[], 'lat_name':[]})
res_names.to_csv('C:\\Users\\Lenovo\\Desktop\\fl\\3\\db_lat_names.csv', mode = 'a', index = False)

#changing symbols(transliteration)
#dont forget to change directory
kir_names = df.name.unique()
for kir_name in kir_names:
    lat_name = []
    for symbol in kir_name:
        if symbol not in dictionary.keys():
            lat_name.append([symbol])
        else:
            lat_name.append(dictionary[symbol])
    lat_name1 = []
    kir_name1 = kir_name
    for key in dictionary1.keys():
        if key in kir_name1:
            kir_name1 = kir_name1.replace(key, dictionary1[key])
            for symbol in kir_name1:
                if symbol not in dictionary.keys():
                    lat_name1.append([symbol])
                else:
                    lat_name1.append(dictionary[symbol])
        else:
            continue
    lat_name2 = translit(kir_name, 'main')
    lat_name3 = translit(kir_name, '779')
    lat_name4 = translit(kir_name, '16876')
    lat_name5 = translit(kir_name, '1362')
    lat_name6 = translit(kir_name, 'mvd')
    lat_name7 = translit(kir_name, 'lc')
    lat_name8 = translit(kir_name, 'bgn')
    lat_name9 = translit(kir_name, 'bsi')
    lat_name10 = translit(kir_name, 'zagr')
    lat_name11 = translit(kir_name, 'ru', reversed=True)

    if kir_name == kir_name1 :
        for optional_name in product(*lat_name):
            final_lat_name = ''
            for i in optional_name:
                final_lat_name += i
            res_names = pd.DataFrame({
                'kir_name':[kir_name,
                    kir_name,
                    kir_name,
                    kir_name,
                    kir_name,
                    kir_name,
                    kir_name,
                    kir_name,
                    kir_name,
                    kir_name,
                    kir_name], 
                    'lat_name':[final_lat_name,
                        lat_name2,
                        lat_name3,
                        lat_name4,
                        lat_name5,
                        lat_name6,
                        lat_name7,
                        lat_name8,
                        lat_name9,
                        lat_name10,
                        lat_name11]})
            res_names.to_csv('C:\\Users\\Lenovo\\Desktop\\fl\\3\\db_lat_names.csv', mode = 'a', index = False, header = False)
    elif len(lat_name1) > 0:
        for optional_name in product(*lat_name):
            final_lat_name = ''
            for i in optional_name:
                final_lat_name += i
            for optional_name1 in product(*lat_name1):
                final_lat_name1 = ''
                for j in optional_name1:
                    final_lat_name1 += j
                res_names = pd.DataFrame({
                    'kir_name':[kir_name, 
                        kir_name,
                        kir_name,
                        kir_name,
                        kir_name,
                        kir_name,
                        kir_name,
                        kir_name,
                        kir_name,
                        kir_name,
                        kir_name,
                        kir_name], 
                        'lat_name':[final_lat_name, 
                            final_lat_name1,
                            lat_name2,
                            lat_name3,
                            lat_name4,
                            lat_name5,
                            lat_name6,
                            lat_name7,
                            lat_name8,
                            lat_name9,
                            lat_name10,
                            lat_name11]})
                res_names.to_csv('C:\\Users\\Lenovo\\Desktop\\fl\\3\\db_lat_names.csv', mode = 'a', index = False, header = False)

#deleting dublicates
#dont forget to change directory
df = pd.read_csv('C:\\Users\\Lenovo\\Desktop\\fl\\3\\db_lat_names.csv')
df = df.drop_duplicates()
df.to_csv('C:\\Users\\Lenovo\\Desktop\\fl\\3\\db_lat_names.csv')

TIME2 = time.perf_counter()
print('\n\n', round((TIME2 - TIME1), 3), ' seconds', sep = '')