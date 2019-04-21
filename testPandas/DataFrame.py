import pandas as pd
import matplotlib.pyplot as plt

# обзор DataFrame
df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
print(df)
df.sort_index()
print(df.info(), '\n')
# использование mean
print("Средняя цена акций в 2012 на закрытии")
print(df.loc['2012-Feb', 'Close'].mean(), '\n')
print("Средняя цена акций в 2012-2015 на закрытии")
print(df.loc['2015-Feb':'2012-Feb', 'Close'].mean(), '\n')
# использование метода resample, W-week и тд
print("Средняя цена закрытия каждую неделю")
print(df.resample('W')['Close'].mean(), '\n')
# визуализация на графике
allTime = df.loc['2017-Feb':'2012-Feb', ['Open', 'Close']]
oneYear = df.loc['2015-Aug':'2014-Feb', ['Open', 'Close']]
allTime.plot()
oneYear.plot()
plt.show()



