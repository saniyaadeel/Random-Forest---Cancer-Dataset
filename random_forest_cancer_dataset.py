# -*- coding: utf-8 -*-
"""Random Forest - Cancer Dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#Reading dataset and visualising
df = churn_df = pd.read_csv('data.csv')
df.head()

#Extracting predictors and labels
label = df['diagnosis']
df = df.drop(columns=['diagnosis'])

#Data preprocessing
df.drop('Unnamed: 0', axis = 1, inplace = True)
df.info() # since only one object predictor so convert into dummies using below code

#Converting precondition into dummy variable
df = pd.get_dummies(df, drop_first= True)
df

#Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df, label, test_size = 0.33, random_state = 42)

#Applying Random Forest to our data
clf = RandomForestClassifier(n_estimators=20)
clf.fit(X_train, y_train)
print('The accuracy of our model is:',clf.score(X_test, y_test))

#Checking if our accuracy is correct
print('The mean number of people having malignant cancer:',np.mean(label=='M'))
print('The mean number of people having benign cancer:',np.mean(label=='B'))

"""Since the accuracy of the model is greater than the majority group mean, it means the model is a good fit."""

#Ensuring accuracy by checking again
y_pred = clf.predict(X_test)
print('Confusion Matrix',confusion_matrix(y_test,y_pred))
print('Classification Report',classification_report(y_test,y_pred))
print('Accuracy score',accuracy_score(y_test, y_pred))

#Visualising the most important features
fi = clf.feature_importances_
features = np.array(df.columns)
df_fi = pd.DataFrame(fi*1000, features)
df_fi = df_fi.sort_values(0)
df_fi.plot(kind='barh', figsize = (10,8), color = 'yellowgreen', title = 'Feature Importance for features', legend = False, edgecolor = 'black')
plt.xlabel('Feature Importances')

