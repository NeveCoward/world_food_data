import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np
import pycountry
import pandas as pd
import plotly.express as px
import plotly.offline as offline
import time

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

    ##biggest producer of each food type
    print(color.BOLD + color.UNDERLINE + 'BIGGEST PRODUCER OF EACH FOOD TYPE BY COUNTRY (2018):'+ color.END)
    for food in headers[2:]:
        country_data = max(food_data, key=lambda country: int(country[food]))
        tonnes = int(country_data[food])
        food_formatted = food.replace('_', ' ')
        print('{} produced the most {}: {} tonnes.'.format(country_data['Country'], food_formatted, tonnes) +'\n')

    time.sleep(2)

    ##top ten producers overall
    print(color.BOLD + color.UNDERLINE + 'TOP TEN FOOD PRODUCERS WORLDWIDE (2018):' + color.END)
    country_names = []
    total_prod = []

    for country in food_data:
        food_totals = (int(country['Citrus_fruit']) + int(country['Eggs']) + int(country['Treenuts']) + int(
            country['Pulses']) + int(country['Coarse_grain']) + int(country['Meat']) + int(
            country['Roots_and_tubers']) + int(country['Vegetables']) + int(country['Milk']) + int(
            country['Fruit']) + int(country['Cereals']))
        country_names.append(country['Country'])
        total_prod.append(food_totals)

    country_totals = dict(zip(country_names, total_prod))
    country_ranked = dict(reversed(sorted(country_totals.items(), key=itemgetter(1))))

    count = 0

    for x in list(country_ranked)[:10]:
        count = count + 1
        print('The No.{} food producer in 2018 was {}, and they produced {} tonnes of food.'.format(count, x, country_ranked[x]))
        print('\n')

    time.sleep(2)

    ##top ten producers of citrus + graph
    citrus_country = np.array(())
    country_nombre = np.array(())
    for country in food_data:
        citrus_country = np.append(citrus_country, int(country['Citrus_fruit']))
        country_nombre = np.append(country_nombre, country['Country'])

    indexes = np.argsort(citrus_country)[::-1][:10]
    citrus_top10 = citrus_country[indexes]
    country_top10 = country_nombre[indexes]

    graph= input(color.BOLD + 'Here is top 10 producers of citrus, represented visually. To activate graph, type: activate'+ color.END + '\n').strip()
    if graph == "activate":
        plt.figure()
        plt.scatter(country_top10, citrus_top10)
        plt.ylabel('Tonnes')
        plt.xlabel('Country')
        plt.xticks(rotation=90)
        plt.title('Top 10 producers of citrus in tonnes')
        plt.show()

    time.sleep(2)

    ##biggest producer by region
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

    time.sleep(2)

    ##search function
    desired_country = input(color.BOLD +'WHICH REGION WOULD YOU LIKE TO KNOW MORE ABOUT? Asia, Africa, Europe, North America, South America, Middle east, Oceania or South Atlantic'+ color.END).lower().strip()
    print('Here is the weight in tonnes per food group produced by that region in 2018:')
    print(areas[desired_country])
    print('\n')

    time.sleep(8)

    print('You will now be taken to a map to show total food production per country in 2018! Hover over the countries to find out more...')

    time.sleep(2)

    ###############################################################################################################################

##choropleth map
pycntrylist = list(pycountry.countries)
pycntrynames = []
for x in pycntrylist:
    pycntrynames.append(x.name)

invalid_names = (list(set(country_names).difference(pycntrynames)))
#print(sorted(invalid_names))

country_names = [country.replace('Mainland China', 'China') for country in country_names]
country_names = [country.replace('USA', 'United States') for country in country_names]
country_names = [country.replace('Russia', 'Russian Federation') for country in country_names]
country_names = [country.replace('Vietnam', 'Viet Nam') for country in country_names]
country_names = [country.replace('Iran', 'Iran, Islamic Republic of') for country in country_names]
country_names = [country.replace('Bolivia', 'Bolivia, Plurinational State of') for country in country_names]
country_names = [country.replace('Venezuela', 'Venezuela, Bolivarian Republic of') for country in country_names]
country_names = [country.replace('Tanzania', 'Tanzania, United Republic of') for country in country_names]
country_names = [country.replace('Laos', "Lao People's Democratic Republic") for country in country_names]
country_names = [country.replace('North Korea', "Korea, Democratic People's Republic of") for country in country_names]
country_names = [country.replace('South Korea', 'Korea, Republic of') for country in country_names]
country_names = [country.replace("Cote d'Ivoire", "Côte d'Ivoire") for country in country_names]
country_names = [country.replace('Congo', 'Congo, The Democratic Republic of the') for country in country_names]
country_names = [country.replace('Syria', 'Syrian Arab Republic') for country in country_names]
country_names = [country.replace('Taiwan', 'Taiwan, Province of China') for country in country_names]
country_names = [country.replace('Czech Republic', 'Czechia') for country in country_names]

##assign country codes to country names
countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_3

country_codes = [countries.get(country, 'Unkwnown code') for country in country_names]

##make pandas dataframe
data = {'Code': country_codes,
        'Name': country_names,
        'Production': total_prod}

df = pd.DataFrame(data)

##use plotly to make map
fig = px.choropleth(df, locations='Code',
                     locationmode='ISO-3',
                     color='Production',
                     hover_name='Name',
                     color_continuous_scale=px.colors.sequential.Plasma)

offline.init_notebook_mode()
offline.plot(fig, auto_open=True, image='png', image_filename='test', output_type='file', image_width=800, image_height=600, filename='temp-plot.html', validate=False)
