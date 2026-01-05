import pandas as pd


df_Housing = pd.read_csv("housing_dataset.csv")
print(df_Housing.sample(10))

# Input Variables:
# CRIM: Crime Rate per capita;
# ZN: Proportion of residential land > 2323 sq.m.;
# INDUS: Proportion of used area for industries;
# CHAS: dummy Charles River dummy variable (= 1 if the land is near the river; 0 otherwise);
# NOX: Nitric oxides concentration (parts per 10 million);
# RM: Average number of rooms per dwelling;
# AGE: Proportion of owner-occupied units built prior to 1940.
# DIS: Weighted distances to five Boston employment centres.
# RAD: Index of accessibility to radial highways.
# TAX: Full-value property-tax rate per $10,000.
# PTRATIO: Pupil-teacher ratio by town.
# LSTAT: % lower status of the population.

# Output Variables:
# MEDV: Median value of owner-occupied homes in $1000's.

df_Housing.rename(columns={'MEDV':'Y'}, inplace=True)
print(df_Housing.sample(10))

# =================================
# paragraph b)
# =================================
import seaborn as sea
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

train, test= train_test_split(df_Housing, test_size=0.2, random_state=3)

print("Train......")
print(train)
print("Test........")
print(test)

# =================================
# paragraph c)
# =================================

correlation = train.corr()
# see the correlation in a heatmap
sea.heatmap(correlation, vmin=-1, vmax=1, cmap='PiYG')
# plt.show()
#or the correlation printed
print("Correlation sorted: ")
print(correlation.Y.abs().sort_values())

# =================================
# paragraph d)
# =================================
from sklearn.linear_model import LinearRegression
ourModel_LR = LinearRegression()
# names of independent variables to use
names_vi= ['RM', 'LSTAT']
ourModel_LR.fit(X=train[names_vi], y=train.Y)

print(ourModel_LR.score(X=test[names_vi], y=test.Y))

# =================================
# paragraph e)
# =================================

print(test[names_vi].head(1))
print('Price Prediction: ')
print(ourModel_LR.predict(test[names_vi].head(1)))
print('Real House Price: ')
print(test.iloc[0].Y)

# =================================
# paragraph f)
# =================================

# names of independent variables to use
names_vi= ['RM', 'LSTAT', 'INDUS']
ourModel_LR_2 = LinearRegression()
ourModel_LR_2.fit(X=train[names_vi], y=train.Y)
print(ourModel_LR_2.score(X=test[names_vi], y=test.Y))

names_vi= ['RM', 'LSTAT', 'INDUS', 'PTRATIO']
ourModel_LR_3 = LinearRegression()
ourModel_LR_3.fit(X=train[names_vi], y=train.Y)
print(ourModel_LR_3.score(X=test[names_vi], y=test.Y))

# print(df_Housing.columns[:-1])

names_vi= df_Housing.columns[:-1] #all the independent variables
ourModel_LR_4 = LinearRegression()
ourModel_LR_4.fit(X=train[names_vi], y=train.Y)
print(ourModel_LR_4.score(X=test[names_vi], y=test.Y))

# =================================
# paragraph g)
# =================================

import pickle
file=open('boston_train_and_test.df','wb')
pickle.dump((train,test),file)
file.close()

