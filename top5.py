'''
========================================================================================
Top 5 News API
========================================================================================
'''
import requests
import json

country_source = """
Please choose the source of the news:
[US] for USA
[ID] for Indonesia
[JP] for Japan
"""
country_input = input ("Source [US/ID/JP]: ")
if country_input.lower() == 'us':
    print('You will be re-directed to US news portal')
    country = 'us'
elif country_input.lower() == 'id':
    print('You will be re-directed to Indonesia news portal')
    country = 'id'
elif country_input.lower() == 'jp':
    print('You will be re-directed to Japan news portal')
    country = 'jp'
else:
    print('Input invalid')

url_tech = 'https://newsapi.org/v2/top-headlines?country='+country+'&category=technology&apiKey=de686c1612b244b3abac73d56cdcebc8'

url_health = 'https://newsapi.org/v2/top-headlines?country='+country+'&category=health&apiKey=de686c1612b244b3abac73d56cdcebc8'

url_business = 'https://newsapi.org/v2/top-headlines?country='+country+'&category=business&apiKey=de686c1612b244b3abac73d56cdcebc8'

url_sport = 'https://newsapi.org/v2/top-headlines?country='+country+'&category=sports&apiKey=de686c1612b244b3abac73d56cdcebc8'

url_science = 'https://newsapi.org/v2/top-headlines?country='+country+'&category=science&apiKey=de686c1612b244b3abac73d56cdcebc8'


a = """
Welcome to the news portal of Ya salam!!!
Which news are you interested in?
[1] Technology
[2] Health
[3] Business
[4] Sport
[5] Science
"""
print(a)
user_input = input('Enter option [1/2/3/4/5]: ')
if user_input == '1':
    tech = requests.get(url_tech)
    print('Top 5 news of Technology: ')
    for new in range(0, 5):
        print(new+1,  '-', tech.json()['articles'][new]["title"])
elif user_input == '2':
    health = requests.get(url_health)
    print('Top 5 news of Health: ')
    for new in range(0, 5):
        print(new+1,  '-', health.json()['articles'][new]["title"])
elif user_input == '3':
    business = requests.get(url_business)
    print('Top 5 news of Business: ')
    for new in range(0,5):
        print(new+1,  '-', business.json()['articles'][new]["title"])
elif user_input == '4':
    sport = requests.get(url_sport)
    print('Top 5 news of Sport: ')
    for new in range(0,5):
        print(new+1,  '-', sport.json()['articles'][new]["title"])
elif user_input == '5':
    science = requests.get(url_science)
    print('Top 5 news of Science: ')
    for new in range(0,5):
        print(new+1,  '-', science.json()['articles'][new]["title"])
else:
    print('Input invalid')


