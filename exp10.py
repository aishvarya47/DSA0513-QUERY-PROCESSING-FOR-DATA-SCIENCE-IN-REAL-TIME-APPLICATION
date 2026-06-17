import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10,4),
    columns=['A','B','C','D']
)

def color_negative(val):
    if val < 0:
        return 'color:red'
    else:
        return 'color:black'

styled_df = df.style.map(color_negative)

print(df)
