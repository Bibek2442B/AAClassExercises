from traceback import print_tb

import pandas as pd
import seaborn as sea
#=================
# paragraph a
from sklearn.datasets import load_breast_cancer

cancer= load_breast_cancer()
print(cancer.DESCR)

print(cancer.target)
print(cancer.target_names)

print(cancer.feature_names)

df= pd.DataFrame(cancer.data, columns=cancer.feature_names)
df['diagnosis'] = cancer.target
print(df)

df.diagnosis = df.diagnosis.map({0: 'malignant', 1: 'benign'})
print(df)

print(df.diagnosis.value_counts())

#============
# paragraph b

import matplotlib.pyplot as plt
sea.relplot(x='mean radius', y='mean texture', data=df, hue='diagnosis', palette=['r', 'b'])
plt.show()

#==============
# paragraph c

from sklearn.model_selection import train_test_split

#a few notes about the parameters:
#test_size=0.3: define 30% of data to the test set and 70% to the training set
#random_state=222: define the seed for the random number generator, ensuring reproducibility of the results will be chosen every time we run the code
#stratify=df.diagnosis: define the stratification of the data, so that the training set will have the same distribution of classes as the test set
Xtrain, Xtest, Ytrain, Ytest = train_test_split(df.drop('diagnosis', axis=1), df['diagnosis'], test_size=0.3, random_state=222, stratify=df.diagnosis)

#====================
# paragraph d

# Using Scikit-learn, create the logistic regression model that allows us to classify the type
# of disease (benign/malignant) based on the 30 available predictors, training it, and
# calculate its success rate.

from sklearn.linear_model import LogisticRegression
ourModel = LogisticRegression()
ourModel.fit(X=Xtrain, y=Ytrain)

#success rate
print(ourModel.score(X=Xtest, y=Ytest))

#====================
# paragraph e
# The accuracy rate is not, by itself, sufficient to evaluate the true performance of a model,
# particularly in datasets with class imbalance. Observe better the model's capability by
# using metrics that allow a more consistent (more reliable) assessment of its true
# performance, such as the confounding matrix, f1 measure, ROC curve and AUC value.

predictions = ourModel.predict(X=Xtest)
probs = ourModel.predict_proba(X=Xtest)
print(probs)

#probability of positive diagnosis
print(probs[:,1])
diagnostic = pd.DataFrame({'prob': probs, 'predict': predictions, 'real': Ytest})
print(diagnostic)

pd.crosstab(diagnostic.real, diagnostic.predict)

from sklearn import metrics
print(metrics.f1_score(y_true= diagnostic.real, y_pred= predictions, pos_label='malignant'))

metrics.roc_auc_score(diagnostic.real, diagnostic.prob)
metrics.RocCurveDisplay.from_estimator(ourModel, y=Ytest, X=Xtest)

plt.show()

Xtest.head(1)
ourModel.predict(Xtest.head(1))

print(round(ourModel.predict_proba(Xtest.head(1))[:,0].max))
### sigmoid function
import numpy as np

x=np.arange(-10,10,0.0001)

# iterates with each item n from the list x
# np.exp(-n) calculates the exponential of -n used by numpy
# 1/(1+np.exp(-n)) that's the sigmoid function (see powerpoint presentation
y=[(1/(1+np.exp(-n))) for n in x]

plt.subplot(121)
plt.plot(x,y)

plt.xlabel('Predicted variable')
plt.ylabel('Probability of positive class occur')
plt.xticks([])
plt.title('Probability of malignant')
plt.show()





