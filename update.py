import datetime
import pandas as pd
import streamlit as st
from database import view_all_data, view_only_train_names, get_train, edit_train_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Train_No', 'Name', 'Train_Type', 'Source', 'Destination', 'Availability'])
    with st.expander("Current Trains"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_train_names()]
    selected_train = st.selectbox("Train to Edit", list_of_trains)
    selected_result = get_train(selected_train)
    # st.write(selected_result)
    if selected_result:
        train_no = selected_result[0][0]
        train_name = selected_result[0][1]
        train_type = selected_result[0][2]
        train_s = selected_result[0][3]
        train_d = selected_result[0][4]
        train_av = selected_result[0][5]


        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_train_no = st.text_input("Train No:", train_no)
            new_train_name = st.text_input("Name:", train_name)
            new_train_av = st.selectbox("Availability", ["Yes","No"])
        with col2:
            new_train_s = st.selectbox("Source", ["Bangalore", "Chennai", "Mangaluru"])
            new_train_d = st.selectbox("Destination", ["Bangalore", "Chennai", "Mangaluru"])
            new_train_type = st.selectbox("Train Type", ["Superfast","Mail","Fast"])
        if st.button("Update Train"):
            edit_train_data(new_train_no, new_train_name, new_train_type, new_train_s, new_train_d,new_train_av, train_no, train_name, train_type, train_s, train_d,train_av)
            st.success("Successfully updated:: {} to ::{}".format(train_name, new_train_name))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Train_No', 'Name', 'Train_Type', 'Source', 'Destination', 'Availability'])
    with st.expander("Updated Data"):
        st.dataframe(df2)