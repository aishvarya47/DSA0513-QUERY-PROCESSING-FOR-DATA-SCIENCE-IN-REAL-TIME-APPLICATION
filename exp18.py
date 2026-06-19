import pandas as pd

student_data = {
    'school_code':['s001','s001','s002','s002','s001'],
    'class':['V','VI','V','VI','V'],
    'name':['Alex','Amy','Allen','Alice','Tom']
}

df = pd.DataFrame(student_data)

grouped = df.groupby(
    ['school_code','class']
)

for name, group in grouped:
    print("\nGroup:", name)
    print(group)
