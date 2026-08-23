"""Logistic Regression on Iris Dataset"""
import pandas as pd
col_names = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
# load dataset
iris = pd.read_csv("ML Classification Assignments/Iris.csv", header=1, names=col_names)
#split dataset in features and target variable
feature_cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
X = iris[feature_cols] # Features
y = iris.Species # Target variable

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

class_names=[0,1,2] # name  of classes
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
target_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
print(classification_report(y_test, y_pred, target_names=target_names))

y_pred_proba = logreg.predict_proba(X_test)
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc

classes = np.unique(y_test)
y_test_bin = label_binarize(y_test, classes=classes)

plt.figure(figsize=(8,6))
for i in range(len(classes)):
    fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_pred_proba[:, i])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f'{target_names[i]} AUC = {roc_auc:.2f}')

plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc=4)
# plt.show()
input("Wait for me.....")



"""Decision Tree  on Iris Dataset"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics 

col_names = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
# load dataset
iris = pd.read_csv("ML Classification Assignments/Iris.csv", header=1, names=col_names)
feature_cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
X = iris[feature_cols] # Features"""Decision Tree Classifier on Iris Dataset"""
y = iris.Species # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
# clf = DecisionTreeClassifier()

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

"""SVM Classifier on Iris Dataset"""
import pandas as pd
import matplotlib.pyplot as plt

data_link = "C:/Users/HP/Documents/GitHub/NexSkill-Ai-Course-Bin/ML Classification Assignments/Iris.csv"
col_names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

bankdata = pd.read_csv(data_link)
bankdata.head()
print(bankdata ['SepalWidthCm'].unique())
print(bankdata.shape)
print ( " Exploring the Dataset:  bankdata['Species'].value_counts()) \n " , bankdata['Species'].value_counts())
print ( " Exploring the Dataset:  bankdata['Species'].value_counts()) \n " , bankdata['Species'].value_counts(normalize=True) )
bankdata['SepalWidthCm'].plot.hist();
plt.show()
plt.close()
print("bankdata.describe().T   :    \n" , bankdata.describe().T )
import matplotlib.pyplot as plt

for col in bankdata.columns[:-1]:
    plt.title(col)
    gc= bankdata[col].plot.hist() #plotting the histogram with Pandas
    gc.figure.show()
    #plt.show();
    
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(bankdata, hue='SepalWidthCm', palette='Set1');
plt.show()
y = bankdata['Species']
X = bankdata[col_names]
from sklearn.model_selection import train_test_split

SEED = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = SEED)
xtrain_samples = X_train.shape[0]
xtest_samples = X_test.shape[0]

print(f'There are {xtrain_samples} samples for training and {xtest_samples} samples for testing.')
from sklearn.svm import SVC
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)
from sklearn.metrics import classification_report, confusion_matrix
y_pred = svc.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
gg=sns.heatmap(cm, annot=True, fmt='d').set_title('Confusion matrix of linear SVM') # fmt='d' formats the numbers as digits, which means integers
gg.figure.show() 

#plt.close()

print(classification_report(y_test,y_pred))