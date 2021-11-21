import pandas as pd
import numpy as np


class MetaDataExtractor:  # class creation
    def __init__(self):  # constructor
        self.data = pd.DataFrame(columns=['rows', 'columns', 'nullvalues', 'fields', 'dataTypes'])

    @staticmethod
    def get_data(fn):
        """gets the data from json file"""
        rdf = pd.read_json(fn)
        return rdf

    def metadata(self, df):
        rows = df.shape[0]
        columns = df.shape[1]
        columnsnames = list(df.columns)
        nullvalues = df.isnull().sum()
        dt = ""
        for x in range(len(columnsnames)):
            dt += "{0}:{1}\n".format(columnsnames[x], type(df.iloc[:, x][1]))
        self.data[len(self.data.index)] = [rows, columns, columnsnames, nullvalues, dt]

    def evaluate_get(self, path, f_types):
        for i, j in path, f_types:

            if j == ".csv":
                df = pd.read_csv(i)
                self.metadata(df)
            elif j == ".xlsx":
                df = pd.read_excel(i)
                self.metadata(df)
            elif j == ".tsv":
                df = pd.read_excel(i)
                self.metadata(df)
            else:
                print("invalid")

    def get_path(self, rdf):
        """gets filename and file type"""
        path = rdf[["Path"]].to_numpy()
        filetype = rdf[["File Type"]].to_numpy()
        return path, filetype

    def runner(self):
        ...


if __name__ == "__main__":
    obj = MetaDataExtractor()
    obj.runner()
