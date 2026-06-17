import pandas as pd

data = {
    'Region':['East','Central','West'],
    'Manager':['Martha','Hermann','Douglas'],
    'SalesMan':['Alexander','Luis','Michael'],
    'Sale_amt':[113810,43128,38336]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(
    df,
    values='Sale_amt',
    index=['Region','Manager','SalesMan'],
    aggfunc='sum'
)

print(pivot)
