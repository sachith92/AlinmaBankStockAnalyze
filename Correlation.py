from DataAnalytics import preprocess
import numpy as np
from scipy.stats import spearmanr
from scipy.stats import pearsonr


def Correlation(filename):
    dict_data = preprocess(filename, False)

    open_value = []
    close_value = []
    pct_change = []
    avg_open_close = []
    turn_over = []

    for key in dict_data:
        if dict_data[key].get('Close') != 0 and dict_data[key].get('Open') != 0:
            open_value.append(dict_data[key].get('Open'))
            close_value.append(dict_data[key].get('Close'))
            pct_change.append(dict_data[key].get('PercentChange'))
            avg_open_close.append(
                (dict_data[key].get('Open') + dict_data[key].get('Close')) / dict_data[key].get('Open'))
            turn_over.append(dict_data[key].get('Turnover'))

    corr, _ = spearmanr(open_value, pct_change)
    print("Spearman Correlation: %.3f" % corr)

    pcorr, _ = pearsonr(open_value, pct_change)
    print("Pearson Correlation: %.3f" % pcorr)

    corr2, _ = spearmanr(close_value, pct_change)
    print("Spearman Correlation: %.3f" % corr2)

    pcorr2, _ = pearsonr(close_value, pct_change)
    print("Pearson Correlation: %.3f" % pcorr2)

    corr3, _ = spearmanr(avg_open_close, pct_change)
    print("Spearman Correlation: %.3f" % corr2)

    pcorr3, _ = pearsonr(avg_open_close, pct_change)
    print("Pearson Correlation: %.3f" % pcorr3)

    corr4, _ = spearmanr(turn_over, pct_change)
    print("Spearman Correlation: %.3f" % corr4)

    pcorr4, _ = pearsonr(turn_over, pct_change)
    print("Pearson Correlation: %.3f" % pcorr4)


Correlation('1150.xlsx')
