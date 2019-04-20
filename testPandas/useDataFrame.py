from pandas import DataFrame as df

# создание фрейма
frame1 = df({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]})
print(frame1, '\n')
# обращение к столбцу по имени
# столбец является тем же Serial
# значит DataFrame является набором Serials
print(frame1['country'], '\n', type(frame1['country']), '\n')
# индексирование происходит по столбцам и строкам
print(frame1.columns, '\n', frame1.index, '\n')
# изменение индексов явно
frame1.index = ['KZ', 'RU', 'BY', 'UA']
frame1.index.name = 'Country code'
# доступ по индексам также возможно осуществлять с помощью .loc и .iloc
print(frame1.iloc[3], '\n')
# с помощью .loc имеется возможность фильтрации
print(frame1.loc[['KZ', 'RU'], 'population'], '\n')
# также фильтрация возможна с помощью булевых массивов
print(frame1[frame1.population > 10][['country', 'square']], '\n')
# добавление, удаление и переименование
frame1['density'] = frame1['population'] / frame1['square'] * 1000000
frame1['unated'] = 'SNG'
del frame1['unated']
frame1 = frame1.rename(columns={'country': 'Country'})
print(frame1, '\n')
# сохранение DataFrame в .csv
frame1.to_csv("SNG.csv")
