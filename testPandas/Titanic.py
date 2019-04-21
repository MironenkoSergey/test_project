import pandas as pd
import os

# считывание данных из csv
titanik_df = pd.read_csv('titanic.csv')
# подсчитаем выжевших пассажиров по полу и классу каюты
print("Выжившие по полу")
print(titanik_df.groupby(['Sex', 'Survived'])['PassengerID'].count(), '\n')
print("Выжившие по классу каюты")
print(titanik_df.groupby(['PClass', 'Survived'])['PassengerID'].count(), '\n')
# сводные таблицы
# подсчитать количество женщин в каютах каждого класса
pvt = titanik_df.pivot_table(index='Sex', columns='PClass',
                             values='Name', aggfunc='count')
print("Женщин в каждом классе")
print(pvt.loc['female', ['1st', '2nd', '3rd']], '\n')
