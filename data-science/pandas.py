# upload csv | working with jupyter labs
# Loading data with pandas

# import pandas
import pandas

# stores the path as a csv
csv_path = '/home/../rogue-data/CRM-Eleven.csv'

# df - dataframe
df = pandas.read_csv(csv_path)

# or
df = pd.read_csv(csv_path)
df.head()

# ---------------
# accessing different parts of the database:
df['Name']
# command will show all the data under the 'Name' column
df['Name'].unique()
# command will show all the unique data in name
df['Name'] >= 2018
# selecting a piece of data within a few rows
