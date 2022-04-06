import numpy as np
import pandas as pd
from py2neo import Graph,Node,Relationship
from py2neo.matching import NodeMatcher

graph = Graph('http://localhost:7474',auth=('data','data'))

#
# if len(nodelist) < 1:
#     node_1 = Node("Person",name="Peter")
#     graph.create(node_1)
#
# matcher = NodeMatcher(graph)
# nodelist = list(matcher.match('Person', name="Peter"))

df = pd.read_csv(r'data.csv')

area_province = []
area_city = []
person = []
industry = []

matcher = NodeMatcher(graph)

for index, row in df.iterrows():
    print(row['name'])

    node_company, node_area, node_industry, node_secretary, node_manager, node_chairman = None, None, None, None, None, None

    node_company = Node("company", name=row['name'])
    graph.create(node_company)

    if row['province'] not in area_province:
        node_area = Node("area", province=row['province'])
        area_province.append(row['province'])
        graph.create(node_area)
    else:
        nodelist = list(matcher.match('area', province=row['province']))
        node_area = nodelist[0]

    if row['chairman'] != None:
        if row['chairman'] not in person:
            node_chairman = Node("person", name=row['chairman'])
            person.append(row['chairman'])
        else:
            nodelist = list(matcher.match("person", name=row['chairman']))
            node_chairman = nodelist[0]

    # if row['manager'] != None:
    #     if row['manager'] not in person:
    #         node_manager = Node("person", name=row['manager'])
    #         person.append(row['manager'])
    #     else:
    #         nodelist = list(matcher.match("person", name=row['manager']))
    #         node_manager = nodelist[0]
    #
    # if row['secretary'] != None:
    #     if row['secretary'] not in person:
    #         node_secretary = Node("person", name=row['secretary'])
    #         person.append(row['secretary'])
    #     else:
    #         nodelist = list(matcher.match("person", name=row['secretary']))
    #         node_secretary = nodelist[0]

    if row['industry_1'] not in industry:
        node_industry = Node("industry", industry=row['industry_1'])
        industry.append(row['industry_1'])
    else:
        nodelist = list(matcher.match("industry", industry=row['industry_1']))
        node_industry = nodelist[0]

    graph.create(node_chairman)
    # graph.create(node_manager)
    # graph.create(node_secretary)
    graph.create(node_industry)

    r_in = Relationship(node_company, '位于', node_area)
    r_c = Relationship(node_chairman, '担任主席', node_company)
    # r_m = Relationship(node_manager, '担任经理', node_company)
    # r_s = Relationship(node_secretary, '担任秘书', node_company)
    r_indus = Relationship(node_company, "属于行业", node_industry)

    graph.create(r_in)
    graph.create(r_c)
    # graph.create(r_m)
    # graph.create(r_s)
    graph.create(r_indus)

# node_company = Node("name", name=df['name'][1])
# node_area = Node("area", province=df['province'][1])
# node_chairman = Node("person", name=df['chairman'][1])
# node_manager = Node("person", name=df['manager'][1])
# node_secretary = Node("person", name=df['secretary'][1])
# node_industry = Node("industry", industry=df['industry_1'][1])
# graph.create(node_company)
# graph.create(node_area)
# graph.create(node_chairman)
# graph.create(node_manager)
# graph.create(node_secretary)
# graph.create(node_industry)
#
# r_in = Relationship(node_company, '位于', node_area)
# r_c = Relationship(node_chairman, '担任主席', node_company)
# r_m = Relationship(node_manager, '担任经理', node_company)
# r_s = Relationship(node_secretary, '担任秘书', node_company)
# r_indus = Relationship(node_company, "属于行业", node_industry)
#
# graph.create(r_in)
# graph.create(r_c)
# graph.create(r_m)
# graph.create(r_s)
# graph.create(r_indus)