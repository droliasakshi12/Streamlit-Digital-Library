import pymysql
import streamlit as st 

db=pymysql.connect(host="localhost",user="root",password="",database="parctice")
cursor=db.cursor()

class insertbook():
     def __init__(self):
           b_name=st.text_input(label="BOOK NAME",placeholder="enter the name of book")
           name=st.text_input(label="AUTHOR NAME",placeholder="enter author name here")
           

           select_author="SELECT author_id FROM author WHERE author_name=%s"
           cursor.execute(select_author,(name))
           db.commit()
           fetch_authid=cursor.fetchone()

           if not fetch_authid:
                self.insert_author(name)
                
           
           insert=st.button(label="INSERT NEW BOOK")
           if insert:
                   self.insert_book(b_name,fetch_authid)
                   st.success("new book recorded")
                   

           
    
    
     def insert_book(self,b_name,fetch_authid):
         inserts_book="INSERT INTO book(book_name,auth_id) VALUES(%s,%s)"
         
         try:
            cursor.execute(inserts_book,(b_name,fetch_authid))
            db.commit()

         except Exception as e:
             st.error(f"error {e}")
             db.rollback()


    
     def insert_author(self,name):
            insert_auth="INSERT INTO author(author_name) VALUES(%s)"
            try:
                cursor.execute(insert_auth,(name))
                db.commit()
            
            

            except Exception as e:
             st.error(f"error {e}")
             db.rollback()

    

obj=insertbook()