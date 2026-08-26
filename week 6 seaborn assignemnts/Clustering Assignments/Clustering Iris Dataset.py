"""Gradient Boosting Vs Ada Boosting Dataset"""
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor

from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor

import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("week 6 seaborn assignemnts/Clustering Assignments/Iris.csv")

print("First 5 rows:")
print(iris.head())

print("\nDataset Shape:")
print(iris.shape)

print("\nColumn Names:")
print(iris.columns)

print("\nDataset Information:")
print(iris.info())

# Select Features and Target
# We will predict PetalLengthCm

feature_cols = ['SepalLengthCm','SepalWidthCm','PetalWidthCm']
target_col = 'PetalLengthCm'

X = iris[feature_cols]
y = iris[target_col]
# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(X,y,
    test_size=0.2,
    random_state=42)
# 1. Gradient Boosting Regressor

gbr = GradientBoostingRegressor(random_state=42)

gbr.fit(X_train, y_train)
y_pred1 = gbr.predict(X_test)
print("Gradient Boosting - R2: ",r2_score(y_test, y_pred1))
# 2. XGBoost Regressor

xgr = XGBRegressor(random_state=42,n_estimators=100)

xgr.fit(X_train, y_train)
y_pred2 = xgr.predict(X_test)
print("XGBoost - R2: ",r2_score(y_test, y_pred2))
# 3. AdaBoost Regressor

adr = AdaBoostRegressor(random_state=42)

adr.fit(X_train, y_train)
y_pred3 = adr.predict(X_test)
print("AdaBoost - R2: ",r2_score(y_test, y_pred3))

# 4. CatBoost Regressor

cbr = CatBoostRegressor(iterations=100,depth=5,learning_rate=0.01,loss_function='RMSE',
    verbose=0,random_seed=42)

cbr.fit(X_train, y_train)
y_pred4 = cbr.predict(X_test)
print("CatBoost - R2: ",r2_score(y_test, y_pred4))

# 5. LightGBM Regressor

lgr = LGBMRegressor(random_state=42,n_estimators=100)

lgr.fit(X_train, y_train)
y_pred5 = lgr.predict(X_test)
print("LightGBM - R2: ", r2_score(y_test, y_pred5))

# Comparison of R2 Scores
print("R2 Score Comparison")

print("Gradient Boosting:",r2_score(y_test, y_pred1))
print("XGBoost:",r2_score(y_test, y_pred2))
print("AdaBoost:",r2_score(y_test, y_pred3))
print("CatBoost:",r2_score(y_test, y_pred4))
print("LightGBM:",r2_score(y_test, y_pred5))

# Plot Actual vs Predicted Values

fig, ax = plt.subplots(figsize=(11, 5))
sns.lineplot(x=range(len(y_test)),y=y_test.values,label='Actual')
sns.lineplot(x=range(len(y_pred1)),y=y_pred1,label='GradientBoosting')
sns.lineplot(x=range(len(y_pred2)),y=y_pred2,label='XGBoost')
sns.lineplot(x=range(len(y_pred3)),y=y_pred3,label='AdaBoost')
sns.lineplot(x=range(len(y_pred4)),y=y_pred4,label='CatBoost')
sns.lineplot(x=range(len(y_pred5)),y=y_pred5,label='LightGBM')
ax.set_xlabel('Test Sample')
ax.set_ylabel('PetalLengthCm')
plt.title('Actual vs Predicted Petal Length - Ensemble Regression')
plt.legend()
plt.tight_layout()
plt.show()


wait = input("wait for....")

"""RandomForestClassifierViaSciKitLearn"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings

warnings.filterwarnings('ignore')

url = "C:\\Users\\HP\\Documents\\GitHub\\NexSkill-Ai-Course-Bin\\week 6 seaborn assignemnts\\Clustering Assignments\\Iris.csv"
iris_data = pd.read_csv(url)
print(iris_data.head())

X = iris_data[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]

y = iris_data['Species']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
rf_classifier = RandomForestClassifier(n_estimators=100,random_state=42)
rf_classifier.fit(X_train, y_train)
# Prediction

y_pred = rf_classifier.predict(X_test)
# Accuracy

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2f}")

classification_rep = classification_report(y_test,y_pred)
print("\nClassification Report:\n")
print(classification_rep)

sample = X_test.iloc[0:1]
prediction = rf_classifier.predict(sample)
sample_dict = sample.iloc[0].to_dict()
print("\nSample Flower:")
print(sample_dict)

print(f"\nPredicted Species: {prediction[0]}")

"""RandomForestRegressorViaSciKitLearn"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

