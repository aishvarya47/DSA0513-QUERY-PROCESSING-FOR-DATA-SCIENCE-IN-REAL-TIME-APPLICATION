import pandas as pd

data = {
    'Item':['Television','Home Theater','Television','Cell Phone'],
    'Units':[95,50,36,27]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(
    df,
    values='Units',
    index='Item',
    aggfunc='sum'
)

print(pivot)
