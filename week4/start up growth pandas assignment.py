import pandas as pd

df = pd.read_csv('startup_growth_investment_data.csv',delimiter=",",parse_dates=[8], date_format={'date_added': '%d-%m-%Y'})

print(df)

print("df - data types" , df.dtypes)
print("df.info():   " , df.info() )

# display the last three rows
print('Last three Rows:')
print(df.tail(4))

# display the first three rows
print('First Three Rows:')
print(df.head(4))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). 
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape) # output  (10000, 10)


# access the Name column
Price = df['Funding Rounds']
print("access the Name column: df : ", Price)

# access multiple columns
price_status = df[['Funding Rounds','Investment Amount (USD)']]
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
first_row4 = df.loc[df['Funding Rounds'] ==  2]
print("Conditional selection of rows using .loc")
print(first_row4)


#Selecting a single column using .loc
first_row5 = df.loc[:1,'Funding Rounds']
print("Selecting a single column using .loc")
print(first_row5)

#Selecting multiple columns using .loc
first_row6 = df.loc[:,['Funding Rounds','Investment Amount (USD)']]
print("Selecting multiple columns using .loc")
print(first_row6)

#Selecting a slice of columns using .loc
first_row7 = df.loc[:1,'Country':'Year Founded']
print("Selecting a slice of columns using .loc")
print(first_row7)

#Combined row and column selection using .loc
first_row8 = df.loc[df['Industry'] == 'E-commerce','Country':'Year Founded']
print("#Combined row and column selection using .loc")
print(first_row8)
# Case 1 : using .loc - default case - ends here

print("# Case 2 : using .loc with index_col - starts here")


 #index_col='Startup Name'
df_index_col = pd.read_csv('startup_growth_investment_data.csv',delimiter=",",parse_dates=[8], date_format={'date_added': '%d-%m-%Y'} , index_col='Startup Name')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())


#Second cycle - with index_col as Startup Name
#Selecting a single row using .loc
first_row = df_index_col.loc['Startup_5']
print("Selecting a single row using .loc")
print(first_row)

##Selecting multiple rows using .loc
first_row2 = df_index_col.loc[['Startup_5', 'Startup_7']]
print("#Selecting multiple rows using .loc")
print(first_row2)

#Selecting a slice of rows using .iloc
first_row3 = df_index_col.loc['Startup_5':'Startup_7']
print("Selecting a slice of rows using .loc")
print(first_row3)


# #Conditional selection of rows using .loc
first_row4 = df_index_col.loc[df_index_col['Country'] == 'India']
print("Conditional selection of rows using .loc")
print(first_row4)


# #Selecting a single column using .iloc
first_row5 = df_index_col.loc[:'Startup_5']
print("Selecting a single column using .iloc")
print(first_row5)

# #Selecting multiple columns using .loc
first_row6 = df_index_col.loc[:'Startup_5',['Industry', 'Country']]
print("Selecting multiple columns using .loc")
print(first_row6)


# #Selecting a slice of columns using .loc
first_row7 = df_index_col.loc[:'Startup_5','Industry':'Country']
print("Selecting a slice of columns using .loc")
print(first_row7)

# #Combined row and column selection using .loc
first_row8 = df_index_col.loc[df_index_col['Country'] == 'Germany','Industry':'Valuation (USD)']
print("#Combined row and column selection using .loc")
print(first_row8)


# # Case 2 : using .loc with index_col  -  ends here
print("Case 3 : Using .iloc - starts here")
# # Case 3 : Using .iloc - starts here


# #Selecting a single row using .iloc
first_row = df_index_col.iloc[7]
print("Selecting a single row using .iloc")
print(first_row)

# #Selecting multiple rows using .iloc
first_row2 = df_index_col.iloc[[1, 4,5]]
print("Selecting multiple rows using .iloc")
print(first_row2)

# #Selecting a slice of rows using .iloc
first_row3 = df_index_col.iloc[1:4]
print("#Selecting a slice of rows using .iloc")
print(first_row3)

# #Selecting a single column using .iloc
first_row5 = df_index_col.iloc[:,5]
print("#Selecting a single column using .iloc")
print(first_row5)

# #Selecting multiple columns using .iloc
first_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(first_row6)


# #Selecting a slice of columns using .iloc
first_row7 = df_index_col.iloc[:,1:2]
print("#Selecting a slice of columns using .iloc")
print(first_row7)

# #Combined row and column selection using .iloc
first_row8 = df_index_col.iloc[[1, 3,5],1:4]
print("#Combined row and column selection using .iloc")
print(first_row8)


# # Case 3 : Using .iloc - ends here
print("Next Run")

# #Add a New Row to a Pandas DataFrame
df.loc[len(df.index)] = ['Startup Name','Industry','Funding Rounds','Investment Amount (USD)','Valuation (USD)','Number of Investors','Country','Year Founded','Growth Rate (%)']
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
df.drop('Number of Investors', axis=1, inplace=True)
# delete marital status column
df.drop(columns='Country', inplace=False)
# delete height and profession columns
df.drop(['Country'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete page_url ,property_type , location , city , column :")
print(df)

#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {'City': 'City_changed'}, inplace=True)
# rename columns 'Age' and 'City'
df.rename(mapper= {'Industry': 'Industry_Changed', 'Year Founded':'Year Founded_Changed'}, axis=1, inplace=True)
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

# select the rows which is Industry_Changed == "Blockchain" or `Year Founded_Changed` == "2003"
selected_rows = df.query('Industry_Changed == "Blockchain" or `Year Founded_Changed` == "2003"', engine = 'python')

print(selected_rows.to_string())
print(len(selected_rows))

# sort DataFrame  in ascending order
sorted_df = df.sort_values(by='Industry_Changed')
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns
df1 = df.sort_values(by=['Industry_Changed', 'Startup Name'])

print("Sorting by 'Industry_Changed' (ascending) and then by 'Startup Name' (ascending):\n")
print(df1.to_string(index=False))

# calculate the sum of prev_sold_date for each category
grouped = df.groupby('Startup Name')['Industry_Changed'].sum()

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
