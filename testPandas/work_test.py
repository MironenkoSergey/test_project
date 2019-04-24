from pandas import DataFrame, concat
import numpy as np


# instead using concate and merge
# we can use df2[df.keys()[0]] = df[df.keys()[0]]
# because we have only one key in first frame
# Example:
if(__name__ == '__main__'):
    df = DataFrame({'f_data':['2015-01-01', '2015-01-02',
                              '2015-01-03', '2015-01-04',
                              '2015-01-05', '2015-01-06',
                              '2015-01-07', '2015-01-08', ]})
    # print(df)
    array = np.zeros((7,7))
    list_with_countries = ['Japan', 'China',
                           'USA', 'Hong Kong',
                           'Russia', 'UK',
                           'Canada']

    # print(array)
    df2 = DataFrame(data=array, columns=list_with_countries)
    # print(df2)
    df2[df.keys()[0]] = df[df.keys()[0]]
    print(df2)
