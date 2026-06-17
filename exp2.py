import pandas as pd

data = {'EMPLOYEE_ID':[102,101,101,201,114,122,200,176,176,200]}

df = pd.DataFrame(data)

result = df.groupby('EMPLOYEE_ID').size()
print(result[result > 1].index.tolist())
