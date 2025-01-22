import csv
from csv import DictReader
import json

countries = set()
with open ('/Users/luciehoeberichts/Desktop/group_violet/LaTexLovers-1/shoe-size-by-country-2024.csv', 'r') as file:
    dict_reader = DictReader(file)
    list_of_dict = list(dict_reader)
    for item in dict_reader:
        countries.add(item['country'])

world_list = []
with open('world_data.json', 'w') as file:
    json.dump(list_of_dict, file, indent=4)

continents = {
    'Asia': {'India', 'China', 'Indonesia', 'Pakistan', 'Bangladesh', 'Japan', 'Philippines', 'Vietnam', 'Thailand', 'South Korea', 'Afghanistan', 'Malaysia', 'Nepal', 'Sri Lanka', 'Singapore', 'Bhutan', 'Maldives'}, 
    'Europe': {"United Kingdom", "Germany", "France", "Italy", "Spain", "Poland", "Netherlands",
        "Belgium", "Sweden", "Norway", "Denmark", "Finland", "Russia", "Ukraine",
        "Switzerland", "Austria", "Ireland", "Portugal", "Czech Republic", "Hungary"}, 
    "North America": {
        "United States", "Canada", "Mexico", "Cuba", "Jamaica", "Haiti", "Panama", "Guatemala",
        "Honduras", "El Salvador", "Costa Rica", "Belize", "Bahamas"
    },
    "South America": {
        "Brazil", "Argentina", "Colombia", "Peru", "Venezuela", "Chile", "Ecuador",
        "Bolivia", "Paraguay", "Uruguay", "Guyana", "Suriname"
    },
    "Africa": {
        "Nigeria", "South Africa", "Egypt", "Kenya", "Ethiopia", "Ghana", "Tanzania",
        "Algeria", "Sudan", "Morocco", "Angola", "Uganda", "Mozambique", "Zambia",
        "Zimbabwe", "Cameroon", "Senegal"
    },
    "Oceania": {
        "Australia", "New Zealand", "Papua New Guinea", "Fiji", "Samoa", "Tonga", "Vanuatu"
    }
}


#continentos = ['Asia', 'Northern Amercia', 'Europe', 'Africa', 'South America', 'Oceania']



with open ('world_data.json', encoding = 'utf-8') as world_file:
        content_world = json.load(world_file)


for item in content_world:
    in_continent = None
    for continent in continents:
        if item['country'] in continents[continent]:
            in_continent = continent

    world_data_dic = {
        "women_shoes": item['AverageWomenShoeSize'],
        "mens_shoes": item['AverageMenShoeSize'],
        "continent": in_continent if in_continent else "Unknown" 
    }
    world_list.append(world_data_dic)

print(world_list)
with open ('data_world.csv', 'w', encoding= 'utf-8', newline= '') as file:
    writer = csv.DictWriter(file, ['women_shoes', 'mens_shoes', 'continent'])
    writer.writeheader()
    writer.writerows(world_list)
