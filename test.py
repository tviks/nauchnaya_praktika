from src.parser import *
from scipy.interpolate import make_interp_spline, BSpline
import matplotlib.pyplot as plt

file = "values.csv"

df = pd.read_csv(file)

n_splits = 1
dfs = []

for x in range(n_splits):
    dfs.append(df[x*int(len(df)/n_splits):(x+1)*int(len(df)/n_splits)])

fig = plt.figure()

for frame in dfs:
    plt.plot(frame['number'], frame['voltage'])

plt.show()
