# """Linear Regression on Test Dataset"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as npA
from sklearn.model_selection import train_test_split

df = pd.read_csv('Regression Dataset/Test.csv')
print(df.head())
print("df.shape:         " , df.shape)

df.plot.scatter(x='Item_Weight', y='Item_Visibility', title='Scatter Plot of Item_Weight and Item_Visibility');
plt.show()
df_num=  df[['Item_Weight', "Item_Visibility"]]
print(df_num.corr())
print("df.describe():                    " , df.describe())

print(" df['Item_Weight'] :     " , df['Item_Weight'])
print("  df['Item_Visibility']   :    ", df['Item_Visibility']   )

y = df[['Item_Visibility']].values.reshape(-1, 1)
X = df[['Item_Weight']].values.reshape(-1, 1)

print("y :  " , y)
print("X :   " , X)

print(df['Item_Weight'].values)
print(df['Item_Weight'].values.shape)
print(X.shape) 
print(X)   

SEED = 42
df = df.dropna() 
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
df = df.dropna() 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
imputer = SimpleImputer(strategy='median')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("Intercept:", regressor.intercept_)
print("Coefficients:", regressor.coef_)

y_pred = regressor.predict(X_test)

results = pd.DataFrame({'Actual': y_test.ravel(), 
                        'Predicted': y_pred.ravel()})
print("\nActual vs Predicted.....\n", results.head(10))
print("\nMSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


def calc(slope, intercept, Item_Weight):
    return slope*Item_Weight+intercept

score = calc(regressor.coef_, regressor.intercept_, 9.5)
print(score) 
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


"""Multiple Regression on Test Dataset"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path_to_file = 'Regression Dataset/Test.csv'
df = pd.read_csv(path_to_file)

print("df.head(): \n", df.head())
print("df.shape: \n", df.shape)
print("df.describe().round(2).T: \n", df.describe().round(2).T)

variables = ['Item_Visibility', 'Item_Weight', 'Outlet_Establishment_Year']

for var in variables:
    plt.figure(figsize=(6,4))
    sns.regplot(x=var, y='Item_Visibility', data=df)
    plt.title(f'Regression plot of {var} and Item_Visibility') 
    plt.show()

input("Wait here: \n")
numeric_df = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(10,8))
correlations = numeric_df.corr()
print("correlations...\n", correlations)

sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap - Pearson Correlations')
plt.show()

input("Wait for me....")
y = df['Item_Visibility']
X = df[['Item_Weight', 'Item_MRP', 'Outlet_Establishment_Year']]

SEED = 200
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=42)

print("X.shape # (48, 4):     \n", X.shape )   
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score

imputer = SimpleImputer(strategy='median')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# 2. Model Train
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print("Intercept:", regressor.intercept_)
print("Coefficients: ", regressor.coef_)
feature_names = X.columns
coefficients_df = pd.DataFrame(data = regressor.coef_,
                               index = feature_names,
                               columns = ['Coefficient value'])
print(coefficients_df)

# 4. Prediction
y_pred = regressor.predict(X_test)

# 5. Actual vs Predicted
results = pd.DataFrame({'Actual': y_test.reset_index(drop=True), 
                        'Predicted': y_pred})
print("\nActual vs Predicted.....\n" , results.head(10))
# 6. Model Performance check
print("\nMSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
