import csv

with open('world_food_production_2018.csv', 'r') as csv_file:
    food_data = csv.DictReader(csv_file)

    headers = food_data.fieldnames
    print(headers)

    for country in food_data:
        country_name = country['Country']
        region = country['Area']
        citrus = country['Citrus_fruit']
        print('In 2018 {} in {} produced {} tonnes of citrus.'.format(country_name, region, citrus))