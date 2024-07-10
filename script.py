import pandas as pd
import numpy as np

#suppress warnings 
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

URL ="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Extract tables from webpage
tables = pd.read_html(URL)
df = tables[3]

# Replace the column headers with column numbers    
df.columns = range(df.shape[1])

# Retain important columns 
df = df[[0,2]]

# Retain firt ten rows
df = df.iloc[1:11,:]

# Assign column names
df.columns = ['Country','GDP (Million USD)']

# Change the data type of the 'GDP (Million USD)' column to integer.
df['GDP(Million USD)'] = df['GDP(Million USD)'].astype(int)

# Convert the GDP value in Million USD to Billion USD
df[['GDP(Million USD)']] = df[['GDP(Million USD)']]/1000

# Use numpy.round() method to round the value to 2 decimal places.
df['GDP(Million USD)'] = np.round(df[['GDP(Million USD)']],2)

# Rename the column header from 
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'})

# Load the DataFrame to the CSV file
df.to_csv('./Largest_economies.csv')
