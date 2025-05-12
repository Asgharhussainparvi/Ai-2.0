import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# --- Page Config ---
st.set_page_config(page_title="Cancer Insights Dashboard", page_icon="🎗", layout="wide")

# --- Load Data ---
file_path = "global_cancer_predictions_reduced.csv"
df = pd.read_csv(file_path)

# Ensure 'Year' column exists if necessary
df["Year"] = pd.to_numeric(df.get("Year", pd.Series()), errors='coerce')

# --- Sidebar ---
with st.sidebar:
    st.title("🎗 **Cancer Dashboard**")
    st.markdown("🚀 **Deep Analysis of Cancer Trends**")
    
    # Sidebar Filters
    selected_countries = st.multiselect("🌍 **Select Countries**", df["Country"].unique(), default=[df["Country"].unique()[0]])
    selected_age_groups = st.multiselect("🧑‍⚕️ **Select Age Groups**", df["Age_Group"].unique(), default=df["Age_Group"].unique()[:3])
    selected_cancer_types = st.multiselect("🎗 **Select Cancer Types**", df["Cancer_Type"].unique(), default=[df["Cancer_Type"].unique()[0]])
    
    # Apply Filters
    filtered_df = df[
        (df["Country"].isin(selected_countries)) &
        (df["Age_Group"].isin(selected_age_groups)) &
        (df["Cancer_Type"].isin(selected_cancer_types))
    ]
    
    # --- Navigation ---
    st.markdown("---")
    selected_page = st.radio("🔹 **Navigate**", ["Home", "Overview", "Graphs", "Trends", "Heatmaps", "Data View", "Death Rate Analysis"])

# --- Home ---
if selected_page == "Home":
    st.title("🎗 **Cancer Insights Dashboard**")
    st.markdown("""
    Welcome to the Cancer Insights Dashboard! This interactive dashboard provides a deep analysis of global cancer trends, 
    allowing you to explore key statistics and visualizations. Use the navigation buttons to access different sections of the dashboard.
    """)
    st.image("cancer.jpg", caption="Cancer Awareness")

# --- Overview ---
if selected_page == "Overview":
    st.title("📊 **Global Cancer Overview**")
    st.markdown("### 🔍 **Explore key trends & statistics**")

    # --- Summary Cards ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📌 Total Cases", f"{filtered_df['Incidence'].sum():,.0f}")
    col2.metric("⚰️ Total Deaths", f"{filtered_df['Mortality'].sum():,.0f}")
    col3.metric("📉 Mortality Rate", f"{(filtered_df['Mortality'].sum()/filtered_df['Incidence'].sum())*100:.2f}%")
    col4.metric("💡 Avg. Life Expectancy", f"{filtered_df['Life_Expectancy'].mean():.1f} Years")

# --- Graphs ---
if selected_page == "Graphs":
    st.title("**Data Visualizations**")
    
    # Graph Selection
    chart_type = st.radio("**Select Chart Type**", ["Pie Chart", "Histogram", "Bar Chart", "Line Chart", "Scatter Plot", "Box Plot", "Heatmap", "Annotated Line Plot"], horizontal=True)
    
    # Grouping Option
    group_by_options = ["Cancer_Type", "Country", "Age_Group"]
    group_by = st.selectbox("🔹 **Group Data By**", group_by_options)

    available_columns = ["Incidence", "Mortality", "Prevalence", "Life_Expectancy", "Urban_Population", "Health_Expenditure_%GDP", "Tobacco_Use_%", "Alcohol_Consumption_Liters", "Physical_Activity_%", "Obesity_%"]

    if chart_type == "Pie Chart":
        st.write("📌 **Pie Chart**")
        pie_column = st.selectbox("Select Column", available_columns)
        fig = px.pie(filtered_df, names=group_by, values=pie_column, title=f"📊 Distribution of {pie_column}")
        st.plotly_chart(fig)

    elif chart_type == "Histogram":
        st.write("📌 **Histogram**")
        hist_column = st.selectbox("Select Column", available_columns)
        fig = px.histogram(filtered_df, x=hist_column, title=f"📊 Distribution of {hist_column}", nbins=20)
        st.plotly_chart(fig)

    elif chart_type == "Scatter Plot":
        st.write("📌 **Scatter Plot**")
        x_axis = st.selectbox("Select X-axis", available_columns, index=0)
        y_axis = st.selectbox("Select Y-axis", available_columns, index=1)
        fig = px.scatter(filtered_df, x=x_axis, y=y_axis, color=group_by, title=f"📊 {x_axis} vs {y_axis}", width=800, height=500)
        st.plotly_chart(fig)

    elif chart_type == "Annotated Line Plot":
        st.write("📌 **Annotated Line Plot**")
        line_column = st.selectbox("Select Column", available_columns)
        fig = px.line(filtered_df, x="Year", y=line_column, color=group_by, title=f"📊 {line_column} Trends Over Time")
        fig.update_traces(mode="lines+markers")
        for i, row in filtered_df.iterrows():
            fig.add_annotation(x=row["Year"], y=row[line_column], text=str(row[line_column]), showarrow=True, arrowhead=2)
        st.plotly_chart(fig)

    elif chart_type == "Bar Chart":
        st.write("📌 **Bar Chart**")
        bar_column = st.selectbox("Select Column", available_columns)
        fig = px.bar(filtered_df, x=group_by, y=bar_column, title=f"📊 {bar_column} by {group_by}", color=group_by)
        st.plotly_chart(fig)

    elif chart_type == "Box Plot":
        st.write("📌 **Box Plot**")
        box_column = st.selectbox("Select Column", available_columns)
        fig = px.box(filtered_df, x=group_by, y=box_column, title=f"📊 Distribution of {box_column} by {group_by}")
        st.plotly_chart(fig)

    elif chart_type == "Heatmap":
        st.write("📌 **Heatmap of Correlations**")
        correlation_matrix = filtered_df[available_columns].corr()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
        st.pyplot(fig)

# --- Trends ---
if selected_page == "Trends":
    st.title("📈 ...")
