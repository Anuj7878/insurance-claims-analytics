import pandas as pd
import numpy as np

df = pd.read_csv("policy_sales_data.csv")

vehicle_value = 100000
claim_amount = vehicle_value * 0.10


df["purchase_day"] = pd.to_datetime(df["Policy_Purchase_Date"]).dt.day

eligible = df[df["purchase_day"].isin([7,14,21,28])]

claims_2025 = eligible.sample(frac=0.30, random_state=42)

claims_2025_data = pd.DataFrame({
    "Claim_ID": range(1, len(claims_2025)+1),
    "Customer_ID": claims_2025["Customer_ID"],
    "Vehicle_ID": claims_2025["Vehicle_ID"],
    "Claim_Amount": claim_amount,
    "Claim_Date": claims_2025["Policy_Start_Date"],
    "Claim_Type": 1
})


four_year = df[df["Policy_Tenure"] == 4]

claims_2026 = four_year.sample(frac=0.10, random_state=42)

dates_2026 = pd.date_range("2026-01-01", "2026-02-28")

claim_dates = np.random.choice(dates_2026, len(claims_2026))

claims_2026_data = pd.DataFrame({
    "Claim_ID": range(len(claims_2025_data)+1,
                      len(claims_2025_data)+len(claims_2026)+1),
    "Customer_ID": claims_2026["Customer_ID"],
    "Vehicle_ID": claims_2026["Vehicle_ID"],
    "Claim_Amount": claim_amount,
    "Claim_Date": claim_dates,
    "Claim_Type": 2
})

claims_data = pd.concat([claims_2025_data, claims_2026_data])

claims_data.to_csv("claims_data.csv", index=False)

print("Claims dataset generated successfully")