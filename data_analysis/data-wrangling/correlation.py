# What is correlation?
# - measure to what extent different variables are interdependent
# Example : lung cancer -> smoking
# - correlation doesn't imply causation


# Positive linear relationship
# - correlation between two features(engine size and price)
# up

# Neg linear relationship
# - correlation between two features(highway mpg and price)
# down

# weak correlation


# -- statistics

# Peason correlation

# Measure the strenth correlation between two features
#   - correlation coefficient
#   - P-value

# Correlation coefficient
# - close +1 large positive relationship
# - close to -1 neg relationship
# - close to 0: no relationship

# P-value
# - P-value < 0.001 Strong - certain in result
# - P-value < 0.05 moderate - certain in result
# - P-value < 0.1 weak - certain in result
# - P-value > 0.1 no certain in result

# strong correlation
# - correlation coefficient close to 1 or -1
# - P value less than 0.001

# example: sipi stats package
Pearson_coef, p_value = stats.personr[['horsepower'], df['price']]
