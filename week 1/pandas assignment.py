import pandas as pd

df = pd.read_csv ("FastFoodRestaurants.csv", delimiter= ",", parse_dates=[9], date_format={'date_added': '%d-%m-%Y'})
print(df)

print("df data types:", df.dtypes)
print("df info:", df.info())

print("last three rows:")
print(df.tail(3))

print("first three rows:")
print(df.head(3))


print(df.describe)

print(df.shape)


address = df['address']
print(address)

address, city = df[['address', 'city']]
print(address, city)


second_row = df.loc[2]
print("second_row:", second_row)

third_row = df.loc[2:3]
print("third_row:",third_row )

fourth_row = df.loc[:2:1]
print("fourth_row:", fourth_row)

fifth_row = df.loc[df['address'] == '324 Main St']
print("fifth_row:", fifth_row)

row_6 = df.loc[:2, 'address']
print("row_6:", row_6)

def_index_col = pd.read_csv('FastFoodRestaurants.csv', delimiter = ',', parse_dates=[9], date_format={'date_added': '%d-%m-%Y'}, index_col = 'address' )
print(def_index_col)

print(df.dtypes)
print(df.info)

row_1 = def_index_col.loc['6098 State Highway 37']
print("row_1:", row_1)

row_2 = def_index_col.icol[0]
print(row_1)