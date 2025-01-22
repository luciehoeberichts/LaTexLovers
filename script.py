import json
import csv 
from csv import DictWriter
import re

countries = set()
with open ('shoe-size-by-country-2024.csv', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    for item in reader:
        countries.add(item['country'])

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
    }
}


foot_size_detector = re.compile(r'([1-9][0-9]*(\.[0-9])?)')

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
data_foot_size = []
mean_country= {}
count_country= {}
for item in alphabet:
    with open (f'People/{item}_people.json', encoding = 'utf-8') as people_file:
        content_people = json.load(people_file)
    for person in content_people:
        if 'ontology/shoeSize' in person and 'ontology/birthPlace_label' in person:
            # Find everything that looks like it might be a shoe size
            shoe_size_string = str(person['ontology/shoeSize']).lower()
            shoe_sizes = foot_size_detector.findall(str(shoe_size_string))

            # Find largest and smallest (maybe) shoe sizes
            largest_shoe_size = 0
            smallest_shoe_size = 9000
            for shoe_size, fraction in shoe_sizes:
                shoe_size = float(shoe_size)
                if shoe_size > largest_shoe_size:
                    largest_shoe_size = shoe_size
                if shoe_size < smallest_shoe_size:
                    smallest_shoe_size = shoe_size

            # Decision tree to decide the US shoe size fr
            if largest_shoe_size > 20:
                fr_shoe_size = ((largest_shoe_size - 2) / 1.27) - 21.5
            else:
                if 's' in shoe_size_string:
                    if 'k' in shoe_size_string:
                        fr_shoe_size = smallest_shoe_size + 1.5
                    else:
                        fr_shoe_size = largest_shoe_size
                else:
                    if 'k' in shoe_size_string:
                        fr_shoe_size = smallest_shoe_size + 1.5
                    else:
                        fr_shoe_size = largest_shoe_size  # educated guess

            # Find place that is actually a country name
            if type(person['ontology/birthPlace_label']) is not list:
                person['ontology/birthPlace_label'] = [person['ontology/birthPlace_label']]

            country = None
            for place in person['ontology/birthPlace_label']:
                if place in countries:
                    country = place

            #Sort by continent
                continent = None
                for current_continent, continent_countries in continents.items():
                    if country in continent_countries:
                        continent = current_continent

            # Create final data dictionary
            foot_dictionary = {
                "shoeSize": fr_shoe_size, 
                "place": country,
                "continent": continent, 
            }
            data_foot_size.append(foot_dictionary)

with open('data_foot_size.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, ['shoeSize', 'place', 'continent'])
    writer.writeheader()
    writer.writerows(data_foot_size)