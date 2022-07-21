import pandas as pd
import json

with open('Apex_Championship', encoding='utf-8') as file:
    data = file.read()

championship = json.loads(data)
print(championship.keys())