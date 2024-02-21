import pandas as pd
import pathlib
from pathlib import Path

pd.set_option('display.max_rows', None)
pd.set_option('display.max_column', None)
pd.set_option('display.max_colwidth', None)

work_path = pathlib.Path.cwd()
print(work_path)
data_path = Path(work_path, 'datasets', 'bikes.csv')
print(data_path)
data = pd.read_csv(data_path, header = None)
data = pd.read_csv(data_path, nrows=3)
data = pd.read_csv(data_path, header=0, skiprows=[3, 5, 8], sep='/')
print(data)



