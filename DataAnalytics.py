import pandas as pd
import numpy as np


def preprocess(filename):
    dataFrame = pd.read_excel(filename, usecols=['Time', 'Open', 'Close', 'Chg', 'PctChg'])
    print(dataFrame.columns.ravel())

    # Drop any empty data points in the excel
    for index, rows in dataFrame.iterrows():
        for columns in rows:
            if columns == '':
                dataFrame.drop(index, inplace=True)
                print("Dropped Index: " + index)

    """ Normalize Data Set """
    dataFrame.Open = minmaxnormalization(dataFrame.Open)
    dataFrame.Close = minmaxnormalization(dataFrame.Close)
    dataFrame.Chg = minmaxnormalization(dataFrame.Chg)
    dataFrame.PctChg = minmaxnormalization(dataFrame.PctChg)

    # print(dataFrame)

    dataDictionary = {}
    for index, row in dataFrame.iterrows():
        dataDictionary[row['Time']] = datarow = {'Open': row['Open'], 'Close': row['Close'], 'Change': row['Chg'],
                                                 'PercentChange': row['PctChg']}

    return dataDictionary


""" 
    Used Min-Max Standard Normalization Technique to Normalize the data set
    
    OriginalValue = (OriginalValue - min(Data Set) )/(max(DataSet) - min(DataSet))
"""
def minmaxnormalization(dataFrame):
    normalized_data = (dataFrame - np.min(dataFrame)) / (np.max(dataFrame) - np.min(dataFrame))

    return normalized_data


preprocess('1150.xlsx')
