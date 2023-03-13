import pandas as pd

a = pd.read_csv('data.csv').dropna()
pd.options.display.max_rows = 9999

print(a)