iris_data = pd.read_csv("week 6 seaborn assignemnts/Clustering Assignments/Iris.csv")
# Select Features and Target

X = iris_data[['SepalLengthCm','SepalWidthCm','PetalWidthCm']]
y = iris_data['PetalLengthCm']
# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100,
random_state=42)
rf_regressor.fit(X_train, y_train)
y_pred = rf_regressor.predict(X_test)
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

# Predict Single Data
single_data = X_test.iloc[0].values.reshape(1, -1)
predicted_value = rf_regressor.predict(single_data)
# Results
print(f"Predicted Value: {predicted_value[0]:.2f}")
print(f"Actual Value: {y_test.iloc[0]:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")

"""K-means-Clustering"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


iris = pd.read_csv("week 6 seaborn assignemnts/Clustering Assignments/Iris.csv")
X = iris[['SepalLengthCm','SepalWidthCm']
].values
k = 3
clusters = {}
np.random.seed(23)
for idx in range(k):
    center = 2 * (2 * np.random.random((X.shape[1],)) - 1)
    points = []
    cluster = {'center': center,'points': []}
    clusters[idx] = cluster
print(clusters)
plt.figure(figsize=(8, 6))
plt.grid(True)
plt.scatter(X[:, 0],X[:, 1])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Dataset')
plt.show()

plt.scatter(X[:, 0],X[:, 1])
plt.grid(True)
for i in clusters:
    center = clusters[i]['center']
    plt.scatter(center[0],center[1],marker='*',c='red')

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Initial Cluster Centers')
plt.show()
def distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))
# Assign Points to Clusters

def assign_clusters(X, clusters):
    for idx in range(X.shape[0]):
        dist = []
        curr_x = X[idx]

        for i in range(k):
            dis = distance(curr_x,clusters[i]['center'])
            dist.append(dis)
        curr_cluster = np.argmin(dist)
        clusters[curr_cluster]['points'].append(curr_x)
    return clusters
# Update Cluster Centers
def update_clusters(X, clusters):
    for i in range(k):
        points = np.array(clusters[i]['points'])
        if points.shape[0] > 0:
            new_center = points.mean(axis=0)
            clusters[i]['center'] = new_center
            clusters[i]['points'] = []
    return clusters
# Predict Cluster
def pred_cluster(X, clusters):
    pred = []
    for i in range(X.shape[0]):
        dist = []
        for j in range(k):
            dist.append(distance(
                    X[i],clusters[j]['center']))
        pred.append(np.argmin(dist))
    return pred
# Assign Clusters

clusters = assign_clusters(X,clusters)
clusters = update_clusters(X,clusters)
pred = pred_cluster(X,clusters)
plt.figure(figsize=(8, 6))
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=pred)

for i in clusters:
    center = clusters[i]['center']
    plt.scatter(center[0],center[1],marker='^',c='red',s=100)
plt.grid(True)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-Means Clustering on Iris Dataset')
plt.show()

"""K-MeansClustering-ViaSKLearn-Example1"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = pd.read_csv("week 6 seaborn assignemnts/Clustering Assignments/Iris.csv")
print(iris.head())
X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
X = X.values
plt.figure(figsize=(7.5, 3.5))

plt.scatter(X[:, 0],X[:, 1],s=20)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Dataset')
plt.show()
kmeans = KMeans(n_clusters=3,max_iter=100,random_state=42)
kmeans.fit(X)

plt.figure(figsize=(7.5, 3.5))
plt.scatter(X[:, 0],X[:, 1],c=kmeans.labels_,s=20,cmap='summer')
plt.scatter(kmeans.cluster_centers_[:, 0],kmeans.cluster_centers_[:, 1],marker='x',c='r',s=50,alpha=0.9)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-Means Clustering on Iris Dataset')
plt.show()

print("\nCluster Centers:")
print(kmeans.cluster_centers_)

"""K-MeansClustering-ViaSKLearn-Example2"""

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

iris = pd.read_csv("week 6 seaborn assignemnts/Clustering Assignments/Iris.csv")
X = iris[['SepalLengthCm','SepalWidthCm']].values
plt.figure(figsize=(7.5, 3.5))
plt.scatter(X[:, 0],X[:, 1],s=20)

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Dataset')
plt.show()

kmeans = KMeans(n_clusters=3,random_state=42)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
plt.figure(figsize=(7.5, 3.5))
plt.scatter(X[:, 0],X[:, 1],c=y_kmeans,s=20,cmap='summer')


