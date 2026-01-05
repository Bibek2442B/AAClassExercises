import seaborn as sea
import matplotlib.pyplot as plt
import ssl
import urllib.request

# Create an unverified SSL context to handle certificate issues
ssl._create_default_https_context = ssl._create_unverified_context

titanic = sea.load_dataset("titanic")
print(titanic)
print(titanic.describe())

q=sea.catplot(x="who", y="age", errorbar=None, kind="bar", data=titanic)
q.set_axis_labels("", "Age")
q.set_xticklabels(["Men", "Women","Children"])
plt.show()

b=sea.catplot(x="who", y="age", errorbar=None, kind="strip", data=titanic)
b.set_axis_labels("", "Age")
b.set_xticklabels(["Men", "Women","Children"])
plt.show()

c=sea.catplot(x="who", y="survived", errorbar=None, kind="bar", data=titanic)
c.set_axis_labels("", "Survived")
c.set_xticklabels(["Men", "Women","Children"])
plt.show()

# paragraph d)
# d=sea.catplot(x="who", y="survived", errorbar=None, kind="bar", data=titanic,hue="class")
d=sea.catplot(x="who", y="survived", errorbar=None, kind="bar", data=titanic,col="class")
# d=sea.catplot(x="who", y="survived", errorbar=None, kind="bar", data=titanic,col="who")


d.set_axis_labels("", "Survived")
d.set_xticklabels(["Men", "Women","Children"])
plt.show()

e=sea.catplot(x='who', y='fare',errorbar=None, data=titanic, kind='bar', hue='class')
e.set_axis_labels('', 'Average Fare')
# e.set_xticklabels(['Men', 'Women','Children'])
plt.show()

