import pandas as pd

covid =pd.read_csv("11-08-2020.csv")

#paragraph a
print(covid.shape)
print(covid.columns)
print(covid.dtypes)

#paragraph b
print(covid.info)

print(covid.head())
print(covid.tail())

#paragraph c

#new datase with the number of confirmed, recovered, active and fatality cases

covidDF= covid[['Country_Region', 'Confirmed', 'Recovered', 'Active', 'Deaths']]
print(covidDF)

#...and sort it in descending order of confirmed cases
covidDF.copy().sort_values('Confirmed', ascending=False,inplace=True)
print(covidDF)

#organize the index after sorting
covidDF.reset_index(inplace=True, drop=True)
print(covidDF)

#paragraph d

#Check where Portugal is in the ranking of countries with the most confirmed cases, and place our country on the world
#stage in terms of location and dispersion measures.
print(covidDF[covidDF['Country_Region']=='Portugal'])
print(covidDF[covidDF['Country_Region']=='Portugal'].describe())


#  Finally, view all the rows in the table with a single output
pd.set_option('display.max_rows', None)
print(covidDF)

pd.reset_option('display.max_rows')


#paragraph e

#view the top 10 countries with the most deaths
print(covidDF.sort_values('Deaths', ascending=False).head(10))

#paragraph f
# Determine the Portuguese and global COVID-19 case fatality rates


sumofDeaths=covid.Deaths.sum()
sumofConfirmed=covid.Confirmed.sum()

rateofDeaths=(sumofDeaths/sumofConfirmed)*100
print('\nRate of deaths in world = {:.2f}%'.format(rateofDeaths))

# Determine the Portuguese COVID-19 case

deathsPortugal= covid[covid['Country_Region']=='Portugal'].Deaths.sum()
confirmedPortugal= covid[covid['Country_Region']=='Portugal'].Confirmed.sum()

rateofDeathsPortugal=(deathsPortugal/confirmedPortugal)*100
print('\nRate of deaths in Portugal = {:.2f}%'.format(rateofDeathsPortugal))

#Paragraph g
covidPrev= pd.read_csv("11-08-2020.csv")
print(covidPrev)
print((covidPrev.Combined_Key!=covid.Combined_Key).any())
print((covidPrev.Combined_Key!=covid.Combined_Key).all())
print((covidPrev.Combined_Key!=covid.Combined_Key).sum())

day=covid[['Confirmed','Recovered', 'Active', 'Deaths']]
print(day)
print(day.head(10))

# Exercise 13
# Try to export dataset to a new file
# To use on the exercise 13

import pickle

f=open('covid8nov2020.df','wb')
pickle.dump((covid,covidPrev),f)
f.close()

print(covid.head(2))
print(covidPrev.head(2))


# Paragraph b
import seaborn as sns
import matplotlib.pyplot as plt

dataF=covid.corr(numeric_only=True)
sns.heatmap(dataF, vmin=1, cmap='PiYG')
plt.show()





