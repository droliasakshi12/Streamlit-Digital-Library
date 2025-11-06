import pymysql 
import streamlit as st 

db=pymysql.connect(host="localhost",user="root",password="",database="parctice")
cursor=db.cursor()


class lib_login:
    def __init__(self):
        username=st.text_input(label="USERNAME",placeholder="enter your username here")
        password=st.text_input(label="PASSWORD",placeholder="enter your password here ")

        login_button=st.button(label="LOGIN")
        if login_button:
            self.login(username,password)
            st.switch_page("pages/select_book.py")





    def login(self,username,password):
        

        select="SELECT * FROM  librarian where username=%s and password=%s"
        try:
            cursor.execute(select,(username,password))
            db.commit()
            fetch_lib=cursor.fetchone()
            if fetch_lib:
                st.success("you are successfully logged in ")
        
        except Exception as e :
            st.error(f"error {e}")
            db.rollback()

obj=lib_login()