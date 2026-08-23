"""Logistic Regression on Fashion-MNIST Test Dataset"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

wine = pd.read_csv("ML Classification Assignments/fashion-mnist_test.csv")

print("Dataset Shape:", wine.shape)
print("\nFirst 5 Rows:")
print(wine.head())
print("\nColumn Names:")
print(wine.columns)
# label is the target
y = wine['label']
# All pixel columns are features
feature_cols = [col for col in wine.columns if col.startswith('pixel')]
X = wine[feature_cols]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=16,stratify=y)
print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(random_state=16,max_iter=1000)
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
print("\nPredicted Values:")
print(y_pred[:20])

from sklearn import metrics

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("\nModel Evaluation using Confusion Matrix:")
print(cnf_matrix)

class_names = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(pd.DataFrame(cnf_matrix),annot=True,cmap="YlGnBu",fmt='g',
            xticklabels=class_names,yticklabels=class_names)

ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion Matrix - Fashion MNIST',y=1.1)

plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.show()
from sklearn.metrics import classification_report

target_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal',
    'Shirt','Sneaker','Bag','Ankle boot']

print("\nClassification Report:")
print(classification_report(y_test,y_pred,target_names=target_names))
accuracy = metrics.accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc

# Convert labels into binary form
y_test_bin = label_binarize(y_test,classes=class_names)
# Probability for each class
y_pred_proba = logreg.predict_proba(X_test)

# Plot ROC curve
plt.figure(figsize=(10, 8))
for i in range(10):
    fpr, tpr, _ = roc_curve(y_test_bin[:, i],y_pred_proba[:, i])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr,tpr,label=f'Class {i} AUC = {roc_auc:.2f}')

# Random classifier line
plt.plot([0, 1],[0, 1],'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Fashion MNIST Logistic Regression')
plt.legend(loc='lower right')
plt.show()

input("Wait for me.....")

"""Decision Tree Classifier on Fashion-MNIST Test Dataset"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
fashion = pd.read_csv("ML Classification Assignments/fashion-mnist_test.csv")

print("Dataset Shape:", fashion.shape)
print("\nFirst 5 Rows:")
print(fashion.head())
# Target variable
y = fashion['label']

# Pixel columns are features
feature_cols = [col for col in fashion.columns if col.startswith('pixel')]
X = fashion[feature_cols]
print("\nFeatures:", X.shape)
print("Target:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=1,stratify=y)
clf = DecisionTreeClassifier()

# Train Decision Tree Classifier
clf = clf.fit(X_train, y_train)
# Prediction
y_pred = clf.predict(X_test)

# Accuracy
print("\nDecision Tree Accuracy:")
print(metrics.accuracy_score(y_test, y_pred))
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

from sklearn.metrics import classification_report

target_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt',
                'Sneaker','Bag','Ankle boot']
print("\nClassification Report:")
print(classification_report(y_test,y_pred,target_names=target_names))


from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,rounded=True,special_characters=True,
                feature_names=feature_cols,class_names=['0', '1', '2', '3', '4','5', '6', '7', '8', '9'],
    max_depth=3)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('fashion_mnist_decision_tree.png')
Image(graph.create_png())

clf = DecisionTreeClassifier(criterion="entropy",max_depth=3)
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("\nDecision Tree V2 Accuracy:")
print(metrics.accuracy_score(y_test, y_pred))
dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,rounded=True,special_characters=True,
    feature_names=feature_cols,class_names=['0', '1', '2', '3', '4','5', '6', '7', '8', '9'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

graph.write_png('fashion_mnist_decision_tree_V2.png')
Image(graph.create_png())

input("Wait for me...")

"""SVM Classifier on Fashion-MNIST Test Dataset"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data_link = "C:\\Users\\HP\\Documents\\GitHub\\NexSkill-Ai-Course-Bin\\ML Classification Assignments\\fashion-mnist_test.csv"

fashiondata = pd.read_csv(data_link)

print("First 5 rows:")
print(fashiondata.head())

print("\nUnique Labels:")
print(fashiondata['label'].unique())

print("\nDataset Shape:")
print(fashiondata.shape)

print("\nExploring the Dataset: fashiondata['label'].value_counts()\n",
    fashiondata['label'].value_counts())

print("\nExploring the Dataset: fashiondata['label'].value_counts(normalize=True)\n",
    fashiondata['label'].value_counts(normalize=True))

fashiondata['label'].plot.hist(bins=10,edgecolor='black')
plt.title("Histogram of Fashion-MNIST Labels")
plt.xlabel("Label")
plt.ylabel("Frequency")

plt.show()
plt.close()

print("\nfashiondata.describe().T:\n",fashiondata.describe().T)

for col in fashiondata.columns[1:6]:
    plt.figure()
    plt.title(col)
    gc = fashiondata[col].plot.hist()
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.show()

    plt.close()
# Fashion-MNIST has 784 pixel columns.
# Therefore, only a few columns are used for pairplot.

pairplot_data = fashiondata[['label', 'pixel1', 'pixel2', 'pixel3', 'pixel4']]

sns.pairplot(pairplot_data,hue='label',palette='Set1')
plt.show()

y = fashiondata['label']
# Select all pixel columns as features
col_names = [col for col in fashiondata.columns
if col.startswith('pixel')]
X = fashiondata[col_names]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())

print("\nX Shape:")
print(X.shape)

print("\ny Shape:")
print(y.shape)

from sklearn.model_selection import train_test_split
SEED = 42

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=SEED,stratify=y)
xtrain_samples = X_train.shape[0]
xtest_samples = X_test.shape[0]

print(f"\nThere are {xtrain_samples} samples for training "f"and {xtest_samples} samples for testing.")

from sklearn.svm import SVC
svc = SVC(kernel='linear')
print("\nTraining SVM...")
svc.fit(X_train, y_train)
print("SVM Training Completed.")

y_pred = svc.predict(X_test)
print("\nPredicted Values:")
print(y_pred[:20])

print("\nActual Values:")
print(y_test.iloc[:20].values)
from sklearn.metrics import classification_report, confusion_matrix

cm = confusion_matrix(y_test,y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm,annot=True,fmt='d',cmap='Blues')
plt.title("Confusion Matrix of Linear SVM")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.show()

plt.close()

print("\nClassification Report:")

print(classification_report(y_test,y_pred))