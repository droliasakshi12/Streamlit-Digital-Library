import pymysql 
import streamlit as st 
import pandas as pd 

db=pymysql.connect(host="localhost",user="root",password="",database="parctice")
cursor=db.cursor()

class book:
    def __init__(self):
        b_name=st.text_input(label="BOOK NAME",placeholder="enter book name here ")
        left_column,right_column=st.columns(2)
        with left_column:
            select_button=st.button(label="FIND BOOK",use_container_width=True)
            if select_button:
                self.select_book(b_name)
       
        with right_column:
            insert_button=st.button(label="INSERT NEW BOOK",use_container_width=True)
            if insert_button:
                st.switch_page("pages/insert_book.py")
            
    
    def select_book(self,b_name):
            select="SELECT * FROM book  where book_name=%s"
            

            try:
                cursor.execute(select,(b_name))
                fetch_book=cursor.fetchone()
        
                if fetch_book:
                   
                    st.success("book available")
                else:
                    st.error("book not available please insert it if you want!!")
            
            
                
            except Exception as e :
                st.error(f"error {e}")
                db.rollback()

            
    
   
        
    


        



        
        
obj=book()