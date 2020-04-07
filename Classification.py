from DataAnalytics import preprocess
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


def logistic_regression(x_train, x_test, y_train, y_test):
    
    logreg = LogisticRegression(C=100, random_state=42)
    logreg.fit(x_train, y_train)

    y_pred = logreg.predict(x_test)

    correct = (y_test == y_pred).sum()
    incorrect = (y_test != y_pred).sum()
    accuracy = correct / (correct + incorrect) * 100

    print("Accuracy for Logistic Regression", accuracy)

def naive_bayes_classifier(x_train, x_test, y_train, y_test):

    model = GaussianNB()
    model.fit(X=x_train, y=y_train)

    y_pred = model.predict(x_test)

    correct = (y_test == y_pred).sum()
    incorrect = (y_test != y_pred).sum()
    accuracy = correct / (correct + incorrect) * 100

    print("Accuracy for Naive Bayes : ", accuracy)

def k_nearest_neighbour(x_train, x_test, y_train, y_test):

    model = KNeighborsClassifier(n_neighbors=5, algorithm='auto', p=2)
    model.fit(x_train, y_train)

    # Prediction
    y_pred = model.predict(x_test)

    correct = (y_test == y_pred).sum()
    incorrect = (y_test != y_pred).sum()
    accuracy = correct / (correct + incorrect) * 100

    print("Accuracy for K Nearest Neighbour : ", accuracy)

def decision_tree(x_train, x_test, y_train, y_test):

    model = DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth=4, random_state=42)
    model.fit(x_train, y_train)

    # Prediction
    y_pred = model.predict(x_test)

    correct = (y_test == y_pred).sum()
    incorrect = (y_test != y_pred).sum()
    accuracy = correct / (correct + incorrect) * 100

    print("Accuracy for Decision Tree : ", accuracy)


def create_data_for_model(dataset):
    x = []
    y = []

    for key in dataset:
        row = []

        row.append(dataset[key].get('Open'))
        row.append(dataset[key].get('Close'))

        if (dataset[key].get('PercentChange') >= 0.0):
            y.append(1)
        else:
            y.append(0)

        x.append(row)

    return x, y

def create_models(train_data, test_data):
    x_train, y_train = create_data_for_model(train_data)
    x_test, y_test = create_data_for_model(test_data)

    logistic_regression(x_train, x_test, y_train, y_test)
    naive_bayes_classifier(x_train, x_test, y_train, y_test)
    k_nearest_neighbour(x_train, x_test, y_train, y_test)
    decision_tree(x_train, x_test, y_train, y_test)


def classification(testingFile, traningFile):
    dict_train_data = preprocess(traningFile, False)
    dict_test_data = preprocess(testingFile, False)

    create_models(dict_train_data, dict_test_data)

classification('1150.xlsx', '1150_2018.xlsx')
