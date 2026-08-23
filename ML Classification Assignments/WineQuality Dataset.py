"""Logistic Regression on Iris Dataset"""
import pandas as pd
col_names = ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality']
# load dataset
wine = pd.read_csv("ML Classification Assignments/winequality-red.csv")
#split dataset in features and target variable
feature_cols = ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides']
X = wine[feature_cols] # Features
y = wine['quality']# Target variable
y = (y >= 7).astype(int)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression(random_state=16, max_iter=1000)
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
# import the metrics class
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(" Model Evaluation using Confusion Matrix : " , cnf_matrix)
# import required modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
plt.Text(0.5,257.44,'Predicted label');
from sklearn.metrics import classification_report
target_names = ['with quality', 'without quality']
print(classification_report(y_test, y_pred, target_names=target_names))

# y_pred_proba = logreg.predict_proba(X_test)
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

y_test_bin = y_test
y_pred_proba = logreg.predict_proba(X_test)[:, 1]
fpr, tpr,_= roc_curve(y_test_bin, y_pred_proba)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label= f'Logistic Regression AUC = {roc_auc: .2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Wine Quality')
plt.legend(loc = 4)
plt.show()
input("Wait for me.....")


"""Decision Tree Classifier on Iris Dataset"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load dataset
wine = pd.read_csv("ML Classification Assignments/winequality-red.csv")

# Display dataset information
print("Dataset Shape:", wine.shape)
print("\nColumns:")
print(wine.columns)

print("\nFirst 5 Rows:")
print(wine.head())

# Features
feature_cols = ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide',
    'total sulfur dioxide','density','pH','sulphates','alcohol']

X = wine[feature_cols]       # Features
y = wine['quality']          # Target variable

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=1)
# Train Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=1)
clf = clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

# Accuracy
print("\nDecision Tree Accuracy:")
print(metrics.accuracy_score(y_test, y_pred))
from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,rounded=True,special_characters=True,
                feature_names=feature_cols,class_names=[str(x) for x in clf.classes_])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('winequality.png')
Image(graph.create_png())\

clf = DecisionTreeClassifier(criterion="entropy",max_depth=3,random_state=1)
clf = clf.fit(X_train, y_train)
# Predict
y_pred = clf.predict(X_test)

# Accuracy
print("\nDecision Tree Accuracy with Entropy:")
print(metrics.accuracy_score(y_test, y_pred))


dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,rounded=True,special_characters=True,
                feature_names=feature_cols,class_names=[str(x) for x in clf.classes_])

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('winequalityV2.png')
Image(graph.create_png())
input("Wait for me...")
"""SVM Classifier on Wine Quality Dataset"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_link = "C:/Users/HP/Documents/GitHub/NexSkill-Ai-Course-Bin/ML Classification Assignments/winequality-red.csv"

wine = pd.read_csv(data_link)
print("\nFirst 5 Rows:")
print(wine.head())

print("\nColumn Names:")
print(wine.columns.tolist())

print("\nUnique Quality Values:")
print(wine['quality'].unique())

print("\nDataset Shape:")
print(wine.shape)

print("\nQuality Value Counts:")
print(wine['quality'].value_counts())

print("\nQuality Value Counts:")
print(wine['quality'].value_counts(normalize=True))

wine['quality'].plot.hist()

plt.title("Wine Quality Distribution")
plt.xlabel("Quality")
plt.ylabel("Frequency")

plt.show()
plt.close()

print("\nDataset Description:")
print(wine.describe().T)

for col in wine.columns[:-1]:
    plt.figure()
    plt.title(col)
    wine[col].plot.hist()
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

    plt.close()

sns.pairplot(wine,hue='quality',palette='Set1')
plt.show()

col_names = ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide',
    'total sulfur dioxide','density','pH','sulphates','alcohol']

print("\nChecking Feature Columns:")
for col in col_names:
    if col in wine.columns:
        print(col, "found")
    else:
        print(col, " NOT FOUND")

X = wine[col_names]
y = wine['quality']
print("\nX Shape:")
print(X.shape)
print("\nY Shape:")
print(y.shape)

from sklearn.model_selection import train_test_split
SEED = 42
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=SEED,stratify=y)
xtrain_samples = X_train.shape[0]
xtest_samples = X_test.shape[0]

print(f"\nThere are {xtrain_samples} samples for training "f"and {xtest_samples} samples for testing.")

from sklearn.svm import SVC
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm,annot=True,fmt='d',cmap='Blues',xticklabels=sorted(y.unique()),yticklabels=sorted(y.unique()))
plt.title("Confusion Matrix of Linear SVM")
plt.xlabel("Predicted Quality")
plt.ylabel("Actual Quality")

plt.show()

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("\nSVM Accuracy:")
print(accuracy)

input("\nWait for me...")