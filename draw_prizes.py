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
    fetch_time = datetime.now().replace(microsecond=0)
    for customer_id in draw["set1"]:
        rows.append({"week": week, "prize": 1, "customer_id": customer_id,
                     "fetch_time": fetch_time})
    for customer_id in draw["set2"]:
        rows.append({"week": week, "prize": 2, "customer_id": customer_id,
                     "fetch_time": fetch_time})

# HERE WE NEED A PANDAS DATA FRAME, df, WITH ONE ROW PER WINNER IN THE LIST rows
df.to_csv("test_dataframe.csv", index=False)
print(df)
