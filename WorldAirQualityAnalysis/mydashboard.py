import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)
path = 'global air pollution dataset.csv'
df = load_data(path)

# Preprocessing
df.dropna(inplace=True)  # Drop rows with missing values

# Set the title of the dashboard
st.title('Global Air Pollution Analysis')



# Add an image
st.sidebar.image('1.jpg')

# Sidebar for user inputs
st.sidebar.header("Filters")
selected_country = st.sidebar.selectbox("Select Country", df['Country'].unique())
filtered_df = df[df['Country'] == selected_country]

# Navigation menu
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Global Map","Distibution Data", "Cities with Highest Value","Comparison Data","AQI Categories", "Filtered Data" ])
                                       

# Global Map Page
if page == "Global Map":
    # Plotly global map visualization
    fig_map = px.scatter_geo(df, locations="Country", locationmode='country names', color="AQI Category",
                             hover_name="City", size="AQI Value",
                             projection="natural earth", title='Global Air Pollution Map')
    st.plotly_chart(fig_map)


elif page == "Distibution Data":
    subpage = st.selectbox("Select one", ["AQI Value Distribution",
                                   "CO AQI Value Distribution", "Ozone AQI Value Distribution",
                                     "NO2 AQI Value Distribution", "PM2.5 AQI Value Distribution"])
    # AQI Value Distribution Page
    if subpage == "AQI Value Distribution":
        
        
        # Plotly visualization
        st.subheader('AQI Value Distribution')
        fig_plotly = px.histogram(df, x='AQI Value', nbins=20, title='AQI Value Distribution')
        st.plotly_chart(fig_plotly)

    # CO AQI Value Distribution Page
    elif subpage == "CO AQI Value Distribution":
        
        
        # Plotly visualization
        st.subheader('CO AQI Value Distribution')
        fig_plotly = px.histogram(df, x='CO AQI Value', nbins=20, title='CO AQI Value Distribution')
        st.plotly_chart(fig_plotly)

    # Ozone AQI Value Distribution Page
    elif subpage == "Ozone AQI Value Distribution":
        
        # Plotly visualization
        st.subheader('Ozone AQI Value Distribution')
        fig_plotly = px.histogram(df, x='Ozone AQI Value', nbins=20, title='Ozone AQI Value Distribution')
        st.plotly_chart(fig_plotly)

    # NO2 AQI Value Distribution Page
    elif subpage == "NO2 AQI Value Distribution":

        # Plotly visualization
        st.subheader('NO2 AQI Value Distribution')
        fig_plotly = px.histogram(df, x='NO2 AQI Value', nbins=20, title='NO2 AQI Value Distribution')
        st.plotly_chart(fig_plotly)

    # PM2.5 AQI Value Distribution Page
    elif subpage == "PM2.5 AQI Value Distribution":
        # Plotly visualization
        st.subheader('PM2.5 AQI Value Distribution')
        fig_plotly = px.histogram(df, x='PM2.5 AQI Value', nbins=20, title='PM2.5 AQI Value Distribution')
        st.plotly_chart(fig_plotly)

