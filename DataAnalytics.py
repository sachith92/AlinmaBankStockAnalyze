import pandas as pd


def preprocess(filename):
    data = pd.read_excel(filename)
    df = pd.DataFrame(data, columns=['Time', 'Open', 'Close', 'Chg', 'PctChg'])

    dataDictionary = {}
    for index, row in df.iterrows():
        dataDictionary[row['Time']] = datarow = {'Open': row['Open'], 'Close': row['Close'], 'Change': row['Chg'],
                                                 'PercentChange': row['PctChg']}

    return dataDictionary


print(preprocess('1150.xlsx'))
