import pandas as pd

student_data = {
    'school_code':['s001','s002','s001','s002','s001'],
    'age':[12,13,12,14,13]
}

df = pd.DataFrame(student_data)

result = df.groupby('school_code')['age'].agg(
    ['mean','min','max']
)

print(result)
