import seaborn as sns 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 


df = pd.read_csv('RealEstate-USA.csv',delimiter= ',', parse_dates=[11],  date_format={'date_added': '%d-%m-%Y'} , index_col='brokered_by' )
print(df.dtypes)
dffilter = df.head(40)
dffilter100 = df.head(100)


# create displot
sns.set(style= 'whitegrid')
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'gray', 'grid.color': 'white'})
#kind='hist'
g=sns.displot(data=dffilter, x="bed" , y="price" , hue="bath",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=bed , y=price , hue=bath,  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("wait for me.....")
#g.figure.clear()



# kind = 'kde'
# create displot
sns.set(style= 'darkgrid')

sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'yellow', 'grid.color': 'white'})
g=sns.displot(data=dffilter, x="bed" , y="price" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=bed , y=price , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("wait for me.....")
#g.figure.clear()


# create kdeplot
g=sns.kdeplot(data=dffilter, x="bed")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create histplot
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'gray', 'grid.color': 'white'})
g = sns.histplot(data=dffilter, x='bed', y='price', hue='bath', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='bed', y='price', hue='bath', multiple=stack)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


#Use Seaborn to create a plot
# create scatterplot
sns.set_theme(style='whitegrid', rc={'axes.facecolor': 'pink', 'grid.color': 'blue'})
g = sns.scatterplot(x='bed', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='bed', y='price', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()



# create lineplot
sns.set(style= 'darkgrid')
g=sns.lineplot(data=dffilter, x="bed" , y="price"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=bed , y=price  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create barplot
sns.set_theme(style='whitegrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.barplot(data=dffilter, x="bed", y="price", legend=True)
g.figure.suptitle("sns.barplot(data=dffilter, x=bed, y=price, legend=True)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create catplot
sns.set_theme(style='whitegrid', rc={'ytick.color': 'blue','xtick.color': 'blue','axes.facecolor': 'pink' })
g=sns.catplot(data=dffilter, x="bed", y="price")
g.figure.suptitle("sns.catplot(data=df, x=bed, y=price)"  )

# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()


#.pivot(index="model", columns="bed", values="price")
glue = dffilter.pivot_table(columns="bed", values="price")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot_table(columns=city, values=price)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
# #g.figure.clear()