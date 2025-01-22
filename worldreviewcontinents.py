import json
import csv 
from csv import DictWriter
import re

countries = set()
with open ('WorldReviewdata.csv', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    for item in reader:
        countries.add(item['country'])

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
continent = None
for current_continent, continent_countries in continents.items():
    if country in continent_countries:
        continent = current_continent

# Create final data dictionary
    foot_dictionary = {
        "shoeSize":  total, 
        "place": country,
        "continent": continent
         }
            data_foot_size.append(foot_dictionary)

with open('data_foot_size.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, ['shoeSize', 'place', 'continent'])
    writer.writeheader()
    writer.writerows(data_foot_size)