centers = kmeans.cluster_centers_
color = np.array(['blue','hotpink','green'])

plt.scatter(centers[:, 0],centers[:, 1],c=color,s=100,alpha=0.9,marker='x')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-Means Clustering on Iris Dataset')
plt.show()
print("Cluster Centers:")
print(centers)

wait = input("Hello")

"""K-MeansClustering-ViaSKLearn-Example3"""

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

# Load Iris dataset from CSV

iris = pd.read_csv("week 6 seaborn assignemnts/Clustering Assignments/Iris.csv")
print("iris.data.shape: ", iris.shape)

# Select the features

X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
print("\nX.shape: ", X.shape)
print("\nFeature data:")
print(X.head())
# Convert Species into numerical labels

iris['Species'] = iris['Species'].map({'Iris-setosa': 0,'Iris-versicolor': 1,'Iris-virginica': 2})
y = iris['Species']
# K-Means Clustering

kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(X)

print("\nkmeans.cluster_centers_.shape: ",kmeans.cluster_centers_.shape)
print("\nK-Means Cluster Centers:")
print(kmeans.cluster_centers_)
# Visualize the clusters

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(X['SepalLengthCm'],X['SepalWidthCm'],c=clusters,cmap=plt.cm.binary)
ax.scatter(kmeans.cluster_centers_[:, 0],kmeans.cluster_centers_[:, 1],marker='X',s=200,color='red')

ax.set(xlabel='Sepal Length',ylabel='Sepal Width',title='K-Means Clustering - Iris Dataset')
plt.show()
wait = input("Wait here: ")
# Match learned cluster labels with true labels
from scipy.stats import mode
labels = np.zeros_like(clusters)
for i in range(3):
    mask = (clusters == i)
    labels[mask] = mode(y[mask],keepdims=True)[0]
# Accuracy
from sklearn.metrics import accuracy_score
print("accuracy_score:",accuracy_score(y, labels))


"""HierarchicalAgglomerativeClustering"""
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
# Load Iris CSV file

iris = pd.read_csv("week 6 seaborn assignemnts/Clustering Assignments/Iris.csv")
# Select numerical features
X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].values
print("X.shape:", X.shape)
# Apply Agglomerative Clustering

clustering = AgglomerativeClustering(n_clusters=3).fit(X)
print("Cluster labels:")
print(clustering.labels_)

"""HierarchicalDivisiveClustering-DistanceMatrixComparision"""
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("week 6 seaborn assignemnts/Clustering Assignments/Iris.csv")
# Select Iris features
X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].values
# Ward Distance
Z = linkage(X, 'ward')
# Plotting the dendrogram
dendrogram(Z)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data point')
plt.ylabel('Distance')
plt.show()

"""DBSCAN-ClusteringViaSKLearn"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import pandas as pd
from sklearn.preprocessing import StandardScaler

iris = pd.read_csv("week 6 seaborn assignemnts/Clustering Assignments/Iris.csv")
# Select features
X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].values
# Convert Species into numerical values
y_true = iris['Species'].map({'Iris-setosa': 0,'Iris-versicolor': 1,'Iris-virginica': 2}).values
print("Dataset shape:", X.shape)

X = StandardScaler().fit_transform(X)
db = DBSCAN(eps=0.5, min_samples=5).fit(X)
core_samples_mask = np.zeros_like(db.labels_,dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print("Number of clusters:", n_clusters_)
# Plot clusters
unique_labels = set(labels)
colors = ['y', 'b', 'g', 'r']
print(colors)
for k, col in zip(unique_labels, colors):
    if k == -1:
        col = 'k'
    class_member_mask = (labels == k)
    # Core points
    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0],xy[:, 1],'o',markerfacecolor=col,markeredgecolor='k',markersize=6)
    # Non-core points
    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0],xy[:, 1],'o',markerfacecolor=col,markeredgecolor='k',markersize=6)
plt.title('Number of clusters: %d' % n_clusters_)
plt.xlabel('Sepal Length (Standardized)')
plt.ylabel('Sepal Width (Standardized)')
plt.show()
# Silhouette Score
if n_clusters_ > 1:
    sc = metrics.silhouette_score(X,labels)
    print("Silhouette Coefficient: %0.2f"% sc)
# Adjusted Rand Index
ari = metrics.adjusted_rand_score(y_true,labels)
print("Adjusted Rand Index: %0.2f"% ari)