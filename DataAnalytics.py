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
    dataFrame = pd.read_excel(filename,
                              usecols=['TRANSACTION_DATE', 'THEORETICAL_OPEN_RATIO', 'PCT_CHANGE'])

    # Drop any empty data points in the excel
    for index, rows in dataFrame.iterrows():
        for columns in rows:
            if columns == 1000 or columns == 0:
                dataFrame.drop(index, inplace=True)
                print("Dropped Index:", index)
                break

    dataFrame = dataFrame.dropna()
    """
    Normalize Data Set if needed
    """
    if bIsNormalize:
        dataFrame.CUSTOMIZE = min_max_normalization(dataFrame.CUSTOMIZE)

    # Insert data to data dictionary
    dataDictionary = {}
    for index, row in dataFrame.iterrows():
        dataDictionary[row['TRANSACTION_DATE']] = datarow = {'THEORETICAL_OPEN_RATIO': row['THEORETICAL_OPEN_RATIO'],
                                                             'PCT_CHANGE': row['PCT_CHANGE']}

    return dataDictionary


# preprocess('1150_HISTORY_ADJUSTED_2018.xlsx', False)
