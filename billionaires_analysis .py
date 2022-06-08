"""
The number of billionaires in a country says a lot about the business environment, 
startup success rate, and many other economic features of a Country. 
So if you want to learn more about how we can find relationships among billionaires around the world, 
this article is for you. In this article, I will walk you through the task of billionaires analysis with Python.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Billionaire.csv")
print(data.head())

#Before we go ahead, let’s see whether or not this dataset contains missing values

print(data.isnull().sum())
data = data.dropna()

#The NetWorth column in this dataset has a $ sign at the beginning of Billionaires’ Net worth and B at the end. 
# So we need to remove these signs and convert the NetWorth column to float

data["NetWorth"] = data["NetWorth"].str.strip("$")
data["NetWorth"] = data["NetWorth"].str.strip("B")
data["NetWorth"] = data["NetWorth"].astype(float)

#Now let’s have a look at the top 10 billionaires according to their NetWorth

df = data.sort_values(by = ["NetWorth"], ascending=False).head(10)
plt.figure(figsize=(20, 10))
sns.histplot(x="Name", hue="NetWorth", data=df)
plt.show()

#Now let’s have a look at the top 5 domains with the most number of billionaires

a = data["Source"].value_counts().head()
index = a.index
sources = a.values
custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(5, 5))
plt.pie(sources, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Domains to Become a Billionaire", fontsize=20)
plt.show()

#Now let’s have a look at the top 5 industries with the most number of billionaires

a = data["Industry"].value_counts().head()
index = a.index
industries = a.values
custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(5, 5))
plt.pie(industries, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Industries with Most Number of Billionaires", fontsize=20)
plt.show()

#Now let’s have a look at the top 5 countries with the most number of billionaires

a = data["Country"].value_counts().head()
index = a.index
Countries = a.values
custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(5, 5))
plt.pie(Countries, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Countries with Most Number of Billionaires", fontsize=20)
plt.show()

#The visualization above shows that the United States and China are the countries from which most people become billionaires. 
#So that means the business environment and the startup success rate is really good in the US and China compared to the rest of the world.


"""
Summary

So this is how you can find patterns among billionaires around the world to analyze the business environment of countries. 
The success of a business or startup depends a lot on the business environment of a country. 
At the end of the analysis of global billionaires, 
I found that China and the United States are the countries with the most billionaires which concludes that the business environment and the success rate of a startup is much better in the US and China than in the rest of the world. 
Hope you liked this article on Billionaires Analysis with Python. 
Please feel free to ask your valuable questions in the comments section below.
"""