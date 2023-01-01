import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config("wide")

# Add header and other text
st.header("The Best Company")
content = """
Every year, more than 10,000 organisations from over 60 countries partner with Great Place to Work® Institute for assessment, benchmarking, and planning actions to strengthen their workplace culture. Great Place to Work® Institute’s methodology is recognised as rigorous and objective and considered the gold standard for defining great workplaces across business, academia, and government organisations. All organisations that nominate themselves for India’s Best Companies to Work For list underwent a rigorous assessment.
"""
st.write(content)
st.subheader("Our Team")

# prepare the columns
col1, col2, col3 = st.columns(3)

# make a dataframe with the company members
df = pandas.read_csv("data.csv", sep=",")

# add content to the first column
with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()} ")
        st.write(row["role"])
        st.image("image/" + row["image"])

# add content to the second column
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("image/" + row["image"])

# add content to the third column
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("image/" + row["image"])