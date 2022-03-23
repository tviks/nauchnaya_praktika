from mpl_toolkits.axisartist.axislines import AxesZero
from matplotlib.pyplot import figure
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
from src.parser import *

def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = '{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)
    #plt.close()

def create_plot(file_path):
    figure(figsize=(5, 5), dpi=100)

    MEDIUM_SIZE = 15

    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels

    ax = plt.gca()

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_label_coords(.0, .1)
    ax.xaxis.set_label_coords(.1, 0.5)
    ax.set_ylabel(ylabel='Ток', loc='top', rotation=0)
    ax.set_xlabel(xlabel='Напряжение', loc='right', rotation=90)

    value_data = pd.read_csv(file_path)
    value_data.head()

    sns.lineplot(x="vol", y="cur", data=value_data, alpha=1, linewidth = 3)
    sns.scatterplot(x="vol", y="cur", data=value_data, color="black", s=50)
    
    save(name='pic', fmt='png')
    return('pic')