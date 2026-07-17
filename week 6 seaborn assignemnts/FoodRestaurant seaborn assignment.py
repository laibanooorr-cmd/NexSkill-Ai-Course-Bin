import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# Load data from a CSV file

df = pd.read_csv('FastFoodRestaurants.csv',delimiter=",", parse_dates=[9],  date_format={'date_added': '%m-%d-%Y'} , index_col='address')

print(df.dtypes)
dffilter= df.head(20)
dffilter80= df.head(80)


# create displot
sns.set(style= 'whitegrid')
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'black',})
#kind='hist'
g=sns.displot(data=dffilter, x="longitude" , y="country" , hue="name",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=longitude , y=country , hue=name,  kind='hist'  )"  )


# Display the plot
g.figure.show()
read = input("wait for me.....")
#g.figure.clear()


# kind = 'kde'
# create displot
sns.set(style= 'darkgrid')

sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'pink', 'grid.color': 'white', 'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.displot(data=dffilter, x="latitude" , y="longitude" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=latitude , y=longitude , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("wait for me.....")
#g.figure.clear()



 #create kdeplot
sns.set(style= 'darkgrid')
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.kdeplot(data=dffilter, x="longitude")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=longitude)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create histplot
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'gray', 'grid.color': 'black'})
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g = sns.histplot(data=dffilter, x='longitude', y='latitude', hue='country', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='longitude', y='latitude', hue='country', multiple=stack)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


#Use Seaborn to create a plot
# create scatterplot
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'pink', 'grid.color': 'white', 'ytick.color': 'brown','xtick.color': 'brown'})
g = sns.scatterplot(x='longitude', y='latitude', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='longitude', y='latitude', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create lineplot
sns.set(style= 'darkgrid')
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.lineplot(data=dffilter, x="longitude" , y="latitude"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=longitude , y=latitude  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create barplot
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.barplot(data=dffilter, x="longitude", y="latitude", legend=True)
g.figure.suptitle("sns.barplot(data=dffilter, x=longitude, y=latitude, legend=True)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create catplot
sns.set_theme(style='whitegrid', rc={'ytick.color': 'brown','xtick.color': 'brown','axes.facecolor': 'white', 'grid.color': 'black' })
g=sns.catplot(data=dffilter, x="country", y="latitude")
g.figure.suptitle("sns.catplot(data=df, x=country, y=latitude)"  )

# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()


#.pivot(index="model", columns="bed", values="price")
glue = dffilter.pivot_table(columns="longitude", values="latitude")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot_table(columns=longitude, values=latitude)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
# #g.figure.clear()