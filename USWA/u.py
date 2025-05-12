import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
file_path = 'Pakistan  Economy AND GDP Contributors.csv'
df = pd.read_csv(file_path, thousands=',', parse_dates=True, dayfirst=True, encoding='latin1', engine='python')  

# Add an image
st.sidebar.image('1.jpg', caption='Pakistan Economy Image')

# Preprocessing
df.dropna(inplace=True)  # Drop rows with missing values

# Set the title of the dashboard
st.title('Pakistan Economy and GDP Contributors')

# Sidebar for user inputs
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Select Year", df['Year'].unique())
filtered_df = df[df['Year'] == selected_year]

# Navigation menu
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Raw Data", "Filtered Data", "GDP Contributors", "Agricultural Sectors", "Industrial Sectors", "Services Sectors", "Global Map"])

# Raw Data Page
if page == "Raw Data":
    st.header("Raw Data")
    st.write(df)

# Filtered Data Page
elif page == "Filtered Data":
    st.header(f"Data for the Year {selected_year}")
    st.write(filtered_df)

# GDP Contributors Page
elif page == "GDP Contributors":
    st.header('GDP Contributors')
    
    # Plotly visualization
    st.subheader('GDP Contributors (Plotly)')
    fig_plotly = px.bar(df, x='Year', y=['GDP', 'Per Capita'], title='GDP and Per Capita Over the Years')
    st.plotly_chart(fig_plotly)
    
    # Matplotlib visualization
    st.subheader('GDP Contributors (Matplotlib)')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Year'], df['GDP'], label='GDP', marker='o')
    ax.plot(df['Year'], df['Per Capita'], label='Per Capita', marker='o')
    ax.set_title('GDP and Per Capita Over the Years')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.legend()
    st.pyplot(fig)

# Agricultural Sectors Page
elif page == "Agricultural Sectors":
    st.header('Agricultural Sectors')
    
    # Plotly visualization
    st.subheader('Agricultural Sectors (Plotly)')
    fig_plotly = px.bar(df, x='Year', y=['Crops', 'Livestock', 'Forestry', 'Fishing'], title='Agricultural Sectors Over the Years')
    st.plotly_chart(fig_plotly)
    
    # Matplotlib visualization
    st.subheader('Agricultural Sectors (Matplotlib)')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Year'], df['Crops'], label='Crops', marker='o')
    ax.plot(df['Year'], df['Livestock'], label='Livestock', marker='o')
    ax.plot(df['Year'], df['Forestry'], label='Forestry', marker='o')
    ax.plot(df['Year'], df['Fishing'], label='Fishing', marker='o')
    ax.set_title('Agricultural Sectors Over the Years')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.legend()
    st.pyplot(fig)

# Industrial Sectors Page
elif page == "Industrial Sectors":
    st.header('Industrial Sectors')
    
    # Plotly visualization
    st.subheader('Industrial Sectors (Plotly)')
    fig_plotly = px.bar(df, x='Year', y=['Mining and Quarrying', 'Manufacturing', 'Large Scale', 'Small Scale', 'Slaughtering', 'Electricity generation & distribution and Gas distribution', 'Construction'], title='Industrial Sectors Over the Years')
    st.plotly_chart(fig_plotly)
    
    # Matplotlib visualization
    st.subheader('Industrial Sectors (Matplotlib)')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Year'], df['Mining and Quarrying'], label='Mining and Quarrying', marker='o')
    ax.plot(df['Year'], df['Manufacturing'], label='Manufacturing', marker='o')
    ax.plot(df['Year'], df['Large Scale'], label='Large Scale', marker='o')
    ax.plot(df['Year'], df['Small Scale'], label='Small Scale', marker='o')
    ax.plot(df['Year'], df['Slaughtering'], label='Slaughtering', marker='o')
    ax.plot(df['Year'], df['Electricity generation & distribution and Gas distribution'], label='Electricity generation & distribution and Gas distribution', marker='o')
    ax.plot(df['Year'], df['Construction'], label='Construction', marker='o')
    ax.set_title('Industrial Sectors Over the Years')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.legend()
    st.pyplot(fig)

# Services Sectors Page
elif page == "Services Sectors":
    st.header('Services Sectors')
    
    # Plotly visualization
    st.subheader('Services Sectors (Plotly)')
    fig_plotly = px.bar(df, x='Year', y=['Wholesale & Retail trade', 'Transport, Storage  & Communication', 'Finance & Insurance', 'Housing Services', 'General Government Services', 'Other  Services'], title='Services Sectors Over the Years')
    st.plotly_chart(fig_plotly)
    
    # Matplotlib visualization
    st.subheader('Services Sectors (Matplotlib)')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Year'], df['Wholesale & Retail trade'], label='Wholesale & Retail trade', marker='o')
    ax.plot(df['Year'], df['Transport, Storage  & Communication'], label='Transport, Storage  & Communication', marker='o')
    ax.plot(df['Year'], df['Finance & Insurance'], label='Finance & Insurance', marker='o')
    ax.plot(df['Year'], df['Housing Services'], label='Housing Services', marker='o')
    ax.plot(df['Year'], df['General Government Services'], label='General Government Services', marker='o')
    ax.plot(df['Year'], df['Other  Services'], label='Other  Services', marker='o')
    ax.set_title('Services Sectors Over the Years')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.legend()
    st.pyplot(fig)

# Global Map Page
elif page == "Global Map":
    st.header('Global Air Pollution Map')
    
    # Plotly global map visualization
    fig_map = px.scatter_geo(df, locations="Country", locationmode='country names', color="AQI Category",
                             hover_name="City", size="AQI Value",
                             projection="natural earth", title='Global Air Pollution Map')
    st.plotly_chart(fig_map)

# Set the background color
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

