"""Linear Regression on AB_NYC_2019 Dataset"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Regression Dataset/AB_NYC_2019.csv')
print(df)
print(df.head())
print(df.info)

print("df.shape:         " , df.shape)
df.plot.scatter(x='longitude', y='latitude', title='Scatter Plot of longitude and latitude');
plt.show()
df_num=  df[["longitude",  "latitude"]]
print(df_num.corr())

print("df.describe():                    " , df.describe())

print(" df['longitude'] :     " , df['longitude'])
print("  df['latitude']   :    ", df['latitude'])
y = df['longitude'].values.reshape(-1, 1)
X = df['latitude'].values.reshape(-1, 1)

print("y:   ", y)
print("x:"   , X) 

print(df['latitude'].values)
print(df['latitude'].values.shape)

print(X.shape) #(48895, 1)
print(X) # [[40.64749][ 40.71283][40.76404]]...]

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
def calc(slope, intercept, latitude):
    return slope*latitude+intercept
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


"""Multiple Regression on AB_NYC_2019 Dataset"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_to_file = 'Regression Dataset/AB_NYC_2019.csv'
df = pd.read_csv(path_to_file)
print("df.head():  \n",df.head())
print("df.shape: \n" , df.shape)
print("df.describe().round(2).T:    \n",df.describe().round(2).T)
import seaborn as sns 
variables = ['longitude','latitude', 'price', 'id', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']
for var in variables:
    plt.figure() 
    sns.regplot(x=var, y='latitude', data=df).set(title=f'Regression plot of {var} and latitude');
    plt.show()
read = input("Wait here: \n")

plt.figure()
df_num=  df[["longitude",  "latitude"]]
print(df_num.corr())
g = sns.heatmap(df_num, annot=True).set(title='Heat map of longitude and latitude Data - Pearson Correlations')
# Display the plot
plt.show()
read = input("Wait for me....")


y = df['longitude']
X = df[['latitude','price', 'id', 'minimum_nights', 'number_of_reviews', 
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

