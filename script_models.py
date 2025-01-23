import json
import csv


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
data_model = []

types = set()
for item in alphabet:
    with open (f'../People/{item}_people.json', encoding = 'utf-8') as people_file:
        content_people = json.load(people_file)

    
    for person in content_people:
        if 'ontology/shoeSize' in person and 'ontology/birthPlace_label' in person:  
            if 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label'in person:
                for type in person['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label']:
                    types.add(type)
                models = []
                if 'model' in person['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label']:
                    models.append(person['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label'][2])
                
                    models_dictionary = {
                    "occupation": models
                }
                    data_model.append(models_dictionary)
            
                
with open('they_all_models.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, ['occupation'])
    writer.writeheader()
    writer.writerows(data_model)
