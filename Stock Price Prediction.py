# -*- coding: utf-8 -*-
"""Stock2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cwLzlpJqgpss_MshrXQqwTD-CcnQULFJ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
df = pd.read_csv('/content/Reliance.csv')
df.head()

import pandas as pd
df = pd.read_csv('/content/Reliance.csv')
df.shape

import pandas as pd
df = pd.read_csv('/content/Reliance.csv')
df.info()

import pandas as pd
df = pd.read_csv('/content/Reliance.csv')
df.describe()

import matplotlib.pyplot as plt
import seaborn as sb

plt.figure(figsize=(15,5))
plt.plot(df['Close'])
plt.title('Reliance.', fontsize=15)
plt.ylabel('Price in dollars.')
plt.show()

import pandas as pd
df = pd.read_csv('/content/Reliance.csv')
df.isnull().sum()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
import pandas as pd # import pandas for reading the csv file
warnings.filterwarnings('ignore')

#Read the csv file with thousands separator as comma
df = pd.read_csv('/content/Reliance.csv', thousands=',') # Tell pandas to treat commas as thousands separators

features = ['Open', 'High', 'Low', 'Close', 'Volume']

plt.subplots(figsize=(20,10))

for i, col in enumerate(features):
  plt.subplot(2,3,i+1)
  sb.distplot(df[col])
  plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
import pandas as pd # import pandas for reading the csv file
warnings.filterwarnings('ignore')

#Read the csv file with thousands separator as comma
df = pd.read_csv('/content/Reliance.csv', thousands=',') # Tell pandas to treat commas as thousands separators

features = ['Open', 'High', 'Low', 'Close', 'Volume']


plt.subplots(figsize=(20,10))
for i, col in enumerate(features):
  plt.subplot(2,3,i+1)
  sb.boxplot(df[col])
  plt.show()

import pandas as pd # import pandas for reading the csv file

df = pd.read_csv('/content/Reliance.csv')

splitted = df['Date'].str.split('/', expand=True)

df['day'] = splitted[1].astype('int')
df['month'] = splitted[0].astype('int')
df['year'] = splitted[2].astype('int')

df['is_quarter_end'] = np.where(df['month']%3==0,1,0)

df.head()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
import pandas as pd # import pandas for reading the csv file
warnings.filterwarnings('ignore')

#Read the csv file with thousands separator as comma
df = pd.read_csv('/content/Reliance.csv', thousands=',') # Tell pandas to treat commas as thousands separators

# Extract year from the 'Date' column
df['year'] = pd.to_datetime(df['Date']).dt.year  # Extract year from 'Date'

features = ['Open', 'High', 'Low', 'Close', 'Volume']

plt.subplots(figsize=(20,10))

# data_grouped = df.groupby('year').mean()
plt.subplots(figsize=(20,10))

for i, col in enumerate(['Open', 'High', 'Low', 'Close']):
  plt.subplot(2,2,i+1)
  # data_grouped[col].plot.bar()
  plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#Read the csv file with thousands separator as comma
df = pd.read_csv('/content/Reliance.csv', thousands=',') # Tell pandas to treat commas as thousands separators
df['open-close'] = df['Open'] - df['Close']
df['low-high'] = df['Low'] - df['High']
df['target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

plt.pie(df['target'].value_counts().values,
		labels=[0, 1], autopct='%1.1f%%')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#Read the csv file with thousands separator as comma
df = pd.read_csv('/content/Reliance.csv', thousands=',') # Tell pandas to treat commas as thousands separators

# Select only numerical columns for correlation calculation
numerical_df = df.select_dtypes(include=['number'])

plt.figure(figsize=(10, 10))

# As our concern is with the highly
# correlated features only so, we will visualize
# our heatmap as per that criteria only.
sb.heatmap(numerical_df.corr() > 0.9, annot=True, cbar=False)
plt.show()