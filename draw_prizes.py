from datetime import datetime

import pandas as pd
from dotenv import load_dotenv

from api_functions import get_draw

# The key of the course API, from the file .env in this folder
load_dotenv(override=True)

# Draw the winners of each week: one row per winner
weeks = [47, 48]
rows = []
for week in weeks:
    draw = get_draw(week)
    # EACH ROW ALSO NEEDS THE COLUMN fetch_time: THE TIME OF THE REQUEST, WITHOUT MICROSECONDS
    for customer_id in draw["set1"]:
        rows.append({"week": week, "prize": 1, "customer_id": customer_id})
    # THE WINNERS OF PRIZE 2 (THE NUMBERS IN set2) ARE MISSING

df = pd.DataFrame(rows)
df.to_csv("test_dataframe.csv", index=False)
print(df)
