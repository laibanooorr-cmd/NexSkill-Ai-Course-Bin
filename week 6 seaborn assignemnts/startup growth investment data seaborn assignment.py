import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# Load data from a CSV file

df = pd.read_csv('startup_growth_investment_data.csv',delimiter=",", parse_dates=[8],  date_format={'date_added': '%m-%d-%Y'} , index_col='Industry')

print(df.dtypes)
dffilter= df.head(20)
dffilter80= df.head(80)

# create displot
sns.set(style= 'whitegrid')
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'gray','ytick.color': 'brown','xtick.color': 'brown'})
#kind='hist'
g=sns.displot(data=dffilter, x="Investment Amount (USD)" , y="Number of Investors" , hue="Country",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x= Investment Amount (USD), y=Number of Investors , hue=Country,  kind='hist'  )"  )


# Display the plot
g.figure.show()
read = input("wait for me.....")
#g.figure.clear()



# kind = 'kde'
# create displot
sns.set(style= 'darkgrid')

sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'pink', 'grid.color': 'blue', 'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.displot(data=dffilter, x="Investment Amount (USD)" , y="Valuation (USD)" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=Investment Amount (USD) , y=Valuation (USD) , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("wait for me.....")
#g.figure.clear()



 #create kdeplot
sns.set(style= 'darkgrid')
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.kdeplot(data=dffilter, x="Investment Amount (USD)")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=Investment Amount (USD))"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create histplot
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'gray', 'grid.color': 'black'})
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g = sns.histplot(data=dffilter, x='Valuation (USD)', y='Investment Amount (USD)', hue='Country', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='Valuation (USD)', y='Investment Amount (USD)', hue='Country', multiple=stack)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


#Use Seaborn to create a plot
# create scatterplot
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'pink', 'grid.color': 'white', 'ytick.color': 'brown','xtick.color': 'brown'})
g = sns.scatterplot(x='Valuation (USD)', y='Investment Amount (USD)', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='Valuation (USD)', y='Investment Amount (USD)', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create lineplot
sns.set(style= 'darkgrid')
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.lineplot(data=dffilter, x="Valuation (USD)" , y="Investment Amount (USD)"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=Valuation (USD) , y=Investment Amount (USD) )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# create barplot
sns.set_theme(style='darkgrid', rc={'ytick.color': 'brown','xtick.color': 'brown'})
g=sns.barplot(data=dffilter, x="Valuation (USD)", y="Investment Amount (USD)", legend=True)
g.figure.suptitle("sns.barplot(data=dffilter, x=Valuation (USD), y=Investment Amount (USD), legend=True)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

# create catplot
sns.set_theme(style='whitegrid', rc={'ytick.color': 'brown','xtick.color': 'brown','axes.facecolor': 'gray', 'grid.color': 'white' })
g=sns.catplot(data=dffilter, x="Country", y="Investment Amount (USD)")
g.figure.suptitle("sns.catplot(data=df, x=Country, y=Investment Amount (USD))"  )

# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()


#.pivot(index="model", columns="bed", values="price")
glue = dffilter.pivot_table(columns="Valuation (USD)", values="Investment Amount (USD)")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot_table(columns=Valuation (USD), values=Investment Amount (USD))"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
# #g.figure.clear()
