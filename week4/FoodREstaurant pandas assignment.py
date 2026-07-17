import pandas as pd

df = pd.read_csv('FastFoodRestaurants.csv',delimiter=",",parse_dates=[9], date_format={'date_added': '%d-%m-%Y'})

print(df)

print("df - data types" , df.dtypes)
print("df.info():   " , df.info() )


# display the last three rows
print('Last three Rows:')
print(df.tail(2))

# display the first three rows
print('First Three Rows:')
print(df.head(2))
print()


#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). 
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape) # output  (10000, 10)


# access the Name column
Price = df['longitude']
print("access the Name column: df : ", Price)

# access multiple columns
price_status = df[['longitude','latitude']]
print("access multiple columns: df : ", price_status)


#Selecting a single row using .loc
first_row = df.loc[1]
print("Selecting a single row using .loc:")
print(first_row)

#Selecting multiple rows using .loc
first_row2 = df.loc[[0, 2]]
print("Selecting multiple rows using .loc:")
print(first_row2)


#Selecting a slice of rows using .loc
first_row3 = df.loc[2:6]
print("Selecting a slice of rows using .loc")
print(first_row3)

#Conditional selection of rows using .loc
first_row4 = df.loc[df['latitude'] ==  39.53255]
print("Conditional selection of rows using .loc")
print(first_row4)


#Selecting a single column using .loc
first_row5 = df.loc[:1,'latitude']
print("Selecting a single column using .loc")
print(first_row5)

#Selecting multiple columns using .loc
first_row6 = df.loc[:,['longitude','latitude']]
print("Selecting multiple columns using .loc")
print(first_row6)


#Selecting a slice of columns using .loc
first_row7 = df.loc[:1,'address':'city']
print("Selecting a slice of columns using .loc")
print(first_row7)

#Combined row and column selection using .loc
first_row8 = df.loc[df['city'] == 'Washington Court House','address':'city']
print("#Combined row and column selection using .loc")
print(first_row8)
# Case 1 : using .loc - default case - ends here

print("# Case 2 : using .loc with index_col - starts here")


# index_col='latitude'
df_index_col = pd.read_csv('FastFoodRestaurants.csv',delimiter=",",parse_dates=[9], date_format={'date_added': '%d-%m-%Y'} , index_col='latitude')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())


#Second cycle - with index_col as latitude
#Selecting a single row using .loc
first_row = df_index_col.loc[44.9213]
print("Selecting a single row using .loc")
print(first_row)

##Selecting multiple rows using .loc
first_row2 = df_index_col.loc[[44.9213, 44.95008]]
print("#Selecting multiple rows using .loc")
print(first_row2)


#Selecting a slice of rows using .iloc
first_row3 = df_index_col.loc[44.9213:44.95008]
print("Selecting a slice of rows using .loc")
print(first_row3)


# #Conditional selection of rows using .loc
first_row4 = df_index_col.loc[df_index_col['city'] == 'Massena']
print("Conditional selection of rows using .loc")
print(first_row4)


# #Selecting a single column using .iloc
first_row5 = df_index_col.loc[:44.950269 ]
print("Selecting a single column using .iloc")
print(first_row5)

# #Selecting multiple columns using .loc
first_row6 = df_index_col.loc[:44.950269,['address', 'city']]
print("Selecting multiple columns using .loc")
print(first_row6)


# #Selecting a slice of columns using .loc
first_row7 = df_index_col.loc[:44.950269,'address':'city']
print("Selecting a slice of columns using .loc")
print(first_row7)

# #Combined row and column selection using .loc
first_row8 = df_index_col.loc[df_index_col['city'] == 'Washington Court House','address':'city']
print("#Combined row and column selection using .loc")
print(first_row8)

# # Case 2 : using .loc with index_col  -  ends here
print("Case 3 : Using .iloc - starts here")
# # Case 3 : Using .iloc - starts here


# #Selecting a single row using .iloc
first_row = df_index_col.iloc[3]
print("Selecting a single row using .iloc")
print(first_row)

# #Selecting multiple rows using .iloc
first_row2 = df_index_col.iloc[[1, 4,5]]
print("Selecting multiple rows using .iloc")
print(first_row2)


# #Selecting a slice of rows using .iloc
first_row3 = df_index_col.iloc[2:4]
print("#Selecting a slice of rows using .iloc")
print(first_row3)

# #Selecting a single column using .iloc
first_row5 = df_index_col.iloc[:,3]
print("#Selecting a single column using .iloc")
print(first_row5)


# #Selecting multiple columns using .iloc
first_row6 = df_index_col.iloc[:,[1,4]]
print("#Selecting multiple columns using .iloc")
print(first_row6)


# #Selecting a slice of columns using .iloc
first_row7 = df_index_col.iloc[:,1:4]
print("#Selecting a slice of columns using .iloc")
print(first_row7)


# #Combined row and column selection using .iloc
first_row8 = df_index_col.iloc[[1, 2,5],1:4]
print("#Combined row and column selection using .iloc")
print(first_row8)


# # Case 3 : Using .iloc - ends here
print("Next Run")


# #Add a New Row to a Pandas DataFrame
df.loc[len(df.index)] = ['address','city','country','keys','latitude','longitude','name','postalCode','province','websites']
print("Modified DataFrame - add a new row:")
print(df)


#Remove Rows/Columns from a Pandas DataFrame

# delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 4], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)


# delete age column
df.drop('latitude', axis=1, inplace=True)
# delete marital status column
df.drop(columns='city', inplace=False)
# delete height and profession columns
df.drop(['country', 'city'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete page_url ,property_type , location , city , column :")
print(df)


#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {'counrty': 'country_changed'}, inplace=True)
# rename columns 'Age' and 'City'
df.rename(mapper= {'key': 'key_Changed', 'address':'address_Changed'}, axis=1, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame  - Rename Labels :")
print(df)


# rename column one index label
df.rename(index={0: 8}, inplace=True)
# rename columns multiple index labels
df.rename(mapper={1: 10, 2: 80}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)


# select the rows where province is "OH" or keys column contains "oh"
selected_rows = df.query('province == "OH" or keys.str.contains("oh")', engine = 'python')

print(selected_rows.to_string())
print(len(selected_rows))




# sort DataFrame by  prev_sold_date in ascending order
sorted_df = df.sort_values(by='websites')
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns
df1 = df.sort_values(by=['websites', 'name'])

print("Sorting by 'websites' (ascending) and then by 'name' (ascending):\n")
print(df1.to_string(index=False))



# calculate the sum of prev_sold_date for each category
grouped = df.groupby('name')['websites'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))


# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)

# filling NaN values with 0
df.fillna("0", inplace=True)

print("\nData after filling NaN with 0:\n", df)


# create a list named data
data = [2, 5, 6, 9]
# create Pandas array using data
array1 = pd.array(data)
print(array1)


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()