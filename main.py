import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('new.csv')
tst = df[['price']]
tst.plot(kind='line', y='price', color='pink')
plt.show()
mn_cost = min(tst['price'])
mx_cost = max(tst['price'])
ind_buy = df[['price']].idxmin()
ind_sell = df[['price']].idxmax()
print('Дата покупки: ', *df['date'].iloc[ind_buy], '\n', 'Дата продажи: ', *df['date'].iloc[ind_sell], '\n', 'Разница: ', mx_cost - mn_cost)

