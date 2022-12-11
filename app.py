# Importing pakages
import streamlit as st
import mysql.connector

from create import create
from database import create_table
from delete import delete
from read import read
from update import update

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
# )
# c = mydb.cursor()

# c.execute("USE railway_reservation_362")


def main():
    st.title("RAILWAY RESERVATION - 362")
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add":
        st.subheader("Enter TRAIN details:")
        create()

    elif choice == "View":
        st.subheader("View added TRAINS")
        read()

    elif choice == "Edit":
        st.subheader("Update TRAIN details")
        update()

    elif choice == "Remove":
        st.subheader("Delete TRAIN details")
        delete()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()