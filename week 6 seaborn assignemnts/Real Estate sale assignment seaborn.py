import seaborn as sns 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

df= pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short (1).csv',delimiter=',',date_format=[13],index_col='Sales Ratio')
print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)


# create displot
sns.set(style= 'whitegrid')
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'gray',})
#kind='hist'
g=sns.displot(data=dffilter, x="Sale Amount" , y="Assessed Value" , hue="Address",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=Sale Amount , y=Assessed Value , hue=Address,  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("wait for me.....")
#g.figure.clear()


# kind = 'kde'
# create displot
sns.set(style= 'darkgrid')

sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'pink', 'grid.color': 'white', 'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.displot(data=dffilter, x="Sale Amount" , y="Assessed Value" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=Sale Amount , y=Assessed Value , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("wait for me.....")
#g.figure.clear()


 #create kdeplot
sns.set(style= 'darkgrid')
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.kdeplot(data=dffilter, x="Sale Amount")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=SAle Amount)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()



# create histplot
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'gray', 'grid.color': 'black'})
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g = sns.histplot(data=dffilter, x='Sale Amount', y='Assessed Value', hue='Town', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='Sale Amount', y='Assessed Value', hue='Town', multiple=stack)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


#Use Seaborn to create a plot
#create scatterplot
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'pink', 'grid.color': 'white', 'ytick.color': 'brown','xtick.color': 'brown'})
g = sns.scatterplot(x='Sale Amount', y='Assessed Value', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='Sale Amount', y='Assessed Value V', data=dffilter)"  )

# display plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create lineplot
sns.set(style= 'darkgrid')
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.lineplot(data=dffilter, x="Sale Amount" , y="Assessed Value"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=Sale Amount , y=Assessed Value  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create barplot
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.barplot(data=dffilter, x="Sale Amount", y="Assessed Value", legend=True)
g.figure.suptitle("sns.barplot(data=dffilter, x=Sale Amount, y=Assessed Value, legend=True)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create catplot
sns.set_theme(style='whitegrid', rc={'ytick.color': 'brown','xtick.color': 'brown','axes.facecolor': 'white', 'grid.color': 'black' })
g=sns.catplot(data=dffilter, x="Town", y="Sale Amount")
g.figure.suptitle("sns.catplot(data=df, x=Town, y=Sale Amount)"  )

# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()



#.pivot(index="model", columns="bed", values="price")
glue = dffilter.pivot_table(columns="Assessed Value", values="Sale Amount")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot_table(columns=Assessed Value, values=Sale Amount)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
# #g.figure.clear()
