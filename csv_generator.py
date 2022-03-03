import pandas as pd
import numpy as np
from faker import Faker
import datetime
import csv
import requests
import random

Faker.seed(42)
fake = Faker(locale='en_US')

df = pd.read_csv('grouped_workouts.csv')
gby = df.groupby(['Fitness Discipline', 'Type', 'Length (minutes)', 'Title'])

def PosNormal(mean, sigma, round_to=2):
    x = np.random.normal(mean,sigma)
    return(round(x, round_to) if x>=0 else PosNormal(mean,sigma))

with open('workouts.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'Workout Timestamp',
        'Live/On-Demand',
        'Instructor Name',
        'Length (minutes)',
        'Fitness Discipline',
        'Type',
        'Title',
        'Class Timestamp',
        'Total Output',
        'Avg. Watts',
        'Avg. Resistance',
        'Avg. Cadence (RPM)',
        'Avg. Speed (mph)',
        'Distance (mi)',
        'Calories Burned',
        'Avg. Heartrate',
        'Avg. Incline',
        'Avg. Pace (min/mi)'
        ]
    )
    for _ in range(random.randint(100,1000)):
        row = df.sample()
        random_sample = random.sample(gby.indices.keys(), 1)
        workout_timestamp = fake.date_time_between_dates(datetime_start=datetime.datetime(2021, 1, 1), datetime_end='now')
        workout_live_on_demand = 'Live' if fake.boolean() else 'On Demand'
        instructor_name = row['Instructor Name'].values[0]
        length = row['Length (minutes)'].values[0]
        fitness_discipline = row['Fitness Discipline'].values[0]
        type = row['Type'].values[0]
        title = row['Title'].values[0]
        class_timestamp = fake.date_time_between_dates(datetime_start=datetime.datetime(2021, 1, 1), datetime_end='now')
        total_output = PosNormal(134.5, 94.5) if fitness_discipline not in ['Meditation', 'Running'] else None
        avg_watts = None if fitness_discipline != 'Cycling' else PosNormal(99.61, 26.85)
        avg_resistance = None if fitness_discipline != 'Cycling' else round(random.random() * 100, 2)
        avg_cadence = None if fitness_discipline != 'Cycling' else PosNormal(75.19, 9.34, 0)
        avg_speed = None if fitness_discipline != 'Cycling' else PosNormal(15.59, 2.10)
        distance = None if fitness_discipline != 'Cycling' else PosNormal(5.58, 3.64)
        calories = PosNormal(183.73, 158.84, 0)
        heart_rate = None if fitness_discipline == 'Running' else PosNormal(131.91, 19.36)
        avg_incline = None
        avg_pace = None
        writer.writerow([
            workout_timestamp, 
            workout_live_on_demand,
            instructor_name,
            length,
            fitness_discipline,
            type,
            title,
            class_timestamp,
            total_output,
            avg_watts,
            avg_resistance,
            avg_cadence,
            avg_speed,
            distance,
            calories,
            heart_rate,
            avg_incline,
            avg_pace
        ])