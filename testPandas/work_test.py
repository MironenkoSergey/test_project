from pandas import DataFrame
import numpy as np



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


    df.append(df2, ignore_index=True, sort=True)
    print(df)
