import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

with open('world_food_production_2018.csv', 'r') as csv_file:
    food_data = csv.DictReader(csv_file)
    headers = food_data.fieldnames

    food_data =list(food_data)
    print()
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'


    print(color.BOLD + color.UNDERLINE + 'BIGGEST PRODUCER OF EACH FOOD TYPE BY COUNTRY (2018):'+ color.END)
    for food in headers[2:]:
        country_data = max(food_data, key=lambda country: int(country[food]))
        tonnes = int(country_data[food])
        food_formatted = food.replace('_', ' ')
        print('{} produced the most {}: {} tonnes.'.format(country_data['Country'], food_formatted, tonnes) +'\n')

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

    print(color.BOLD + color.UNDERLINE + 'BIGGEST PRODUCER OF EACH FOOD TYPE BY REGION (2018):' + color.END)
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
        print('{} produced the most {}: {} tonnes.'.format(area, food_formatted, tonnes) + '\n')

    desired_country = input(color.BOLD +'WHICH REGION WOULD YOU LIKE TO KNOW MORE ABOUT? Asia, Africa, Europe, North America, South America, Middle east, Oceania or South Atlantic'+ color.END).lower().strip()
    print('Here is the weight in tonnes per food group produced by that region in 2018:')
    print(areas[desired_country])
    print('\n')


    citrus_country = np.array(())
    for country in food_data:
        citrus_country = np.append(citrus_country, int(country['Citrus_fruit']))

    country_name = np.array (())
    for country in food_data:
        country_name = np.append(country_name, (country['Country']))

    plt.figure()
    plt.scatter(country_name, citrus_country)
    plt.ylabel('Tonnes')
    plt.xlabel('Country')
    plt.title('Tonnes of citrus produced by country')
    plt.show()

    ###############################################################################################################################

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