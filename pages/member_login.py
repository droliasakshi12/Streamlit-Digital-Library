import pymysql
import streamlit as st 

db=pymysql.connect(host="localhost",user="root",password="",database="parctice")
cursor=db.cursor()

class member:
    def __init__(self):
        username=st.text_input(label="USERNAME",placeholder="enter your username")
        password=st.text_input(label="PASSWORD",placeholder="enter tour password",type="password")

        left_column=st.columns(2)

        with left_column:

            login_button=st.button(label="LOGIN",use_container_width=True)

            if login_button:
                self.member_login(username,password)
           
        
            
        
        
        


    def member_login(self,username,password):
        select_member="SELECT * FROM member WHERE username = %s and password =%s"
        try:
            cursor.execute(select_member,(username,password))
            db.commit()
            fetch_member=cursor.fetchone()

            if fetch_member:
                st.success("YOU ARE LOGGED IN!")
                st.switch_page("pages/select_book.py")
            else:
                st.error("you are not the member please sign in first")
                
            
        
        except Exception as e:
            st.error(f"error {e}")
            db.rollback()



   



obj=member()