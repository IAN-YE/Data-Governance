import pandas as pd
import json
from pyecharts.charts import Bar, Timeline, Map, Tree
from pyecharts import options as opts

data = pd.read_csv(r'data/athlete_events.csv')

def show_olympic_athete(season) -> Map:
    tl = Timeline()
    if season == "summer":
        athlete = data[data['Season'] == 'Summer']
    else:
        athlete = data[data['Season'] == 'Winter']
    years = athlete['Year'].sort_values().unique().tolist()
    number = len(years)
    data_country = data.groupby(by=['Year','Team'])['ID'].count().reset_index()
    print(data_country)

    for i in range(number):
        year = years[i]
        country_list = data_country[data_country['Year']==year][['Team','ID']].values.tolist()
        map = (
            Map()
            .add("参赛人数", country_list, "world",
                 is_map_symbol_show=False)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年奥运会各国运动员参赛情况".format(year)),
                visualmap_opts=opts.VisualMapOpts(max_=1000, range_color=['#ffce7b', '#ef4136'])
            )
        )
        tl.add(map, "{}年".format(year))
    return tl


def show_sports(year, sports):
    with open('./data/event_json.json', 'r', encoding='utf8') as f:
        events = json.load(f)

    for event in events:
        if year == event["name"]:
            tmp = event["children"]
            for i in tmp:
                if sports == i["name"]:
                    data = i
                    break

    map = (
        Tree()
            .add("", [data])
            .set_global_opts(title_opts=opts.TitleOpts(title="{}年{}项目子项展示".format(year,sports)))
    )

    return map


