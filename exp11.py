import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),
                  columns=['A','B','C','D'])

df.iloc[2,1] = np.nan
df.iloc[5,3] = np.nan
df.iloc[7,0] = np.nan

print(df)

print("\nNaN Positions:")
print(df.isnull())
