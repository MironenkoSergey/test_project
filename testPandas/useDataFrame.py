from pandas import DataFrame as df

# создание фрейма
frame1 = df({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]})
print(frame1)
# добавление коммента
