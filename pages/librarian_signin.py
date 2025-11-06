import pymysql 
import streamlit as st 

db=pymysql.connect(host="localhost",user="root",password="",database="parctice")
cursor=db.cursor()

class signin():
    def __init__(self):
        name = st.text_input(label="YOUR NAME",placeholder="enter your name here ")
        username=st.text_input(label="USERNAME",placeholder="enter your username here ")
        password=st.text_input(label="PASSWORD",placeholder="enter your password here")

        signin_button=st.button(label="SignIn")
        if signin_button:
            self.lib_signin(name,username,password)
            st.switch_page("pages/librarian_login.py")

    



    def lib_signin(self,name,username,password):
        insert="INSERT INTO librarian(name,username,password) VALUES(%s,%s,%s)"
        try:
            cursor.execute(insert,(name,username,password))
            db.commit()
            affected=cursor.rowcount()

            if affected:
                st.success("you are successfully logged in ")


        except Exception as e :
            st.error(f"error {e}")
            db.rollback()

obj=signin()