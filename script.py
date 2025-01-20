import json

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
data_foot = []

for item in alphabet:
    with open (f'../People/{item}_people.json', encoding = 'utf-8') as people_file:
        content_people = json.load(people_file)
    for person in content_people:
        if 'ontology/shoeSize' in person:
             data_foot.append(person['ontology/shoeSize'])

print(len(data_foot))

# dictionary_people = eval(content_people)
# with open('results.json', 'w', encoding='utf-8') as file:
#     json.dump(dictionary_people, file, indent = 4)



# shoesize = []

# for element in dictionary_people:
#     if item['ontology/shoeSize'] == '(UK) 9 (US) 11 (EU) 41-42':
# #        shoesize.append(item)

# print(shoesize)