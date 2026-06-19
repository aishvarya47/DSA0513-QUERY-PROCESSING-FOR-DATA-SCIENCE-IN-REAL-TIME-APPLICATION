import pandas as pd
import numpy as np

exam_data = {
'name':['Anastasia','Dima','Katherine','James'],
'score':[12.5,9,16.5,np.nan],
'attempts':[1,3,2,3],
'qualify':['yes','no','yes','no']
}

df = pd.DataFrame(exam_data)

print(df.head(3))
