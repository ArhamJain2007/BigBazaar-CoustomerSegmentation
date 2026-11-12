
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(
    page_title="Big Bazaar Customer Segmentation",
    page_icon="🛒",
    layout="wide"
)

# Load customer data
data = pd.read_csv("Output/Graphs/final_customer_segments.csv")

# Give meaningful names to clusters
data["Segment"] = data["Cluster"].map({
    0: "Low Engagement",
    1: "High Engagement"
})

# Dashboard title
st.title("Big Bazaar Customer Segmentation")
st.write("Customer analysis using K-Means Clustering")

st.divider()

# Main statistics
total_customers = len(data)
total_segments = data["Cluster"].nunique()
average_income = data["annual_income"].mean()
average_spending = data["annual_spending"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", total_customers)
col2.metric("Customer Segments", total_segments)
col3.metric("Average Annual Income", f"₹{average_income:,.0f}")
col4.metric("Average Annual Spending", f"₹{average_spending:,.0f}")

st.divider()

# Customer segment selection
st.subheader("Customer Segment Analysis")

selected_segment = st.selectbox(
    "Select Customer Segment",
    ["All Customers", "Low Engagement", "High Engagement"]
)

if selected_segment == "All Customers":
    filtered_data = data
else:
    filtered_data = data[data["Segment"] == selected_segment]

# Segment statistics
col1, col2, col3 = st.columns(3)

col1.metric("Customers in Selection", len(filtered_data))

col2.metric(
    "Average Spending Score",
    round(filtered_data["spending_score"].mean(), 2)
)

col3.metric(
    "Average Monthly Visits",
    round(filtered_data["visit_frequency"].mean(), 2)
)

# Customer scatter plot
st.subheader("Income vs Spending Score")

fig, ax = plt.subplots(figsize=(9, 5))

for segment in filtered_data["Segment"].unique():

    segment_data = filtered_data[
        filtered_data["Segment"] == segment
    ]

    ax.scatter(
        segment_data["annual_income"],
        segment_data["spending_score"],
        label=segment,
        alpha=0.6
    )

ax.set_xlabel("Annual Income (₹)")
ax.set_ylabel("Spending Score")
ax.set_title("Customer Segmentation")
ax.legend()

st.pyplot(fig)
plt.close(fig)

# Customer distribution
st.subheader("Customer Distribution")

segment_counts = data["Segment"].value_counts()

fig, ax = plt.subplots(figsize=(8, 4))

segment_counts.plot(kind="bar", ax=ax)

ax.set_title("Number of Customers in Each Segment")
ax.set_xlabel("Customer Segment")
ax.set_ylabel("Number of Customers")
ax.tick_params(axis="x", rotation=0)

st.pyplot(fig)
plt.close(fig)

# Customer segment summary
st.subheader("Customer Segment Summary")

summary = data.groupby("Segment").agg({
    "annual_income": "mean",
    "spending_score": "mean",
    "visit_frequency": "mean",
    "average_basket_value": "mean",
    "annual_spending": "mean",
    "days_since_last_visit": "mean"
}).round(2)

st.dataframe(summary, use_container_width=True)

# Marketing recommendations
st.subheader("Marketing Recommendations")

if selected_segment == "Low Engagement":

    st.write("### Low Engagement Customers")

    st.write("1. Offer discounts on frequently purchased products.")
    st.write("2. Provide cashback on selected purchases.")
    st.write("3. Send reminders to customers who have not visited recently.")
    st.write("4. Introduce loyalty points to encourage repeat visits.")
    st.write("5. Offer special weekend shopping deals.")

elif selected_segment == "High Engagement":

    st.write("### High Engagement Customers")

    st.write("1. Provide premium membership benefits.")
    st.write("2. Offer exclusive deals and early access to sales.")
    st.write("3. Recommend products based on previous purchases.")
    st.write("4. Reward customers for frequent purchases.")
    st.write("5. Introduce referral rewards.")

else:

    st.write("### General Marketing Strategies")

    st.write("1. Use targeted promotional campaigns.")
    st.write("2. Introduce customer loyalty programmes.")
    st.write("3. Provide personalized shopping offers.")
    st.write("4. Monitor customer purchase behaviour.")

# Customer records
st.subheader("Customer Records")

st.dataframe(filtered_data, use_container_width=True)

st.success("Customer segmentation dashboard loaded successfully!")
