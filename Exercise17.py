#=========================================

import pickle
file=open('boston_train_and_test.df','rb')
(train,test)=pickle.load(file)
file.close()
print(train)

# names of the independent variables to use
names_vi= ['RM', 'LSTAT']

# polynomial regression
from sklearn.preprocessing import PolynomialFeatures
order=2
pf = PolynomialFeatures(degree=order)

# creates new columns with exponential from the ones that are until theorder indicated
xpol = pf.fit_transform(train[names_vi])
print(xpol)

pf.get_feature_names_out(names_vi)

from sklearn.linear_model import LinearRegression
ourModel = LinearRegression()
ourModel.fit(X=xpol, y=train.Y)

xpol_test = pf.fit_transform(test[names_vi])

print(ourModel.score(X=xpol_test, y=test.Y))

#====================
# paragraph b
#======================
#Use the developed polynomial regression model to predict the price of a house with the characteristics of the first example in the test set.
#Compare it to the actual value.

xpol_test0 = pf.fit_transform(test[names_vi].head(1))
print(xpol_test0)
#predicted price
print(ourModel.predict(xpol_test0))
# real house price
print(test.iloc[0].Y)

order=4
pf = PolynomialFeatures(degree=order)

names_vi= train.drop('Y',axis=1).columns
print(names_vi)

names_vi= ['RM', 'LSTAT', 'INDUS', 'PTRATIO']
print(names_vi)

xpol = pf.fit_transform(train[names_vi])

ourModel_2 = LinearRegression()
ourModel_2.fit(X=xpol, y= train.Y)

xpol_test = pf.fit_transform(test[names_vi])

print(ourModel_2.score(X= xpol_test, y =test.Y))



