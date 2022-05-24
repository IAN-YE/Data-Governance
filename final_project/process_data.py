import numpy as np
import pandas as pd
import json

data = pd.read_csv('data/athlete_events.csv')

# with open("data/city.txt", "a") as f_city:
#     for city in data['City'].unique():
#         print(city, file=f_city)
#     f_city.close()
#
# with open("data/sports.txt", "a") as f_sport:
#     for city in data['Sport'].unique():
#         print(city, file=f_sport)
#     f_sport.close()
#
# with open("data/events.txt", "a") as f_event:
#     for event in data['Event'].unique():
#         print(event, file=f_event)
#     f_event.close()

def generate_events_json():
    events_list = data[['Year','Sport','Event']].drop_duplicates().sort_values(by=['Year','Sport','Event']).reset_index()
    sport, event, year = None, None, None
    res, sports, events = [], [], []
    for index, row in events_list.iterrows():
        year_now = row['Year']
        sport_now = row['Sport']
        if year_now != year and year != None:
            res.append({"name": year, "children": sports})

        if sport != sport_now and sport != None:
            sports.append({"name": sport, "children": events})
            events = []

        events.append({"name": row['Event']})
        sport = sport_now
        year = year_now

    return res

# res = generate_events_json()
# with open('data/event_json.json', 'w') as f:
#     f.write(json.dumps(res))