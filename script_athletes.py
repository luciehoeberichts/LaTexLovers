import json

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
data_foot_size = []
models = []
types = set()
for item in alphabet:
    with open (f'../People/{item}_people.json', encoding = 'utf-8') as people_file:
        content_people = json.load(people_file)

    
    for person in content_people:
        if 'ontology/shoeSize' in person and 'ontology/birthPlace_label' in person:  
            if 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label'in person:
                for type in person['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label']:
                    types.add(type)

                if 'model' in person['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label']:
                    models.append(person['title'])
            
                
print(len(models))