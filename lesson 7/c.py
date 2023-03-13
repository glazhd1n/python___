import pandas as pd

a = pd.read_json('sample-data.json').dropna()
pd.options.display.max_rows = 9999
print(a.to_string())