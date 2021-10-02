import json

# 2 important functions for JSON:
# loads -> convert something (file, string) to a json object
# dump -> convert json obect to something (file, string)

if __name__ == '__main__':
    with open('files/person.json') as file:
        person_str = file.read()

    person_json = json.loads(person_str)
    numbers = person_json['phoneNumbers']
    for number in numbers:
        if number['type'] == 'home':
            number['number'] = "514 123-4567"

    with open('files/person_edited.json', 'w') as file:
        json.dump(person_json, file)

