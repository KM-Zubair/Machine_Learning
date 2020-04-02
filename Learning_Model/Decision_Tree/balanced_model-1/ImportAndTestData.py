"""
Created on Thu April 2 13:21:14 2020

@author: KM Zubair
"""


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score 


# list/array to store data
data = []

# Using Pandas to read File
# PLEASE CHANGE THE FILE LOCATION ACCODING TO YOUR PREFERENCE WHILE RUNNING THIS CODE
data = pd.read_csv("G:\Sem 2\IS CSC 2301 Section 02\QUIZ 2\quiz2\KMZubair\FILE.csv")


# Using LabelEncoder and .fit_transform to Get the string fileds connected to numbers
# since Machine Learning Tress can only guess using numbers
la_ramtype = LabelEncoder()
la_hdd = LabelEncoder()
la_display = LabelEncoder()

# Using .fit_transform to make columns with numbers referencing the columns with strings
data['Ram_Type_n'] = la_ramtype.fit_transform(data['Ram Type'])
data['HDD_n'] = la_hdd.fit_transform(data['HDD'])
data['Display_n'] = la_display.fit_transform(data['Display'])

data.head()

# Inserting all columns from data except 'Label','Display','HDD','Ram Type'
Features = data.drop(['Label','Display','HDD','Ram Type'], axis = 'columns')

# It's easy to Use only one input or column for the Label 
# Failure to do that brings complexity to use the formula for calculating accuracy
Label = data['Label']

# Putting formula to use as variables for decision tree
X_train = [] 
X_test = []

y_train = [] 
y_test = []


# This will take 80% data randomly from anywhere of the total data to train itself
X_train, X_test, y_train, y_test = train_test_split(Features, Label, test_size = 0.2, random_state=1)

# Create a Blank Classifier
# Choosing Decision Tree as it suits the most fot this kind of random dataset
clsfr = tree.DecisionTreeClassifier()

# Train the Model
clsfr = clsfr.fit(X_train, y_train)

# Do the prediction
y_pred = clsfr.predict(X_test)


# Measure and Print the accuracy

print('Accuracy :', accuracy_score(y_test,y_pred)*100) 

# We can also measure accuracy by implementing this formula after importing metrics
# from sklearn import metrics
# print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)
