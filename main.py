import json
import re

file = open('pokemon_full.json', 'r')
pokemon_full = file.read()
file.close()

print('1) Total word count:', len(pokemon_full))

pokemon_full_no_punctuation = re.sub('[^\w]', '', pokemon_full)
print('2) Total word count with no punctuation:', len(pokemon_full_no_punctuation))

pokemon_full_json = json.loads(pokemon_full)
max_description = (0, '')
for item in pokemon_full_json:
    max_cur_description = [max_description, (len(item['description']), item['name'])]
    max_description = max(max_cur_description, key=lambda x: x[0])
print('3) Pokemon with longest description:', max_description[1])

max_number = 0
for item in pokemon_full_json:
    for skill in item['abilities']:
        max_number = max(max_number, len(skill.split()))
print('4) Skills with largest number of words:', end=' ')
for item in pokemon_full_json:
    for skill in item['abilities']:
        if max_number == len(skill.split()):
            print(skill)
