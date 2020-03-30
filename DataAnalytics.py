import pandas as pd
import array 

def preProcessData(filename):
    data = pd.read_excel(filename)
    df = pd.DataFrame(data, columns=['Time', 'Open', 'Close', 'Chgange', 'PercentChange'])

    dataDictionary = {}
    for index, row in df.iterrows():
        dataDictionary[row['Time']] = datarow = {'Open': row['Open'], 'Close':row['Close'], 'Change':row['Chgange'], 'PercentChange':row['PercentChange']}

    return dataDictionary


print(preProcessData('1150.xlsx'))
