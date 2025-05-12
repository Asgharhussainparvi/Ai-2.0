import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
file_path = "global_cancer_predictions.csv"
df = pd.read_csv(file_path)

# Streamlit title
st.title("\U0001F30D Global Cancer Data ")
st.write("Analyze cancer incidence, mortality, and risk factors across countries.")

# Sidebar filters
st.sidebar.header("Filter Data")
countries = st.sidebar.multiselect("Select Countries", df["Country"].unique(), default=["United States", "India"])
cancer_types = st.sidebar.multiselect("Select Cancer Types", df["Cancer_Type"].unique(), default=["Lung", "Breast"])
age_groups = st.sidebar.multiselect("Select Age Groups", sorted(df["Age_Group"].unique()), default=sorted(df["Age_Group"].unique())[:2])

# Apply filters
filtered_df = df[df["Country"].isin(countries) & df["Cancer_Type"].isin(cancer_types) & df["Age_Group"].isin(age_groups)]

# Show dataset preview
if st.button("Show Filtered Data Preview"):
    st.subheader("Filtered Data Preview")
    st.write(filtered_df.head())

# Line Chart: Incidence & Mortality Trends
if st.button("Show Incidence & Mortality Trends"):
    st.subheader("Cancer Incidence & Mortality Trends")
    fig = px.line(filtered_df, x="Age_Group", y=["Incidence", "Mortality"], color="Cancer_Type", markers=True, title="Incidence & Mortality by Age Group")
    st.plotly_chart(fig)

# Bar Chart: Prevalence of Cancer Types
if st.button("Show Prevalence Across Cancer Types"):
    st.subheader("Prevalence Across Cancer Types")
    fig2 = px.bar(filtered_df, x="Cancer_Type", y="Prevalence", color="Country", barmode="group", title="Prevalence by Cancer Type")
    st.plotly_chart(fig2)

# Box Plot: Incidence & Mortality Distribution
if st.button("Show Box Plot"):
    st.subheader("Box Plot: Incidence & Mortality by Age Group")
    fig_box = px.box(filtered_df, x="Age_Group", y="Incidence", color="Cancer_Type", title="Incidence Distribution by Age Group")
    st.plotly_chart(fig_box)

# Scatter Plot: Incidence vs. Mortality
if st.button("Show Scatter Plot"):
    st.subheader("Scatter Plot: Incidence vs Mortality")
    fig_scatter = px.scatter(filtered_df, x="Incidence", y="Mortality", color="Cancer_Type", size="Prevalence", 
                             hover_data=["Country"], title="Incidence vs Mortality")
    st.plotly_chart(fig_scatter)

# Bar Plot: Cancer Cases by Country
if st.button("Show Bar Plot"):
    st.subheader("Bar Plot: Cancer Cases by Country")
    fig_bar = px.bar(filtered_df, x="Country", y="Incidence", color="Cancer_Type", 
                     barmode="group", title="Incidence by Country and Cancer Type")
    st.plotly_chart(fig_bar)

# Histogram: Age Distribution of Cancer Cases
if st.button("Show Histogram"):
    st.subheader("Histogram: Age Distribution of Cancer Cases")
    fig_hist = px.histogram(filtered_df, x="Age_Group", y="Incidence", color="Cancer_Type", 
                            barmode="group", title="Cancer Incidence by Age Group")
    st.plotly_chart(fig_hist)

st.write("Dashboard created with Streamlit & Plotly ✨")
