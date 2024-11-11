# -*- coding: utf-8 -*-
"""CIE1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AKgNj0iBvxjZ0T00Ghixr7p_r9dNaXuX
"""

import pandas as pd
data=pd.read_csv("/content/mtcars (1).csv")
print(data)

import matplotlib.pyplot as plt
plt.hist(data['mpg'],bins=10,color='grey',edgecolor='k')
plt.title('Frequency Distribution of Miles per Gallon (mpg)')
plt.xlabel('Miles per Gallon (mpg)')
plt.ylabel('Frequency')
plt.grid()
plt.show()

import matplotlib.pyplot as plt
plt.scatter(data['wt'], data['mpg'], color='r', alpha=0.5)
plt.title('Relationship between Car Weight and MPG')
plt.xlabel('Weight of the Car')
plt.ylabel('Miles per Gallon (MPG)')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
tc = data.groupby('manufacturer').size().nlargest(5)
tc.plot(kind='bar', color='lightpink')
plt.title('Frequency Distribution of Transmission Types')
plt.xlabel('types of cars')
plt.ylabel('Frequency')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8,4))
sns.boxplot(x=data['mpg'] ,data=data,color='y')
plt.title('Box and Whisker Plot of mpg')
plt.xlabel('Miles per Gallon (MPG)')
plt.show()

summaries=data['mpg'].describe()
print(summaries)