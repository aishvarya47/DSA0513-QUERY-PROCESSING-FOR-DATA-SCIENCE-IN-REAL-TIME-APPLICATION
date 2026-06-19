import pandas as pd

df = pd.DataFrame({
    'Name':['Alex','Amy','Allen','Alice','Tom']
})

result = df['Name'].str.find('Al')

print(result)
