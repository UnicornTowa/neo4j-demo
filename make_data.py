import pandas as pd
import numpy as np
import random

male_names = []
with open('names100m.txt', 'r') as f:
    for line in f:
        male_names.append(str(line).rstrip())

female_names = []
with open('names100f.txt', 'r') as f:
    for line in f:
        female_names.append(str(line).rstrip())
surnames = []
with open('surnames500.txt', 'r') as f:
    for line in f:
        surnames.append(str(line).rstrip().lower().title())

persons = pd.DataFrame(columns=['PersonID', 'PersonName', 'PersonResidence', 'PersonSex', 'PersonAge'])

cities = ['New York', 'Los Angeles', 'Chicago']


def random_age():
    return 18 + int(np.random.chisquare(20))


for i in range(1500):
    persons.loc[len(persons.index)] = [i,
                                       random.choice(female_names) + ' ' + random.choice(surnames),
                                       random.choice(cities),
                                       'female',
                                       random_age()]
for i in range(1500):
    persons.loc[len(persons.index)] = [i + 1500,
                                       random.choice(male_names) + ' ' + random.choice(surnames),
                                       random.choice(cities),
                                       'male',
                                       random_age()]

persons.to_csv('persons.csv', index=False)