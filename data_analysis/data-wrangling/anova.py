# analysis of variance (anova)
# - stat comparison of groups
# - example: average price of different vehicle makes

# Why?
# - finding correlation between different groups of a categorical variable
# Obtain?
# - F-test score : variation between sample means divided by variation within sample group
# - P-value : confidence degree

df_anova = df[["make", "price"]]
grouped_anova = df_anova.groupby(["make"])
