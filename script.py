import json
import csv 
from csv import DictWriter
import re

countries = set()
with open ('shoe-size-by-country-2024.csv', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    for item in reader:
        countries.add(item['country'])

foot_size_detector = re.compile(r'([1-9][0-9]*(\.[0-9])?)')

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
data_foot_size = []

for item in alphabet:
    with open (f'./People/{item}_people.json', encoding = 'utf-8') as people_file:
        content_people = json.load(people_file)
    for person in content_people:
        if 'ontology/shoeSize' in person and 'ontology/birthPlace_label' in person: 
            # Find anything that resembles a shoe size
            shoe_sizes = foot_size_detector.findall(str(person['ontology/shoeSize']))

            # If multiple, select the largest shoe size
            largest_size = 0
            for shoe_size, fraction in shoe_sizes:
                shoe_size = float(shoe_size)
                if shoe_size > largest_size:
                    largest_size = shoe_size

            # Convert to US size
            if largest_size > 20:
                largest_size = ((largest_size - 2) / 1.27) - 21.5

            # Find place that is actually a country name
            if type(person['ontology/birthPlace_label']) is not list:
                person['ontology/birthPlace_label'] = [person['ontology/birthPlace_label']]

            country = None
            for place in person['ontology/birthPlace_label']:
                if place in countries:
                    country = place

            # Create final data dictionary
            foot_dictionary = {
                "shoeSize": largest_size, 
                "place": country
            }
            data_foot_size.append(foot_dictionary)

with open('data_foot_size.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, ['shoeSize', 'place'])
    writer.writeheader()
    writer.writerows(data_foot_size)