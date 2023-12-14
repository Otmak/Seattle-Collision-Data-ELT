import pandas as pd
import os

my_data = pd.read_csv(f'{os.getcwd()}/data/SDOT_Collisions_All_Years.csv')


def extract(job, data):
    result = dict()
    my_list = list()
    i = 0
    
    while i < len(data):
        for key, value in job.items():
            if key in data:
                result[value] = data.iloc[i][key]
        my_list.append(result)
        print(result)
        i += 1

    return my_list
