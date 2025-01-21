import json
import csv 
from csv import DictWriter
import re

foot_size_detector = re.compile(r'([1-9][0-9]*(\.[0-9])?)')

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
data_foot_size = []

for item in alphabet:
    with open (f'../People/{item}_people.json', encoding = 'utf-8') as people_file:
        content_people = json.load(people_file)
    for person in content_people:
        if 'ontology/shoeSize' in person and 'ontology/birthPlace_label' in person:
            shoe_size_string = str(person['ontology/shoeSize']).lower()
            shoe_sizes = foot_size_detector.findall(str(shoe_size_string))

            largest_shoe_size = 0
            smallest_shoe_size = 9000
            for shoe_size, fraction in shoe_sizes:
                shoe_size = float(shoe_size)
                if shoe_size > largest_shoe_size:
                    largest_shoe_size = shoe_size
                if shoe_size < smallest_shoe_size:
                    smallest_shoe_size = shoe_size

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

            foot_dictionary = {
                "shoeSize": fr_shoe_size, 
                "place": person['ontology/birthPlace_label'][0] if type(person['ontology/birthPlace_label']) is list 
                            else person['ontology/birthPlace_label']
            }
            data_foot_size.append(foot_dictionary)
             




with open('data_foot_size.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, ['shoeSize', 'place'])
    writer.writeheader()
    writer.writerows(data_foot_size)