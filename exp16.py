import pandas as pd

student_data = {
    'school_code':['s001','s002','s001','s002','s001'],
    'name':['Alex','Amy','Allen','Alice','Tom'],
    'age':[12,13,12,14,13]
}

df = pd.DataFrame(student_data)

grouped = df.groupby('school_code')

print(grouped)
print(type(grouped))
