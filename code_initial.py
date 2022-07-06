import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,recall_score, precision_score
from sklearn.linear_model import LogisticRegression
import argparse

def Create_Model():
    # Label Encoded Dataset
    # Iris-setosa = 0
    # Iris-versicolor = 1
    # Iris-virginica = 2
    ## import dataset
    df = pd.read_csv("Iris_Flower_Dataset.csv")
    
    ## Separate dependent and independent features
    x = df.iloc[:, 1:-1].values
    y = df.iloc[:, -1].values
    
    ## Split the into training and testing
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 10)
    
    ## Create Logistic regression model
    log_reg = LogisticRegression(fit_intercept=True, penalty='l2', 
                                 multi_class="ovr",
                                 random_state = 10)
    log_reg.fit(x_train,y_train)
    y_pred = log_reg.predict(x_test)
    
    ## Metrics 
    accuracy = accuracy_score(y_pred, y_test)
    recall = recall_score(y_pred, y_test,average="weighted")
    precision = precision_score(y_pred, y_test,average="weighted")
    
    print("Accuracy==>",accuracy)
    print("Recall==>",recall)
    print("Precision==>",precision)

## call the create model function
Create_Model()

