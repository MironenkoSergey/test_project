import pandas as pd

# просмотр Series
series1 = pd.Series([5, 6, 7, 8, 9, 10])
print(series1, series1.index, '\n', series1.values)
# доступ по элементу
print("Fours element is ", series1[4])
# явное определение индексов
series2 = pd.Series(["one", "two", "three", "four", "five"],
                    index=['Mike', 'Den', 'Andrew', 'Lina', 'Serzh'])
# множественное присваивание
series2['Mike', 'Den', 'Lina'] = "zero"
# добавления имен индексов и атрибутов
series2.name = 'budget'
series2.index.name = 'person'
# фильтрация и действия с помощью индекса
print(series2[series2 != "two"] + " dollars")
# наличие элемента в Series
print('Serzh' in series2)

