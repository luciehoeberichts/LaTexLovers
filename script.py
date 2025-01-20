import json


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


for item in alphabet:
    with open (f'../People/{item}_people.json', encoding = 'utf-8') as people:
        content_people = people.read()
        print(content_people)
