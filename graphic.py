from mpl_toolkits.axisartist.axislines import AxesZero
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import ndimage
from src.parser import *

file = "values.csv"

figure(figsize=(8, 8), dpi=150)

SMALL_SIZE = 2
MEDIUM_SIZE = 10
BIGGER_SIZE = 20

#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

ax = plt.gca()

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_label_coords(.0, .1)
ax.set_ylabel(ylabel='current', loc='top', rotation=0)
ax.set_xlabel(xlabel='voltage', loc='right', rotation=0)

value_data = pd.read_csv("values.csv")
value_data.head()
value_data['mov_avg'] = value_data['voltage']
print(value_data)


sns.scatterplot(x="voltage", y="current", data=value_data, color="g", s=30)
sns.lineplot(x="voltage", y="current", data=value_data, alpha=1, 'r-.')

#sns.lmplot(x='voltage', y='current', data=value_data, hue='number', ci=None, order=5, truncate=True)

plt.show()