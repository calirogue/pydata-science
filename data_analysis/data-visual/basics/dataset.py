# Dataset
# population division of the UN compiled data pertaining to 45 countries

# Read data into pandas dataframe

# useful for many scientific computing in python
import numpy as np
# primary data structure library
import pandas as pd
# adds compatibility to python 3
from __future__ import print_function

# install xlrd
!pip install xlrd
# used to abstract data from excel
print('xlrd installed!')

df_can = pd.read_excel(

)

# Display dataframe in pandas
df_can.head()
#  or
df.head()
