"""Logistic Regression on Bank Dataset"""
import pandas as pd
col_names = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome','deposit']
# load dataset
bank_data = pd.read_csv("ML Classification Assignments/Bank.csv", header=1, names=col_names)
#split dataset in features and target variable
feature_cols = ['age', 'balance', 'duration']
X = bank_data[feature_cols] # Features
y = bank_data.deposit # Target variable

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression(random_state=16)
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
target_names = ['without deposit', 'with deposit']
print(classification_report(y_test, y_pred, target_names=target_names))

y_pred_proba = logreg.predict_proba(X_test)
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc

classes = np.unique(y_test)
y_test_bin = label_binarize(y_test, classes=classes)

y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test_bin.ravel(),  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()

input("Wait for me.....")

"""Decision Tree Classifier on Iris Dataset"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics 

col_names = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome', 'deposit']
# load dataset
iris = pd.read_csv("ML Classification Assignments/Bank.csv", header=1, names=col_names)
feature_cols = ['age', 'balance', 'duration']
X = iris[feature_cols] # Features
y = iris.deposit # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = DecisionTreeClassifier().fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1','2'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('iris.png')
Image(graph.create_png())
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
from six import StringIO 
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True, feature_names = feature_cols,class_names=['0','1','2'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('irisV2.png')
Image(graph.create_png())
input("Wait for me...")

"""SVM Classifier on Bank Dataset"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data_link = r"C:\Users\HP\Documents\GitHub\NexSkill-Ai-Course-Bin\ML Classification Assignments\bank.csv"
bankdata = pd.read_csv(data_link)
print(bankdata.dtypes)
print("\nFirst 5 Rows:")
print(bankdata.head())
print("\nShape of Dataset:")
print(bankdata.shape)
print("\nColumn Names:")
print(bankdata.columns)

print("\nExploring the Dataset: bankdata['deposit'].value_counts()\n",bankdata['deposit'].value_counts())
print("\nExploring the Dataset: bankdata['deposit'].value_counts(normalize=True)\n",bankdata['deposit'].value_counts(normalize=True))
bankdata['deposit'].value_counts().plot.hist()
plt.title("Deposit Distribution")
plt.show()
plt.close()

print("\nbankdata.describe().T:\n",bankdata.describe().T)
for col in bankdata.select_dtypes(include=['int64', 'float64']).columns:
    plt.figure(figsize=(6, 4))
    plt.title(col)
    gc = bankdata[col].plot.hist(bins=30)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()
    plt.close()

sns.pairplot(bankdata,hue='deposit',palette='Set1')
plt.show()
y = bankdata['deposit']
X = bankdata[['age','job','marital','education','default','balance','housing','loan','contact',
     'day','month','duration','campaign','pdays','previous','poutcome']]
print("\nTarget Variable:")
print(y.head())
print("\nFeatures:")
print(X.head())
y = y.map({'no': 0,'yes': 1})

print("\nConverted Target:")
print(y.head())

X = pd.get_dummies(X,drop_first=True)
print("\nFeatures After Encoding:")
print(X.head())
print("\nShape After Encoding:")
print(X.shape)
X = X.astype(int)
from sklearn.model_selection import train_test_split

SEED = 42
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.20,random_state=SEED,stratify=y)
xtrain_samples = X_train.shape[0]
xtest_samples = X_test.shape[0]
print(f'\nThere are {xtrain_samples} samples 'f'for training and {xtest_samples} samples 'f'for testing.')
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.svm import SVC
svc = SVC(kernel='linear',probability=True,random_state=SEED)
svc.fit(X_train,y_train)
y_pred = svc.predict(X_test)
y_pred_proba = svc.predict_proba(X_test)[:, 1]

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test,y_pred)
print("\nAccuracy:")
print(accuracy)
from sklearn.metrics import classification_report
print("\nClassification Report:")
print(classification_report(y_test,y_pred))







