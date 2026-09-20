import sys

# viewing arguments passed when running the script
print ('arguments', sys.argv)
month = int(sys.argv[1])
print(f'hello pipeline, month={month}')

###### Using pandas #######
import pandas as pd

# create a df
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df['month'] = month # tieing it in with the argument from earlier
print(df.head())

# converting to parquet
df.to_parquet(f"output_{month}.parquet")