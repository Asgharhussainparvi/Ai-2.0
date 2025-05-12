import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
file_path = 'Pakistan economy and GDP Sectors.csv'
df = pd.read_csv(file_path)

# Preprocessing
df.dropna(inplace=True)  # Drop rows with missing values

# Set the title of the dashboard
st.title('Pakistan Economy and GDP Sectors Dashboard')

# Sidebar for user inputs
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Select Year", df['Year'].unique())
filtered_df = df[df['Year'] == selected_year]

# Navigation menu
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Raw Data", "Filtered Data", "GDP Sectors by Year", "Income Per Capita Distribution","Manufacturing Comparison"])

# Raw Data Page
if page == "Raw Data":
    st.header("Raw Data")
    st.write(df)

# Filtered Data Page
elif page == "Filtered Data":
    st.header(f"Data for the Year {selected_year}")
    st.write(filtered_df)

# GDP Sectors by Year Page
elif page == "GDP Sectors by Year":
    st.header('GDP Sectors by Year')
    
    # Matplotlib visualization
    st.subheader('GDP Sectors by Year')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Year', y='GDP Current Prices', data=df, ax=ax)
    ax.set_title('GDP Current Prices by Year')
    st.pyplot(fig)
    
    # Plotly visualization
    st.subheader('GDP Sectors by Year ')
    fig_plotly = px.bar(df, x='Year', y='GDP Current Prices', title='GDP Current Prices by Year')
    st.plotly_chart(fig_plotly)
    
    # NumPy operation
    mean_gdp = np.mean(df['GDP Current Prices'])
    st.write(f'Mean GDP Current Prices: {mean_gdp}')

# Income Per Capita Distribution Page
elif page == "Income Per Capita Distribution":
    st.header('Income Per Capita Distribution')
    
    # Matplotlib visualization
    st.subheader('Income Per Capita Distribution ')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['Income Per Capita'], bins=10, kde=True, ax=ax)
    ax.set_title('Income Per Capita Distribution')
    st.pyplot(fig)
    
    # Plotly visualization
    st.subheader('Income Per Capita Distribution')
    fig_plotly_hist = px.histogram(df, x='Income Per Capita', nbins=10, title='Income Per Capita Distribution')
    st.plotly_chart(fig_plotly_hist)
# Manufacturing Comparison Page
elif page == "Manufacturing Comparison":
    st.header('Comparison of Small Scale and Large Scale Manufacturing')
    
    # Matplotlib visualization
    st.subheader('Manufacturing Comparison ')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Year'], df['Small Scale Manufacturing'], label='Small Scale Manufacturing', marker='o')
    ax.plot(df['Year'], df['Large Scale Manufacturing'], label='Large Scale Manufacturing', marker='o')
    ax.set_title('Small Scale vs Large Scale Manufacturing')
    ax.set_xlabel('Year')
    ax.set_ylabel('Manufacturing Value')
    ax.legend()
    st.pyplot(fig)
    
    # Plotly visualization
    st.subheader('Manufacturing Comparison')
    fig_plotly_comp = px.line(df, x='Year', y=['Small Scale Manufacturing', 'Large Scale Manufacturing'], 
                              labels={'value': 'Manufacturing Value', 'variable': 'Manufacturing Type'},
                              title='Small Scale vs Large Scale Manufacturing')
    st.plotly_chart(fig_plotly_comp)

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

# Add an image
st.image('1.jpg', caption='Pakistan Economy Image')