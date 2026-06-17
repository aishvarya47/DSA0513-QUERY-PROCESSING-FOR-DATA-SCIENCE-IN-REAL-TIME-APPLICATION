import pandas as pd

data = {
    'JOB_ID':['AD_PRES','AD_VP','IT_PROG','SA_MAN'],
    'JOB_TITLE':['President','Administration Vice President',
                 'Programmer','Sales Manager']
}

df = pd.DataFrame(data)

print(df.sort_values(by='JOB_TITLE', ascending=False))
