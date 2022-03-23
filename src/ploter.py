from mpl_toolkits.axisartist.axislines import AxesZero
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import ndimage
from src.parser import *

figure(figsize=(8, 8), dpi=150)

MEDIUM_SIZE = 10

plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels

ax = plt.gca()

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_label_coords(.0, .1)
ax.set_ylabel(ylabel='cur', loc='top', rotation=0)
ax.set_xlabel(xlabel='vol', loc='right', rotation=0)

def create_plot(file_path):
    value_data = pd.read_csv(file_path)

    print(value_data)
    value_data.head()

    sns.scatterplot(x="vol", y="cur", data=value_data, color="g", s=30)
    sns.lineplot(x="vol", y="cur", data=value_data, alpha=1)


    plt.show()