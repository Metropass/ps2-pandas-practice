import pandas as pd
import psutil


class PS2Data:
    def __init__(self):
        self.__file = 'PS2-GAMEID-TITLE-MASTER.csv'
        self.__df = pd.read_csv('PS2-GAMEID-TITLE-MASTER.csv', sep=';')

    def searchByRegion(value):
        #Values: 1 - Americas, 2 - Europe, 3 - Japan
        try:
            q = None
            if value == 1:
                s = ['SLUS', 'SCES']
                q = self.__df[self.__df['GameID'].str.contains('|'.join(s)])
                print(q)
            elif value == 2:
                s = ['SCES', 'SLES']
                q = self.__df[self.__df['GameID'].str.contains('|'.join(s)])
                print(q)
            elif value == 3:
                s = ['SCPS', 'SLPS']
                q = self.__df[self.__df['GameID'].str.contains('|'.join(s)])
                print(q)
            return q
        except ValueError:
            print("NOT IN RANGE")

    def searchByID(IDValue):
        df_search = self.__df[self.__df['GameID'] == IDValue]
        if df_search.empty:
            print('The search returned empty')
            return None
        else:
            print(df_search)
            return df_search
