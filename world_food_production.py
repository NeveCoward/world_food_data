import csv
from operator import itemgetter

with open('world_food_production_2018.csv', 'r') as csv_file:
    food_data = csv.DictReader(csv_file)

    headers = food_data.fieldnames
    print(headers)

    food_data =list(food_data)

    for food in headers[2:]:
        country_data = max(food_data, key=lambda country: int(country[food]))
        tonnes = int(country_data[food])
        food_formatted = food.replace('_', ' ')
        print('In 2018, the country which produced the most {} was {}, and they produced {} tonnes.'.format(food_formatted, country_data['Country'], tonnes))

        areas = {
        'asia': {},
        'europe': {},
        'africa': {},
        'middle east': {},
        'north america': {},
        'south america': {},
        'south atlantic': {},
        'oceania': {}
    }

    for country in food_data:
        area = country['Area'].lower()
        for food in headers[2:]:
            if food not in areas[area]:
                areas[area][food] = int(country[food])
            else:
                areas[area][food] += int(country[food])

    for food in headers[2:]:
        area = max(areas.keys(), key=lambda area: areas[area][food])
        tonnes = int(areas[area][food])
        food_formatted = food.replace('_', ' ')
        print('In 2018, the area which produced the most {} was {}, and they produced {} tonnes.'.format(food_formatted, area, tonnes))

    desired_country = input('What area do you want to know about: Asia, Africa, Europe, North America, South America, Middle east, Oceania or South Atlantic').lower().strip()
    print(areas[desired_country])

    ################################################################################################neve above, fenella below

    country_names = []
    total_prod = []

    for country in food_data:
        food_totals = (int(country['Citrus_fruit']) + int(country['Eggs']) + int(country['Treenuts']) + int(
            country['Pulses']) + int(country['Coarse_grain']) + int(country['Meat']) + int(
            country['Roots_and_tubers']) + int(country['Vegetables']) + int(country['Milk']) + int(
            country['Fruit']) + int(country['Cereals']))
        country_names.append(country['Country'])
        total_prod.append(food_totals)

    country_totals = dict(zip(country_names,total_prod))
    country_ranked = dict(reversed(sorted(country_totals.items(), key=itemgetter(1))))

    count = 0

    for x in list(country_ranked)[:10]:
        count = count + 1
        print('The no.{} food producer in 2018 was {}, and they produced {} tonnes of food' .format(count, x, country_ranked[x]))