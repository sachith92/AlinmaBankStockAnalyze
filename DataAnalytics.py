import pandas as pd
import numpy as np

""" 
    Used Min-Max Standard Normalization Technique to Normalize the data set
    OriginalValue = (OriginalValue - min(Data Set) )/(max(DataSet) - min(DataSet))
"""


def min_max_normalization(dataFrame):
    normalized_data = (dataFrame - np.min(dataFrame)) / (np.max(dataFrame) - np.min(dataFrame))

    return normalized_data


def preprocess(filename, bIsNormalize):
    data_frame = pd.read_excel(filename, usecols=['Time', 'Open', 'Close', 'Chg', 'PctChg', 'Turnover'])

    # # Drop any empty data points in the excel
    # for index, rows in dataFrame.iterrows():
    #     for columns in rows:
    #         if columns == '' and columns == 0:
    #             dataFrame.drop(index, inplace=True)
    #             print("Dropped Index: %d", index)

    dataFrame = data_frame.dropna()

    """ 
    Normalize Data Set if needed
    """
    if bIsNormalize:
        dataFrame.Open = min_max_normalization(dataFrame.Open)
        dataFrame.Close = min_max_normalization(dataFrame.Close)
        dataFrame.Chg = min_max_normalization(dataFrame.Chg)
        dataFrame.PctChg = min_max_normalization(dataFrame.PctChg)
        dataFrame.Turnover = min_max_normalization(dataFrame.Turnover)

    # Insert data to data dictionary
    dataDictionary = {}
    for index, row in dataFrame.iterrows():
        dataDictionary[row['Time'].strip()] = datarow = {'Open': row['Open'], 'Close': row['Close'],
                                                         'Change': row['Chg'],
                                                         'PercentChange': row['PctChg'], 'Turnover': row['Turnover']}

    return dataDictionary


#print(preprocess('1150.xlsx', False))
