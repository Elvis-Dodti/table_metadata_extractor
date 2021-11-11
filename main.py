import pandas as pd
import numpy as np

# create an Empty DataFrame object
data = pd.DataFrame(columns=['rows', 'columns', 'nullvalues', 'fields', 'dataTypes'])


def metadata(df):
    rows = df.shape[0]
    columns = df.shape[1]
    columnsnames = list(df.columns)
    nullvalues = df.isnull().sum()
    dt = ""
    for x in range(len(columnsnames)):
        dt += "{0}:{1}\n".format(columnsnames[x], type(df.iloc[:, x][1]))
    data[len(data.index)] = [rows, columns, columnsnames, nullvalues, dt]


def evaluate_get(path,types):
    for i in path:

     if i == ".csv":
            df = pd.read_csv(i)
            metadata(df)
     elif i == ".xlsx":
            df = pd.read_excel(i)
            metadata(df)
     elif i == ".tsv":
            df = pd.read_excel(i)
            metadata(df)

     else:
            print("invalid")


def get_path(rdf):
    s_array = rdf[["FileName"]].to_numpy()
    print(s_array)

    t_array = rdf[["Path"]].to_numpy()
    print(t_array)
    return s_array, t_array


def get_data():
    rdf = pd.read_json("retrieved_data.json")
    return rdf



if __name__ == "__main__":
        x = get_data()
        fp,dt = get_path(x)
        evaluate_get(fp, dt)
        print(data)













