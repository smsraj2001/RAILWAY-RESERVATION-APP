import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        train_no = st.text_input("Train No:")
        train_name = st.text_input("Name:")
        train_av = st.selectbox("Availability", ["Yes","No"])
    with col2:
        train_s = st.selectbox("Source", ["Bangalore", "Chennai", "Mangaluru"])
        train_d = st.selectbox("Destination", ["Bangalore", "Chennai", "Mangaluru"])
        train_type = st.selectbox("Train Type", ["Superfast","Mail","Fast"])
    
    if st.button("Add Train"):
        add_data(train_no,train_name,train_type,train_s,train_d,train_av)
        st.success("Successfully added TRAIN: {}".format(train_name))
    