import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("Godstime's and Sons")
st.write("""Hi, I am Ardit! I am a Python programmer, teacher, and founder of PythonHow. I graduated in 2013 with a Master of Science in Geospatial Technologies from the University of Muenster in Germany with a focus on using Python for remote sensing.
I have worked with companies from various countries, such as the Center for Conservation Geography, to map and understand Australian ecosystems, image processing with the Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
    """)
st.subheader("Our Team")

df = pandas.read_csv("data.csv", sep=",")

col1, col2, col3 = st.columns(3)
with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()}{row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"], width=300)

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()}{row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"], width=300)

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f"{row['first name'].title()}{row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"], width=300)