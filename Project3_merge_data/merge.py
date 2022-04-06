import numpy as np
import pandas as pd

company_industry = pd.read_csv(r'data/Exp 3_company_industry.csv')
industry = pd.read_csv(r'data/Exp 3_industry.csv')
namechange = pd.read_csv(r'data/Exp 3_namechange.csv')
stock_basic = pd.read_csv(r'data/Exp 3_stock_basic.csv')
stock_company = pd.read_csv(r'data/Exp 3_stock_company.csv')

industry.rename(columns={'industry_3_code': 'industry'}, inplace=True)
company_industry.rename(columns={'company_display_name': 'name'}, inplace=True)

stock_basic = stock_basic[stock_basic['ts_code'].str.contains('SH')]
stock_company = stock_company[stock_company['ts_code'].str.contains('SH')]
namechange = namechange[namechange['ts_code'].str.contains('SH')][['ts_code','name']]

merge1 = pd.merge(stock_basic, stock_company, on='ts_code')
merge_industry = pd.merge(company_industry, industry, on='industry')
merge_industry_name = pd.merge(merge_industry, namechange, on='name').drop_duplicates(subset=['ts_code'])

merge_res = pd.merge(merge1,merge_industry_name, on='ts_code')
# print(merge_industry_name.columns.values)
# print(merge_res.shape)
# print(merge_res.columns.values)

merge_res.to_csv(r'merge_res.csv', encoding='UTF8')