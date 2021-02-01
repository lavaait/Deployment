# Simple Linear Regression

# Importing the libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import os
os.chdir("/home/gramophone/Downloads/simple-Linear-Regression/simple_linear_regression.py")

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


#dumping the model in the disk savable format
# save the model to disk
import pickle
filename = '/home/gramophone/Downloads/simple-Linear-Regression/finalized_model.pkl'
pickle.dump(regressor, open(filename, 'wb'))

# Predicting the Test set results
regressor.predict(X_test)


#reloading the model object
regressor = pickle.load(open(filename,'rb'))




