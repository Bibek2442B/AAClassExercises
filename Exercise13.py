# exercise 13
# try to export dataset to a new file
# to use on the exercise 13

#paragraph a)
import pickle

#load the dataset from the file
f= open('covid8nov2020.df', 'rb')
#pickle.dump((covid, covidPrev), f)

covid, covidPrev = pickle.load(f)
f.close()

print(covid.head(2))
print(covidPrev.head(2))

# --------------------
# paragraph b)
import seaborn as sns
import matplotlib.pyplot as plt

# print(covid.corr(numeric_only=True))
dataF = covid.corr(numeric_only =True)
sns.heatmap(dataF, vmin=-1, vmax=1, cmap ='PiYG')
plt.show()

# counts the number of missing values of each column(attribute)

print(covid.isna().sum())
print(covid.isna().all())

covid.dropna(axis=1, how='all', inplace=True)
sns.set(font_scale=1.2)
sns.heatmap(covid.corr(numeric_only=True), vmin=-1, vmax=1, cmap='PiYG')
plt.show()

#--------------
#paragraph c)
sns.relplot(x='Confirmed', y='Deaths', data=covid, kind='scatter')
plt.plot(covid.Confirmed, covid.Deaths, '.b')
plt.show()


#--------------
#paragraph d)

cov10 =covidPrev[0:10]
#print(cov10)
plt.bar(cov10.Country_Region, cov10.Active, color='g', label='Actives', alpha=0.5)
plt.bar(cov10.Country_Region, cov10.Recovered, color='b', label='Recovered', alpha=0.5)
plt.bar(cov10.Country_Region, cov10.Deaths, color='r', label='Deaths', alpha=0.5)

plt.xticks(rotation='vertical')
plt.legend()
plt.title('Covid-19 cases in top 10 countries')
plt.show()
