import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Insurance Claims Analytics Dashboard",
    layout="wide"
)

st.title("Insurance Claims Analytics Dashboard")

monthly_claims = pd.DataFrame({
    "Month": [
        "Jan 2025",
        "Feb 2025",
        "Mar 2025",
        "Apr 2025",
        "May 2025",
        "Jun 2025",
        "Jul 2025",
        "Aug 2025",
        "Sep 2025",
        "Oct 2025",
        "Nov 2025",
        "Dec 2025"
    ],
    "Claim Cost": [
        32980000,
        33830000,
        32300000,
        32610000,
        32490000,
        32950000,
        32260000,
        32360000,
        32390000,
        33040000,
        31970000,
        33520000
    ]
})

claim_types = pd.DataFrame({
    "Claim Type": [
        "Accident",
        "Theft",
        "Fire",
        "Damage"
    ],
    "Count": [
        52,
        20,
        15,
        13
    ]
})

monthly_count = pd.DataFrame({
    "Month": [
        "Jan 2025",
        "Feb 2025",
        "Mar 2025",
        "Apr 2025",
        "May 2025",
        "Jun 2025",
        "Jul 2025",
        "Aug 2025",
        "Sep 2025",
        "Oct 2025",
        "Nov 2025",
        "Dec 2025"
    ],
    "Total Claims": [
        3298,
        3383,
        3230,
        3261,
        3249,
        3295,
        3226,
        3236,
        3239,
        3304,
        3197,
        3352
    ]
})

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Premium",
        "₹240,065,600"
    )

with col2:
    st.metric(
        "Total Claims",
        "₹392,740,000"
    )

with col3:
    st.metric(
        "Loss Ratio",
        "36%"
    )

st.subheader("Monthly Claims Trend")

fig1 = px.line(
    monthly_claims,
    x="Month",
    y="Claim Cost",
    markers=True,
    template="plotly_dark"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.subheader("Claim Type Distribution")

fig2 = px.pie(
    claim_types,
    names="Claim Type",
    values="Count",
    hole=0.5,
    template="plotly_dark"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.subheader("Claims by Month")

fig3 = px.bar(
    monthly_count,
    x="Month",
    y="Total Claims",
    template="plotly_dark"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.subheader("Business Insights")

st.success("Loss ratio decreases as policy tenure increases.")

st.info("4-year policies are the most profitable segment.")

st.warning("Estimated future claim liability is ₹9.51 Billion.")

st.subheader("Portfolio Summary")

summary_df = pd.DataFrame({
    "Metric": [
        "Total Premium",
        "Total Claims",
        "Portfolio Loss Ratio",
        "Future Claim Liability"
    ],
    "Value": [
        "₹240,065,600",
        "₹392,740,000",
        "36%",
        "₹9,511,330,000"
    ]
})

st.dataframe(
    summary_df,
    use_container_width=True
)