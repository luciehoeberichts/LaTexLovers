import json


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


for item in alphabet:
    with open (f'../People/{item}_people.json', encoding = 'utf-8') as people:
        content_people = people.read()

dictionary_people = eval(content_people)
# with open('results.json', 'w', encoding='utf-8') as file:
#     json.dump(dictionary_people, file, indent = 4)


