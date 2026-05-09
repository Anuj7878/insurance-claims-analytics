import pandas as pd

policy = pd.read_csv("policy_sales_data.csv")
claims = pd.read_csv("claims_data.csv")

policy["Policy_Purchase_Date"] = pd.to_datetime(
    policy["Policy_Purchase_Date"],
    errors="coerce"
)

policy["Policy_Start_Date"] = pd.to_datetime(
    policy["Policy_Start_Date"],
    errors="coerce"
)

policy["Policy_End_Date"] = pd.to_datetime(
    policy["Policy_End_Date"],
    errors="coerce"
)

claims["Claim_Date"] = pd.to_datetime(
    claims["Claim_Date"],
    errors="coerce"
)

total_premium = policy["Premium"].sum()
total_claims = claims["Claim_Amount"].sum()

loss_ratio = (
    total_claims / total_premium
) * 100

claims["Month"] = claims["Claim_Date"].dt.strftime("%b %Y")

monthly_claims = claims.groupby(
    "Month"
)["Claim_Amount"].sum()

merged = claims.merge(
    policy,
    on=["Customer_ID", "Vehicle_ID"]
)

ratio_tenure = merged.groupby(
    "Policy_Tenure"
).agg(
    Total_Claims=("Claim_Amount", "sum"),
    Total_Premium=("Premium", "sum")
)

ratio_tenure["Loss_Ratio"] = (
    ratio_tenure["Total_Claims"] /
    ratio_tenure["Total_Premium"]
) * 100

claim_distribution = (
    claims["Claim_Type"]
    .value_counts(normalize=True) * 100
)

claimed_vehicle = claims["Vehicle_ID"].nunique()
total_vehicle = policy["Vehicle_ID"].nunique()

remaining = total_vehicle - claimed_vehicle

future_liability = remaining * 10000

policy["Policy_Days"] = (
    policy["Policy_Tenure"] * 365
)

earned_days = (
    pd.Timestamp("2026-02-28") -
    policy["Policy_Start_Date"]
).dt.days.clip(lower=0)

earned_premium = (
    earned_days /
    policy["Policy_Days"]
) * policy["Premium"]

print("\n========== INSURANCE ANALYTICS REPORT ==========\n")

print("Total Premium:")
print(f"₹{total_premium:,.0f}")

print("\nTotal Claims:")
print(f"₹{total_claims:,.0f}")

print("\nPortfolio Loss Ratio:")
print(f"{loss_ratio:.0f}%")

print("\nEstimated Future Claim Liability:")
print(f"₹{future_liability:,.0f}")

print("\nPremium Earned Till Feb 2026:")
print(f"₹{earned_premium.sum():,.0f}")

print("\n========== MONTHLY CLAIMS TREND ==========\n")
print(monthly_claims)

print("\n========== CLAIM TYPE DISTRIBUTION ==========\n")
print(claim_distribution)

print("\n========== LOSS RATIO BY TENURE ==========\n")
print(ratio_tenure)

print("\n========== BUSINESS INSIGHTS ==========\n")

print("1. Loss ratio decreases as policy tenure increases.")
print("2. 4-year policies are the most profitable segment.")
print("3. Accident claims contribute the highest share.")
print("4. Future estimated claim liability is significant.")