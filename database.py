# pip install mysql-connector-python
import mysql.connector
import streamlit as st

try:
    mydb = mysql.connector.connect(**st.secrets["mysql"])
    c = mydb.cursor(buffered = True)
except Exception as e:
    st.write("Error is :{}....Trying to Reconnect".format(e))
    mydb = mysql.connector.connect(**st.secrets["mysql"])
    c = mydb.cursor(buffered = True)    


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Train_362(Train_No INT,Name VARCHAR(30),Train_Type VARCHAR(30),Source VARCHAR(30),Destination VARCHAR(30),Availability VARCHAR(30))')

def add_data(train_no,train_name,train_type,train_s,train_d,train_av):
    c.execute('INSERT INTO Train_362(Train_No,Name,Train_Type,Source,Destination,Availability) VALUES (%s,%s,%s,%s,%s,%s)',(train_no,train_name,train_type,train_s,train_d,train_av))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM Train_362')
    data = c.fetchall()
    return data


def view_only_train_names():
    c.execute('SELECT name FROM Train_362')
    data = c.fetchall()
    return data


def get_train(train_name):
    c.execute('SELECT * FROM Train_362 WHERE Name="{}"'.format(train_name))
    data = c.fetchall()
    return data


def edit_train_data(new_train_no, new_train_name, new_train_type, new_train_s, new_train_d,new_train_av, train_no, train_name, train_type, train_s, train_d,train_av):
    c.execute("UPDATE Train_362 SET Train_No=%s, Name=%s, Train_Type=%s, Source=%s, Destination=%s, Availability=%s  WHERE Train_No=%s and Name=%s and Train_Type=%s and Source=%s and Destination=%s and Availability=%s", (new_train_no, new_train_name, new_train_type, new_train_s, new_train_d,new_train_av, train_no, train_name, train_type, train_s, train_d,train_av))
    mydb.commit()
    data = c.fetchmany()
    return data


def delete_data(train_name):
    c.execute('DELETE FROM Train_362 WHERE Name="{}"'.format(train_name))
    mydb.commit()
