import json

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
data_foot_size = []

for item in alphabet:
    with open (f'../People/{item}_people.json', encoding = 'utf-8') as people_file:
        content_people = json.load(people_file)
    for person in content_people:
        if 'ontology/shoeSize' in person and 'ontology/birthPlace_label' in person:            
            foot_dictionary = {"shoeSize": person['ontology/shoeSize'], 
                                "place": str(person['ontology/birthPlace_label'])
                                }
            data_foot_size.append(foot_dictionary)
             









with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(data_foot_size, file, indent = 4)


