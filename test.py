import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel("Documents/matches.xlsx", "Sheet1")
var=df.groupby(['team1']).sum().stack()

temp=var.unstack()

type(temp)
x_list = temp['winner']
label_list = temp.index
pyplot.axis("equal") #The pie chart is oval by default. To make it a circle use pyplot.axis("equal")
#To show the percentage of each pie slice, pass an output format to the autopctparameter 
plt.pie(x_list,labels=label_list,autopct="%1.1f%%") 
plt.title("matches comparison")
plt.show()
