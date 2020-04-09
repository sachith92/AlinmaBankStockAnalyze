# Import the required libraries
import numpy as np


# Sigmoid function
def sigmoid(z):
    s = 1 / (1 + np.exp(-z))
    return s


# Initialize weight and bias parameters
def initialize_weights_and_bias(dimension):
    w = np.full((dimension,1), 0.01)
    b = 0.0
    return w, b


# Forward and Backward propagation to find out Cost and Gradient for this training data set
def propagation(w, b, x, y):
    p = x.shape[1]
    
    # forward propagation
    s = sigmoid(np.dot(w.T, x) + b)
    loss = -1 *(y * np.log(s) + (1 - y) * np.log(1 - s))
    cost = (np.sum(loss)) / p
    
    # backward propagation
    dw = (np.dot(x, ((s - y).T))) / p
    db = np.sum(s - y) / p
    gradients = {"dw": dw, "db": db}

    return cost, gradients


# Optimize the weight and bias
def optimize(w, b, x, y, learning_rate, number_of_iterarion):
    
    costs = []
    cost_list = []
    index = []
    
    for i in range(number_of_iterarion):
        
        # calculate cost and gradient in each iteration
        cost, gradients = propagation(w, b, x, y)

        costs.append(cost)
        w = w - learning_rate * gradients["dw"]
        b = b - learning_rate * gradients["db"]

        # print cost each 20 iterations
        if i % 20 == 0:
            #print ("Cost after iteration %i: %f" %(i, cost))
            cost_list.append(cost)
            index.append(i)

    parameters = {"w": w,"b": b}

    return parameters, gradients, costs


# Predict whether the label is 0 or 1 using learned logistic regression parameters (w, b)
def predict(w, b, x):
    p = x.shape[1]
    
    z = sigmoid(np.dot(w.T, x) + b)
    Y_prediction = np.zeros((1, p))

    
    for i in range(z.shape[1]):
        if z[0, i] <= 0.5:
            Y_prediction[0, i] = 0
        else:
            Y_prediction[0, i] = 1

    return Y_prediction


# Implementation of logistic regreation function
def logistic_regression(x_train, x_test, y_train, y_test, learning_rate, num_iterations):
    x_train = np.array(x_train)
    x_train = x_train.T

    x_test = np.array(x_test)
    x_test = x_test.T

    y_train = np.array(y_train)
    y_train = y_train.T

    y_test = np.array(y_test)
    y_test = y_test.T

    w, b = initialize_weights_and_bias(x_train.shape[0])

    parameters, gradients, costs = optimize(w, b, x_train, y_train, learning_rate, num_iterations)
    
    y_prediction = predict(parameters["w"],parameters["b"],x_test)

    return (100 - np.mean(np.abs(y_prediction - y_test)) * 100)