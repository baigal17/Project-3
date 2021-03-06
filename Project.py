#Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

################################################################################
# Streamlit application headings
st.markdown("# Health Records")
st.markdown("## Select a Patient")
st.text(" \n")

# Patients' Personal Information

# Database of multiple patients' personal information
patients_database = {
    "George": ["George", "16", "5'11", "80", "Images/George.jpg"],
    "Jane": ["Jane", "21", "5'4", "50", "Images/Jane.jpg"],
    "Karen": ["Karen", "55", "5'7", "30", "Images/Karen.jpg"],
    "Luke": ["Luke", "1", "2", "100", "Images/Luke.jpg"],
    "Tom": ["Tom", "65", "6'2", "50", "Images/Tom.jpg"]
}

# A list of the patients' first names
people = ["George", "Jane", "Karen", "Luke", "Tom"]


def get_people(w3):
    """Display the database of the patients information."""
    db_list = list(patients_database.values())

    for number in range(len(people)):

        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Age: ", db_list[number][1])
        st.write("Height: ", db_list[number][2])
        st.write("Health Score: ", db_list[number][3])
        st.text(" \n")

################################################################################
# Streamlit Code
get_people(w3)


################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Patients' Details")


# Create a select box to select a patient
person = st.sidebar.selectbox('Select a Person', people)

# Create a slider to measure each patient's health score in a range of 0 through 100.
health_score = st.sidebar.slider("Range of Health Score:", value=(0, 100))

# Create a textbox for doctors to leave additional information for each patient.  
text = st.sidebar.text_area("Any additional information")

if st.sidebar.button('Save'):
    st.sidebar.write('Saved')
else:
    st.sidebar.write('Edit')

# Create a button for parties to upload any additional information. 
st.sidebar.markdown("## Upload Additional Information!")

data = uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     st.write(bytes_data)

# Create a download text file.
text_contents = '''This is text file'''
st.sidebar.download_button('Download text file', text_contents)


# Sending Information to Blockchain
if st.sidebar.button("Send Information"):
    transaction_hash = send_transaction("name", "age", "health_score")

    st.sidebar.markdown("#### Validated Transaction Hash")
    st.sidebar.write(transaction_hash)
       
    st.balloons()