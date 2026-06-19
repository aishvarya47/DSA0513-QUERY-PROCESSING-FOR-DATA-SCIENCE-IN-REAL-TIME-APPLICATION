import pandas as pd

df = pd.DataFrame({
    'Name':['Alex','Amy','Allen']
})

df['Name'] = df['Name'].str.swapcase()

print(df)
