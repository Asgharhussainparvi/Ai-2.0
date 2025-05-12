import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Set page title and layout
st.set_page_config(page_title="World Air Quality Analysis", layout="wide")




# Title
st.title("    World Air Quality Analysis")
st.write("                              Explore air quality data across continent, countries, and cities")

# Load and preprocess data
@st.cache_data
def load_data():
    # Synthetic data generation for demonstration
    np.random.seed(42)
    num_rows = 1000
    data = pd.read_excel('air.xls')
    return data

data = load_data()

# Sidebar
st.sidebar.image('1.jpg')
st.sidebar.header("Filters")

# Continent filter
selected_continent = st.sidebar.selectbox("Select Continent", data["Continent"].unique())

# Country filter (based on selected continent)
country_options = data[data["Continent"] == selected_continent]["Country"].unique()
selected_country = st.sidebar.selectbox("Select Country", country_options)



# City filter (based on selected region)
city_options = data[
    (data["Continent"] == selected_continent) &
    (data["Country"] == selected_country) 
]["City/station"].unique()


# Filter data based on selections in sidebar
filtered_data = data[
    (data["Continent"] == selected_continent) &
    (data["Country"] == selected_country) 
]



# Interactive plots
selected_plot = st.selectbox("Select Visualization", [
    "Basic Statistics", "PM2.5 Distribution", "PM10 Distribution", 
    "Top 10 Cities with Highest PM2.5", 
    "Top 10 Cities with Highest PM10", "Temporal Coverage Analysis", 
    "Comparison: PM2.5 Distribution by Country", "Comparison: PM10 Distribution by Country",
    "Box Plot: PM2.5 Distribution by Continent"
])


# Display raw data
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)

# Display filtered data
elif st.sidebar.checkbox("Show Filtered Data"):
    st.subheader("Filtered Data")
    st.write(filtered_data)

elif selected_plot == "Basic Statistics":
    st.header("Basic Statistics")
    st.write(filtered_data[["PM10", "PM 2.5"]].describe())

elif selected_plot == "PM2.5 Distribution":
    st.subheader("PM2.5 Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data["PM 2.5"].dropna(),bins=10, kde=True, ax=ax)
    ax.set_title("PM 2.5 Distribution")
    st.pyplot(fig)

elif selected_plot == 'PM10 Distribution':
    st.header("PM10 Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data["PM10"].dropna(),bins=10, kde=True, ax=ax)
    ax.set_title("PM10 Distribution")
    st.pyplot(fig)


elif selected_plot == 'Scatter Plot: PM2.5 vs PM10':
    st.header("PM 2.5 vs PM10 Scatter Plot")
    fig, ax = plt.subplots()
    sns.scatterplot(x=filtered_data["PM 2.5"], y=filtered_data["PM10"], ax=ax)
    ax.set_title("PM2.5 vs PM10")
    st.pyplot(fig)

elif selected_plot == 'Top 10 Cities with Highest PM2.5':
    st.header("Top 10 Cities with Highest PM2.5")
    top_cities = filtered_data.nlargest(10, "PM 2.5")[["City/station", "PM 2.5"]]
    fig, ax = plt.subplots()
    sns.barplot(x=top_cities["PM 2.5"], y=top_cities["City/station"], palette="viridis", ax=ax)
    ax.set_title("Top 10 Cities with Highest PM 2.5")
    st.pyplot(fig)

elif selected_plot == 'Top 10 Cities with Highest PM10':
    st.header("Top 10 Cities with Highest PM10")
    top_cities = filtered_data.nlargest(10, "PM10")[["City/station", "PM10"]]
    fig, ax = plt.subplots()
    sns.barplot(x=top_cities["PM10"], y=top_cities["City/station"], palette="viridis", ax=ax)
    ax.set_title("Top 10 Cities with Highest PM10")
    st.pyplot(fig)

elif selected_plot == 'Temporal Coverage Analysis':
    st.header("Temporal Coverage Analysis")
    temporal_coverage = filtered_data["Temporal coverage"].value_counts()
    st.write(temporal_coverage)
    fig, ax = plt.subplots()
    sns.barplot(x=temporal_coverage.index, y=temporal_coverage.values, palette="magma", ax=ax)
    ax.set_title("Temporal Coverage of Monitoring Stations")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

elif selected_plot == 'Box Plot: PM2.5 Distribution by Continent':
    st.header("Box Plot: PM2.5 Distribution by Continent")
    
    # Plot
    fig, ax = plt.subplots()
    sns.boxplot(x=filtered_data["Continent"], y=filtered_data["PM 2.5"], palette="viridis", ax=ax)
    ax.set_title("PM2.5 Distribution by Continent")
    ax.set_xlabel("Continent")
    ax.set_ylabel("PM2.5 Concentration (µg/m³)")
    st.pyplot(fig)

elif selected_plot == 'Comparison: PM2.5 Distribution by Country':
    st.header("Comparison: PM2.5 Distribution by Country")
    country1 = st.selectbox("Select First Country", data["Country"].unique())
    country2 = st.selectbox("Select Second Country", data["Country"].unique())
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    sns.histplot(data[data["Country"] == country1]["PM 2.5"].dropna(),bins=10, kde=True, ax=ax[0])
    ax[0].set_title(f"PM2.5 Distribution in {country1}")
    sns.histplot(data[data["Country"] == country2]["PM 2.5"].dropna(), bins=10,kde=True, ax=ax[1])
    ax[1].set_title(f"PM2.5 Distribution in {country2}")
    st.pyplot(fig)

elif selected_plot == 'Comparison: PM10 Distribution by Country':
    st.header("Comparison: PM10 Distribution by Country")
    country1 = st.selectbox("Select First Country", data["Country"].unique())
    country2 = st.selectbox("Select Second Country", data["Country"].unique())
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    sns.histplot(data[data["Country"] == country1]["PM10"].dropna(),bins=10, kde=True, ax=ax[0])
    ax[0].set_title(f"PM10 Distribution in {country1}")
    sns.histplot(data[data["Country"] == country2]["PM10"].dropna(),bins=10, kde=True, ax=ax[1])
    ax[1].set_title(f"PM10 Distribution in {country2}")
    st.pyplot(fig)