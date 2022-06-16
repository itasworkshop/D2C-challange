import pandas as pd
from pathlib import Path
import json

# path to file
p = Path(r'C:\Development\D2C-challange\d2c-app\resources\test.json')

# read json
with p.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())

# create dataframe
print(data)
df = pd.json_normalize(data, record_path='hits', meta=["start_date_date","source","campaign","medium","device","channel_grouping","session_id"])

ndf = df[df.columns[::-1]]

ndf.to_csv(r'C:\Development\D2C-challange\d2c-app\resources\output.csv', encoding='utf-8')