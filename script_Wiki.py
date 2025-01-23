import json
import csv 
from csv import DictWriter
import re
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent = "Nominatim")
people_list = []

continents = {
    "Africa": {
        "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon",
        "Central African Republic", "Chad", "Comoros", "Congo", "Djibouti", "Egypt", "Equatorial Guinea",
        "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast",
        "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania",
        "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe",
        "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan",
        "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"
    },
    "Asia": {
        "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia",
        "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan",
        "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives",
        "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines",
        "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Tajikistan",
        "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan",
        "Vietnam", "Yemen", "Taiwan", "Russia"
    },
    "Europe": {
        "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia",
        "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
        "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg",
        "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland",
        "Portugal", "Romania", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden",
        "Switzerland", "Ukraine", "United Kingdom", "Vatican City"
    },
    "North America": {
        "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica",
        "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica",
        "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
        "Trinidad and Tobago", "United States"
    },
    "Oceania": {
        "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau",
        "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"
    },
    "South America": {
        "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay",
        "Peru", "Suriname", "Uruguay", "Venezuela"
    }
}

countries = set()
for continent, continent_countries in continents.items():
    countries |= continent_countries


foot_size_detector = re.compile(r'([1-9][0-9]*(\.[0-9])?)')

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
data_foot_size = []

for item in alphabet:
    with open (f'./People/{item}_people.json', encoding = 'utf-8') as people_file:
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
            
            # If we cannot find a country, try geocoding
            if country is None:
                place = person['ontology/birthPlace_label'][0]
                for i in range(3):
                    try:
                        location = geolocator.geocode(place, language='en')
                        if location:
                            country = location.address.split(', ')[-1]
                            time.sleep(.5)
                        break
                    except:
                        if i == 2:
                            print('Failed.')
                        else:
                            print(f'Trying again... ({i + 1})')
                        time.sleep(1.5)

            #Sort by continent
            continent = None
            for current_continent, continent_countries in continents.items():
                if country in continent_countries:
                    continent = current_continent

            # Create final data dictionary
            foot_dictionary = {
                "shoeSize": fr_shoe_size, 
                "place": country,
                "continent": continent
            }
            data_foot_size.append(foot_dictionary)

with open('data_foot_size.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, ['shoeSize', 'place', 'continent'])
    writer.writeheader()
    writer.writerows(data_foot_size)

