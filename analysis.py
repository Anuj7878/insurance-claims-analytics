import pandas as pd


policy = pd.read_csv("policy_sales_data.csv")
claims = pd.read_csv("claims_data.csv")

print("Policy Dataset Shape:", policy.shape)
print("Claims Dataset Shape:", claims.shape)


policy["Policy_Purchase_Date"] = pd.to_datetime(policy["Policy_Purchase_Date"], errors="coerce")
policy["Policy_Start_Date"] = pd.to_datetime(policy["Policy_Start_Date"], errors="coerce")
policy["Policy_End_Date"] = pd.to_datetime(policy["Policy_End_Date"], errors="coerce")


claims["Claim_Date"] = pd.to_datetime(claims["Claim_Date"], errors="coerce")
total_premium = policy["Premium"].sum()

print("Total Premium Collected in 2024:")
print(total_premium)

claims["Year"] = claims["Claim_Date"].dt.year
claims["Month"] = claims["Claim_Date"].dt.month


claims_summary = claims.groupby(["Year","Month"])["Claim_Amount"].sum()

print("\nClaim Cost by Year and Month:")
print(claims_summary)


merged = claims.merge(policy, on=["Customer_ID","Vehicle_ID"])
ratio_tenure = merged.groupby("Policy_Tenure").agg(
    total_claim=("Claim_Amount","sum"),
    total_premium=("Premium","sum")
)

ratio_tenure["Loss_Ratio"] = ratio_tenure["total_claim"] / ratio_tenure["total_premium"]

print("\nClaim to Premium Ratio by Tenure:")
print(ratio_tenure)

policy["Purchase_Month"] = policy["Policy_Purchase_Date"].dt.month

merged_month = merged.copy()
merged_month["Purchase_Month"] = merged_month["Policy_Purchase_Date"].dt.month

month_ratio = merged_month.groupby("Purchase_Month").agg(
    claim_cost=("Claim_Amount","sum"),
    premium=("Premium","sum")
)

month_ratio["Loss_Ratio"] = month_ratio["claim_cost"] / month_ratio["premium"]

print("\nLoss Ratio by Purchase Month:")
print(month_ratio)

claimed_vehicle = claims["Vehicle_ID"].nunique()
total_vehicle = policy["Vehicle_ID"].nunique()

remaining = total_vehicle - claimed_vehicle

future_liability = remaining * 10000

print("\nEstimated Future Claim Liability:")
print(future_liability)

policy["Policy_Days"] = policy["Policy_Tenure"] * 365

total_premium = policy["Premium"].sum()
total_days = policy["Policy_Days"].sum()

daily_premium = total_premium / total_days

earned_days = (pd.Timestamp("2026-02-28") - policy["Policy_Start_Date"]).dt.days.clip(lower=0)

earned_premium = (earned_days / policy["Policy_Days"]) * policy["Premium"]

print("\nPremium Earned till Feb 28 2026:")
print(earned_premium.sum())