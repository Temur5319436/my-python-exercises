keywords = {
    'int': 'Butun qiymat',
    'bool': 'Mantiqiy qiymat',
    'float': 'O\'nlik son',
    'string': 'Matnlik qiymat',
    'list': 'Ro\'yxat',
    'tuple': 'O\'zgarmas ro\'yxat',
    'dictionary': 'Lug\'at',
}

for keyword, description in keywords.items():
    print(f'{keyword} - {description}')

countries = {
    'AQSH': 'Washington D.C',
    'Italiya': 'Rim',
    'Malayziya': 'Kuala-Lanpur',
    'O\'zbekiston': 'Tashkent',
    'Rossiya': 'Moskava',
}

print('Dunyo poytaxtlari:')
for capital in countries.values():
    print(capital)

print('Dunyo davlatlari:')
for country in countries.keys():
    print(country)
