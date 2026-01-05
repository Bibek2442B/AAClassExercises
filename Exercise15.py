import seaborn as sea
import matplotlib.pyplot as plt
import ssl

# load the dataset containing 150 samples of iris flowers
# from 3 species
# each row has 5 attributes:
# 4 numerical(in centimeters): sepal_length, sepal_width, petal_length, petal_width
# and 1 categorical label species
ssl._create_default_https_context = ssl._create_unverified_context

iris = sea.load_dataset("iris")

# prints general information about the dataset
print(iris.info())
print(iris.head(3))

# set the plot a dark grid one of the Seaboard's predefined style
sea.set_style("darkgrid")
# increases the font size
sea.set(font_scale=1.2)

# create the Scatter Plot
b = sea.relplot(x='petal_width', y='petal_length',
                    kind='scatter', data=iris, hue='species',
                    palette= 'Set1' )

plt.show()