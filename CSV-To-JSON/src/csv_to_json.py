import pandas as pd
import json

def return_list(PATH):
    
    data = pd.read_csv(PATH)
    columns = data.columns

    if columns[0] == "Index":
        columns = columns[1:]

    data = data.fillna(0)

    json_arr = []

    for i in range(data.shape[0]):

        record = {}

        for column in columns:
            key = data[column][i]

            record[column] = key

        json_arr.append(record)

    return json_arr

def make_json(arr, path):

    with open(path, "w") as file:
        json.dump(arr, file, indent=4)