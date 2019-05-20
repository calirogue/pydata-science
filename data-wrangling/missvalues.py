# missing value:
# missing values occur when no data value is stoed for a
# variable (feature) is an observation
# could rep as ?, N/A, 0

# How to deal with missing data?
# - check source
# - drop variable
# - drop data entry

# replace the missing values
# - replace it with an average of datapoints
# - replace it based on other functions
# - replace it by frequency

# Leave it


# ______
# How to drop missing values in python
# use:
dataframes.dropna():

    # how to replace missing values in python
    # use:
dataframe.replace(missing_value, new_value):

    # average example
mean = df["example"].mean()
df[example].replace(np.nan, mean)
