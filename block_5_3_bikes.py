

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_column', None)
pd.set_option('display.max_colwidth', None)


plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pd.read_csv('/home/jinelli/PycharmProjects/pythonProject/datasets/bikes.csv',
                       sep=',', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
fixed_df[:3]
fixed_df['Berri 1'][:10]
fixed_df['Berri 1'].plot()
fixed_df.plot(figsize=(15, 10))
print(fixed_df)
berri_bikes = fixed_df[['Berri 1']].copy()
print(berri_bikes)
berri_bikes[:5]
berri_bikes.index.day
berri_bikes.index.weekday
berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday
print(berri_bikes[:5])
print()
