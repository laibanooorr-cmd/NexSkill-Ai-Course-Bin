"""Logistic Regression on Fashion-MNIST Train Dataset"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Fashion-MNIST Train Dataset
wine = pd.read_csv("ML Classification Assignments/fashion-mnist_train.csv")

# Dataset Information
print("Dataset Shape:", wine.shape)
print("\nFirst 5 Rows:")
print(wine.head())

print("\nColumn Names:")
print(wine.columns)

print("\nDataset Information:")
print(wine.info())

# label is the target
y = wine['label']
# All pixel columns are features
feature_cols = [col for col in wine.columns if col.startswith('pixel')]

X = wine[feature_cols]
print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

print("\nTarget Classes:")
print(y.unique())

print("\nClass Distribution:")
print(y.value_counts().sort_index())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=16,stratify=y)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(random_state=16,max_iter=1000)
print("\nTraining Logistic Regression Model...")
logreg.fit(X_train, y_train)
print("Model Training Completed!")

y_pred = logreg.predict(X_test)

print("\nPredicted Values:")
print(y_pred[:20])
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("\nModel Evaluation using Confusion Matrix:")
print(cnf_matrix)
class_names = [0, 1, 2, 3, 4,5, 6, 7, 8, 9]

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(pd.DataFrame(cnf_matrix),annot=True,cmap="YlGnBu",fmt='g',
    xticklabels=class_names,yticklabels=class_names)

ax.xaxis.set_label_position("top")
plt.tight_layout()

plt.title('Confusion Matrix - Fashion MNIST Logistic Regression',y=1.1)
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')

plt.show()
from sklearn.metrics import classification_report

target_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
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


"""Decision Tree and SVM Classifier on Fashion-MNIST Dataset"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
data_link = "C:/Users/HP/Documents/GitHub/NexSkill-Ai-Course-Bin/ML Classification Assignments/fashion-mnist_train.csv"
fashion = pd.read_csv(data_link)
print("Dataset Shape:", fashion.shape)

print("\nFirst 5 Rows:")
print(fashion.head())

print("\nColumn Names:")
print(fashion.columns)
print("\nLabel Unique Values:")
print(fashion['label'].unique())

print("\nLabel Value Counts:")
print(fashion['label'].value_counts())

print("\nLabel Value Counts Normalized:")
print(fashion['label'].value_counts(normalize=True))

print("\nDataset Description:")
print(fashion.describe().T)

plt.figure(figsize=(10, 6))
fashion['label'].value_counts().sort_index().plot.hist(bins=10)
plt.title("Fashion-MNIST Label Distribution")
plt.xlabel("Label")
plt.ylabel("Frequency")
plt.show()

plt.close()

# Plot histogram of some pixel columns
pixel_columns = ['pixel1','pixel2','pixel3','pixel4','pixel5']
fashion[pixel_columns].hist(figsize=(10, 8),bins=20)
plt.suptitle("Pixel Value Histograms")
plt.show()

plt.close()
plt.figure(figsize=(10, 6))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    image = fashion.iloc[i][[col for col in fashion.columns if col.startswith('pixel')]].values
    image = image.reshape(28, 28)
    plt.imshow(image, cmap='gray')
    plt.title("Label: " + str(fashion.iloc[i]['label']))
    plt.axis('off')
plt.tight_layout()
plt.show()
# Target variable
y = fashion['label']
# All pixel columns are features
feature_cols = [col for col in fashion.columns
    if col.startswith('pixel')]
X = fashion[feature_cols]
print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

SEED = 42

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=SEED,stratify=y)
xtrain_samples = X_train.shape[0]
xtest_samples = X_test.shape[0]
print(f'\nThere are {xtrain_samples} samples for training 'f'and {xtest_samples} samples for testing.')

# Train Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=SEED)
clf = clf.fit(X_train,y_train)

# Prediction
y_pred = clf.predict(X_test)
print("\nDecision Tree Accuracy:",metrics.accuracy_score(y_test, y_pred))
from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus
dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,rounded=True,special_characters=True,
    feature_names=feature_cols,class_names=[
        '0', '1', '2', '3', '4',
        '5', '6', '7', '8', '9'],max_depth=3)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('fashion_mnist_tree.png')
Image(graph.create_png())
clf = DecisionTreeClassifier(criterion="entropy",max_depth=3,random_state=SEED)
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("\nDecision Tree Entropy Accuracy:",metrics.accuracy_score(y_test, y_pred))


from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,rounded=True,special_characters=True,feature_names=feature_cols,
    class_names=['0', '1', '2', '3', '4','5', '6', '7', '8', '9'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('fashion_mnist_treeV2.png')
Image(graph.create_png())

cm = metrics.confusion_matrix(y_test,y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm,annot=True,fmt='d',cmap='Blues')

plt.title('Confusion Matrix of Decision Tree')
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')

plt.show()

target_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
print("\nDecision Tree Classification Report:")

print(metrics.classification_report(y_test,y_pred,target_names=target_names))
from sklearn.svm import SVC
print("\nTraining SVM...")
svc = SVC(kernel='linear')
svc.fit(X_train,y_train)

y_pred_svm = svc.predict(X_test)
print("\nSVM Accuracy:",metrics.accuracy_score(y_test,y_pred_svm))

cm_svm = metrics.confusion_matrix(y_test,y_pred_svm)
plt.figure(figsize=(10, 8))
sns.heatmap(cm_svm,annot=True,fmt='d',cmap='Blues')
plt.title('Confusion Matrix of Linear SVM')
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')

plt.show()
print("\nSVM Classification Report:")

print(metrics.classification_report(y_test,y_pred_svm,target_names=target_names))

input("Wait for me...")