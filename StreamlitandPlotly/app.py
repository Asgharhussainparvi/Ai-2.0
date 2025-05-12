import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px 
import time as t





st.sidebar.header("Next Page")
bar = st.sidebar.selectbox('Pages',[1,2,3,4,5])
if bar == 1:
    st.title('My Dashboard')
    st.header("Python Code")
    st.subheader("My first file")
    st.write("I am a Software Engineering Student.")

    df = pd.DataFrame({
        'a1': np.arange(10),
        'a2': np.random.randn(10)
        })
    st.table(df)
    st.header("Line Plot")
    fg = px.line(df,x='a1',y='a2',title="Line Plot")
    st.line_chart(fg)
    st.header("Scatter Plot")
    fg = px.line(df,x='a1',y='a2',title="Scatter Plot")
    st.bar_chart(fg)


elif bar == 2:
    st.header('Page 2')
    st.image("1.jpg",caption="Cartoon")
    st.video('1.mp4')
    st.radio('What is your Favourite Movie?',['Taar e Zameen pr','3 Idiots','Zero'])
    st.audio('1.mp3')
elif bar == 3:
    st.header('Page 3')
    st.selectbox('What is your Favourite Movie?',['Taar e Zameen pr','3 Idiots','Zero'])
    st.multiselect('What is your Favourite Movie?',['Taar e Zameen pr','3 Idiots','Zero'])
    st.checkbox('Human')
elif bar == 4:
    st.header('Page 4')
    txt = st.text_area('Write 500 words paragraph:')
    st.write('Your Text\n',txt)
    num = st.number_input("Write the numberes here :",max_value=200,min_value=0)
    st.write('Your Number\n',num)
elif bar == 5:
    st.header('Page 5')
    
    
    file = st.file_uploader('Uploaded !',type='csv')
    if file:
        st.write("File uploaded succesfully!")

    st.slider('Select year range',0,15)
    b = st.button(label="BUTTON")
    if b:
        st.write("Pressed!")
    bar = st.sidebar.selectbox('Gender?',['Male','Female'])

    if bar == 'Male':
        st.title("Male's Page")
        st.write("You are Male")
    elif bar == 'Female':
        st.title("Female's Page")
        st.write("You are Female")

    
    