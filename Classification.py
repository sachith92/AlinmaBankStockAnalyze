import numpy as np
import matplotlib.pyplot as plt
from DataAnalytics import preprocess
from logistic_regression import logistic_regression
from sklearn.model_selection import train_test_split


def logistic_regression_(x_train, x_test, y_train, y_test):

    learning_rate = [0.05, 0.04, 0.03, 0.02, 0.01, 0.005]
    test_accuracy_learning_rate = np.empty(len(learning_rate))

    for i, k in enumerate(learning_rate):
        accuracy = logistic_regression(x_train, x_test, y_train, y_test, learning_rate=k, num_iterations=500)
        test_accuracy_learning_rate[i] = accuracy
        print("%0.2f' Accuracy of the prediction when learning rate = %0.2f'" %(accuracy, k))

    plt.plot(learning_rate, test_accuracy_learning_rate, label='Accuracy against learing rate')
    plt.legend()
    plt.xlabel('Learning Rate')
    plt.ylabel('Accuracy')
    plt.show()
    

    iterations = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000]
    test_accuracy_iterations = np.empty(len(iterations))

    for j, l in enumerate(iterations):
        accuracy = logistic_regression(x_train, x_test, y_train, y_test, learning_rate=0.01, num_iterations=l)
        test_accuracy_iterations[j] = accuracy
        print("%0.2f' Accuracy of the prediction when number of iterations = %2d'" % (accuracy, l))

    plt.plot(iterations, test_accuracy_iterations, label='Accuracy against iterations')
    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Accuracy')
    plt.show()

def create_data_for_model(dataset):
    x = []
    y = []

    for key in dataset:
        row = []

        row.append(dataset[key].get('OPEN'))
        row.append(dataset[key].get('CLOSE'))

        if (dataset[key].get('PCT_CHANGE') >= 0.0):
            y.append(1)
        else:
            y.append(0)

        x.append(row)

    return x, y

def create_models(train_data, test_data):
    #x_train, y_train = create_data_for_model(train_data)
    #x_test, y_test = create_data_for_model(test_data)

    x, y = create_data_for_model(train_data)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

    logistic_regression_(x_train, x_test, y_train, y_test)


def classification(testingFile, traningFile):
    dict_train_data = preprocess(traningFile, False)
    dict_test_data = preprocess(testingFile, False)

    create_models(dict_train_data, dict_test_data)

classification('1150_HISTORY_ADJUSTED_2019.xlsx', '1150_HISTORY_ADJUSTED_2018.xlsx')
