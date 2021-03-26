"""
Sheth Riya Nimish
A0176880R
e0235287@u.nus.edu
Final Year Project

"""

import sys
import pickle
import docx
import json
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import shap
import argparse
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from pytesseract import image_to_string 
from PIL import Image
from sklearn import utils
from sklearn.naive_bayes import GaussianNB

df= pd.read_csv("data.csv")
lendf= len(df.columns)
y= df.iloc[:, -1:]

x= df.drop(df.columns[lendf-1], axis=1)


averages=[]
for i in range(lendf-1):
    averages.append(x.iloc[:, i].mean())

meandf= DataFrame(averages)
meandf.to_csv("averages.csv")

