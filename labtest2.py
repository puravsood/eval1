from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score
#from sklearn.linear_model import NaiveBayes
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=load_diabetes()
X=df.data
y=df.target
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.6)
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.8)
plt.scatter(dia[0],dia[9])
plt.show
dia=pd.DataFrame(X)
print("No.of features = ", dia.count(axis=1))
dia
