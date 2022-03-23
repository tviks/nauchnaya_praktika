import pandas as pd
from urllib3 import Retry


def get_data(file_path):
    value_data = pd.read_csv(str(file_path))
    value_data.head()
    return value_data

def get_min(file_path, vel):
    value_data = pd.read_csv(str(file_path))
    min_value=value_data[vel].min()
    return min_value

def get_max(file_path, vel):
    value_data = pd.read_csv(str(file_path))
    max_value=value_data[vel].max()
    return max_value

print(get_data('C:/Users/tviks/Desktop/GitHub/nauchnaya_praktika/data/1.csv'))