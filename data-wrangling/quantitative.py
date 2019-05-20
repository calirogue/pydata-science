# turning categorical variables into quantitative variables in pythons

# Categorical variables
# problem:
# - most stat models can't take in objects / strings as input

# solution
# - add dummy variables for each unique category
# - assign 0 or 1 in each category

pd.get_dummbies(df['fuel'])
