from email import policy

import pandas as pd
import numpy as np

num_customers = 1000000

tenures = np.random.choice(
    [1,2,3,4],
    size=num_customers,
    p=[0.2,0.3,0.4,0.1]
)

dates = pd.date_range(start="2024-01-01", end="2024-12-31")
purchase_dates = np.random.choice(dates, num_customers)

df = pd.DataFrame({
    "Customer_ID": range(1, num_customers + 1),
    "Vehicle_ID": range(1000001, 1000001 + num_customers),
    "Vehicle_Value": 100000,
    "Policy_Tenure": tenures,
    "Policy_Purchase_Date": purchase_dates
})

df["Premium"] = df["Policy_Tenure"] * 100

df["Policy_Start_Date"] = df["Policy_Purchase_Date"] + pd.Timedelta(days=365)

df["Policy_End_Date"] = df["Policy_Start_Date"] + pd.to_timedelta(df["Policy_Tenure"]*365, unit='D')

df.to_csv("policy_sales_data.csv", index=False)

print("Policy dataset generated successfully!")

print("Policy Dataset Shape:", policy.shape)