elif page == "Cities with Highest Value":
    subpage = st.selectbox("Select one", ['Top Cities with Highest AQI Value', 'Top Cities with Highest PM2.5','Top Cities with Highest CO', 'Top Cities with Highest Ozone', 'Top Cities with Highest NO2'])

    if subpage == 'Top Cities with Highest AQI Value':
        st.header("Top 10 Cities with Highest AQI Value")
        top_cities = filtered_df.nlargest(10, "AQI Value")[["City", "AQI Value"]]
        fig, ax = plt.subplots()
        sns.barplot(x=top_cities["AQI Value"], y=top_cities["City"], palette="viridis", ax=ax)
        ax.set_title("Top 10 Cities with Highest AQI Value")
        st.pyplot(fig)
    
    elif subpage == 'Top Cities with Highest PM2.5':
        st.header("Top 10 Cities with Highest PM2.5")
        top_cities = filtered_df.nlargest(10, "PM2.5 AQI Value")[["City", "PM2.5 AQI Value"]]
        fig, ax = plt.subplots()
        sns.barplot(x=top_cities["PM2.5 AQI Value"], y=top_cities["City"], palette="viridis", ax=ax)
        ax.set_title("Top 10 Cities with Highest PM2.5")
        st.pyplot(fig)
    
    elif subpage == 'Top Cities with Highest CO':
        st.header("Top 10 Cities with Highest CO")
        top_cities = filtered_df.nlargest(10, "CO AQI Value")[["City", "CO AQI Value"]]
        fig, ax = plt.subplots()
        sns.barplot(x=top_cities["CO AQI Value"], y=top_cities["City"], palette="viridis", ax=ax)
        ax.set_title("Top 10 Cities with Highest CO")
        st.pyplot(fig)

    elif subpage == 'Top Cities with Highest Ozone':
        st.header("Top 10 Cities with Highest Ozone")
        top_cities = filtered_df.nlargest(10, "Ozone AQI Value")[["City", "Ozone AQI Value"]]
        fig, ax = plt.subplots()
        sns.barplot(x=top_cities["Ozone AQI Value"], y=top_cities["City"], palette="viridis", ax=ax)
        ax.set_title("Top 10 Cities with Highest Ozone")
        st.pyplot(fig)

    elif subpage == 'Top Cities with Highest NO2':
        st.header("Top 10 Cities with Highest NO2")
        top_cities = filtered_df.nlargest(10, "NO2 AQI Value")[["City", "NO2 AQI Value"]]
        fig, ax = plt.subplots()
        sns.barplot(x=top_cities["NO2 AQI Value"], y=top_cities["City"], palette="viridis", ax=ax)
        ax.set_title("Top 10 Cities with Highest NO2")
        st.pyplot(fig)
elif page == "Comparison Data":
    subpage = st.selectbox("Select one", ["Comparison: AQI Value by Country", "Comparison: PM2.5 by Country", "Comparison: CO by Country", "Comparison: Ozone by Country", "Comparison: NO2 by Country"])
    # Comparison: AQI Value by Country Page
    if subpage == "Comparison: AQI Value by Country":
        countries = df['Country'].unique()

        selected_countries = st.multiselect(
            'Select Random countries to compare:',
            options=countries 
        )

        filtered_df = df[df['Country'].isin(selected_countries)]
        fig_plotly = px.bar(filtered_df, x='Country', y='AQI Value', title='Comparison: AQI Value by Country')
        st.plotly_chart(fig_plotly)
    
    # Comparison: PM2.5 by Country Page
    elif subpage == "Comparison: PM2.5 by Country":
        
        countries = df['Country'].unique()

        selected_countries = st.multiselect(
            'Select two countries to compare:',
            options=countries 
        )

        filtered_df = df[df['Country'].isin(selected_countries)]
        fig_plotly = px.bar(filtered_df, x='Country', y='PM2.5 AQI Value', title='Comparison: PM2.5 by Country')
        st.plotly_chart(fig_plotly)


    # Comparison: CO by Country Page
    elif subpage == "Comparison: CO by Country":
        
        # Plotly visualization
        st.subheader('Comparison: CO by Country')
        fig_plotly = px.bar(df, x='Country', y='CO AQI Value', title='Comparison: CO by Country')
        st.plotly_chart(fig_plotly)

    # Comparison: Ozone by Country Page
    elif subpage == "Comparison: Ozone by Country":
        
        # Plotly visualization
        st.subheader('Comparison: Ozone by Country')
        fig_plotly = px.bar(df, x='Country', y='Ozone AQI Value', title='Comparison: Ozone by Country')
        st.plotly_chart(fig_plotly)
    
    # Comparison: NO2 by Country Page
    elif subpage == "Comparison: NO2 by Country":
        
        # Plotly visualization
        st.subheader('Comparison: NO2 by Country')
        fig_plotly = px.bar(df, x='Country', y='NO2 AQI Value', title='Comparison: NO2 by Country')
        st.plotly_chart(fig_plotly)

# AQI Categories Page
elif page == "AQI Categories":
    st.header(f"AQI Categories for {selected_country}")
    
    # Plotly visualization
    st.subheader('AQI Categories')
    fig_plotly = px.bar(filtered_df, x='City', y='AQI Value', color='AQI Category', title=f'AQI Categories for {selected_country}')
    st.plotly_chart(fig_plotly)


# Filtered Data Page
elif page == "Filtered Data":
    st.header(f"Data for {selected_country}")
    st.write(filtered_df)
