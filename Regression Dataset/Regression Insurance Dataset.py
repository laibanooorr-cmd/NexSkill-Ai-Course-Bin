"""Linear Regression on Insurance Dataset"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Regression Dataset/insurance.csv')
print(df)
print(df.head())
print(df.info)

print("df.shape:         " , df.shape)
df.plot.scatter(x='age', y='charges', title='Scatter Plot of cahrges and scores percentages');
plt.show()
df_num=  df[["age",  "charges"]]
print(df_num.corr())

print("df.describe():                    " , df.describe())

print(" df['age'] :     " , df['age'])
print("  df['charges']   :    ", df['charges'])
y = df['age'].values.reshape(-1, 1)
X = df['charges'].values.reshape(-1, 1)

print("y:   ", y)
print("x:"   , X) 

print(df['charges'].values)
print(df['charges'].values.shape)

print(X.shape) #(1338, 1)
print(X) # [[16884.924 ][ 1725.5523][ 4449.462 ]...]

SEED = 42

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)
print(X_train)
print(y_train)

#Training a Linear Regression Model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)

#Making Predictions
def calc(slope, intercept, charges):
    return slope*charges+intercept
score = calc(regressor.coef_, regressor.intercept_, 9.5)
print(score) 

# Passing 9.5 in double brackets to have a 2 dimensional array
score = regressor.predict([[9.5]])
print(score)
y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)

from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')


"""Multiple Regression  on Insurance Dataset"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_to_file = 'Regression Dataset/insurance.csv'
df = pd.read_csv(path_to_file)
print("df.head():  \n",df.head())
print("df.shape: \n" , df.shape)
print("df.describe().round(2).T:    \n",df.describe().round(2).T)
import seaborn as sns 
variables = ['age','bmi', 'charges', 'children']
for var in variables:
    plt.figure() 
    sns.regplot(x=var, y='charges', data=df).set(title=f'Regression plot of {var} and charges');
    plt.show()
read = input("Wait here: \n")

plt.figure()
df_num=  df[["age",  "charges"]]
print(df_num.corr())
g = sns.heatmap(df_num, annot=True).set(title='Heat map of charges Data - Pearson Correlations')
# Display the plot
plt.show()
read = input("Wait for me....")


y = df['charges']
X = df[['age',
       ]]

SEED = 200
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=SEED)

print("X.shape # (50, 2):     \n", X.shape )   

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)
print("regressor.intercept_......\n", regressor.intercept_)
print("regressor.coef_ " , regressor.coef_)

y_pred = regressor.predict(X_test)

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("Actual vs Predicted.....\n" , results)

from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')

actual_minus_predicted = sum((y_test - y_pred)**2)
actual_minus_actual_mean = sum((y_test - y_test.mean())**2)
r2 = 1 - actual_minus_predicted/actual_minus_actual_mean
print('R²:', r2)

print(" R2 also comes implemented by default into the score method of Scikit-Learn's linear regressor class...\n", regressor.score(X_test, y_test))

"""Lodistic Regression Operation"""
import pandas as pd

col_num = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
df  = pd.read_csv('Regression Dataset/insurance.csv', header=1, names=col_num)
print(df)

features_col = ['age','children', 'bmi', 'charges']
X = df[features_col]
y = df['smoker'].map({'yes':1, 'no':0})
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state= 16)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(random_state=16)

logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
from sklearn import metrics

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(" Model Evaluation using Confusion Matrix : " , cnf_matrix)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
class_names = [0, 1] # class names
fig , ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.yticks(tick_marks, class_names)
plt.xticks(tick_marks, class_names)

sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" , fmt= 'g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
plt.Text(0.5,257.44,'Predicted label');

from sklearn.metrics import classification_report
target_names = ['without smoker', 'with smoker']
print(classification_report(y_test, y_pred, target_names=target_names))

y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()

input("Wait for me.....")
