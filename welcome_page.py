import streamlit as st
import pymysql

db=pymysql.connect(host="",user="root",password="",database="parctice")
cursor=db.cursor()
class logins:
    def __init__(self):
        
        select=st.selectbox("",("librarian","member"))
        if select=="member":
            left_column,right_column=st.columns(2)
            with left_column:
            
                login_button=st.button(label="LOGIN",use_container_width=True)
                
                if login_button:
                    st.switch_page("pages/member_login.py")
                
                            
            with right_column:
                sign_in=st.button(label="SignIn",use_container_width=True)
                
                if sign_in:
                    st.switch_page("pages/member_signin.py")

        if select=="librarian":
            left_column,right_column=st.columns(2)
            with left_column:
                lib_login=st.button(label="LOGIN",use_container_width=True)
                if lib_login:
                    st.switch_page("pages/librarian_login.py")
            with right_column:
                lib_signin=st.button(label="SignIn",use_container_width=True)
                if lib_signin:
                    st.switch_page("pages/librarian_signin.py")

obj=logins()