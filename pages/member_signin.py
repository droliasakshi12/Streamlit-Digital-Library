import pymysql
import streamlit as st 

db=pymysql.connect(host="localhost",user="root",password="",database="parctice")
cursor=db.cursor()

class member():

    def __init__(self):
        name=st.text_input(label="NAME")
        username=st.text_input(label="USERNAME",placeholder="enter username here")
        password=st.text_input(label="PASSWORD",placeholder="enter your password here",type="password")
        signin_button=st.button(label="SignIn")
        
        if signin_button:
                st.success("you have successfully signed in ")
                self.member_sign_in(name,username,password)
                st.switch_page("pages/member_login.py")

                

        
        
    def member_sign_in(self,name,username,password):
       insert_member="INSERT INTO member(name,username,password) VALUES(%s,%s,%s)"
       try:
        cursor.execute(insert_member,(name,username,password))
        db.commit()
       except Exception as e :
        st.error(f"error {e}")
        db.rollback()



obj=member()





 
