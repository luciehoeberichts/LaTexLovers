import json
import csv 
from csv import DictWriter
import re


countries = set() 
with open ('WorldReviewdata.csv', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    for item in reader:
        countries.add(item['country'])

    country_dictionary=[]
    continents = {
    'Asia': {'India', 'Uzbekistan', 'Bahrain','China', 'Indonesia', 'Iran', 'Pakistan', 'Bangladesh', 'Japan', 'Israel', 'Philippines', 'Vietnam', 'Thailand', 'South Korea', 'Afghanistan', 'Malaysia', 'Nepal', 'Sri Lanka', 'Singapore', 'Bhutan', 'Maldives', 'Turkey'}, 
    'Europe': {"United Kingdom", 'Malta','Lithuania','Serbia', "Germany", "France", "Italy", "Spain", "Poland", "Netherlands",
        "Belgium", "Sweden", 'Albania', 'Croatia', 'Iceland', 'Latvia', 'Estonia', 'Bosnia and Herzegovina', "Norway", "Denmark", "Finland", "Russia", "Ukraine",
        "Switzerland", "Austria", 'Greece', 'Slovakia', "Ireland", "Portugal", "Czech Republic", "Hungary", 'Estonia'}, 
    "North America": {
        "United States", "Canada", "Mexico", "Cuba", "Jamaica", "Haiti", "Panama", "Guatemala",
        "Honduras", "El Salvador", "Costa Rica", "Belize", "Bahamas", 'Dominican Republic'
    },
    "South America": {
        "Brazil", "Argentina", "Colombia", "Peru", "Venezuela", "Chile", "Ecuador",
        "Bolivia", "Paraguay", "Uruguay", "Guyana", "Suriname"
    },
    "Africa": {
        "Nigeria", "South Africa", 'Tunisia', "Egypt", "Kenya", "Ethiopia", "Ghana", "Tanzania",
        "Algeria", "Sudan", "Morocco", "Angola", "Uganda", "Mozambique", "Zambia",
        "Zimbabwe", "Cameroon", "Senegal", 'Namibia'
    },
    "Oceania": {
        "Australia", "New Zealand", "Papua New Guinea", "Fiji", "Samoa", "Tonga", "Vanuatu"
    }} 
    for country in countries:
            #Sort by continent
        continent = None
        for current_continent, continent_countries in continents.items():
                    if country in continent_countries:
                        continent = current_continent
        dictionary_continents_sorted = {
                        "place": country,
                        "continent": continent, 
                        'shoesize': shoe_size
                            }
        country_dictionary.append(dictionary_continents_sorted)

with open('worldreviewdatasorted.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, ['place', 'continent', 'shoesize'])
    writer.writeheader()
    writer.writerows(country_dictionary)