import json
from db import Database
from tkinter import messagebox
from myapi import API
d=[]
class Validation(Exception):
    def __init__(self,message):
        print(message)
        
        
from tkinter import *
class NLPApp:
    def __init__(self):
        self.dbo=Database()
        self.apio=API()
        
        self.root=Tk()
        self.root.title('NLPApp')
        self.root.geometry('400x650')
        self.root.configure(bg='black')
        
        self.login_gui()
        
        
        self.root.mainloop()
    
    
    def login_gui(self):
        
        self.clear()
        
        #Heading for login gui
        heading=Label(self.root,text='NLPApp',bg='black',fg='white')
        heading.pack(pady=(50,50))
        heading.configure(font=('poppins',24,'bold'))
        
        #Label for email
        label1=Label(self.root,text='Enter email:',bg='black',fg='white')
        label1.configure(font=('poppins',15,'bold'))
        label1.pack(pady=(10,10))
        
        #Email input box
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(10,10),ipady=4)  
        
        #Label for password
        label2=Label(self.root,text='Enter password:',bg='black',fg='white')
        label2.configure(font=('poppins',15,'bold'))
        label2.pack(pady=(10,10))
        
        #password input box
        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(10,10),ipady=4)  
              
         #login button     
        login_button=Button(self.root,text='Login',width=30,bg='black',border='5',fg='white',command=self.login_user)
        login_button.pack(pady=(30,30))
        login_button.configure(font=('poppins',12,'bold'))
        
        #Label for register button
        label3=Label(self.root,text='Not a member ?',bg='black',fg='white',font=('bold'))
        label3.configure(font=('poppins',12,'bold'))
        label3.pack(pady=(10,10))
            
        #register button
        register_button=Button(self.root,text='Register now',bg='white',border='5',fg='black',command=self.register_gui)
        register_button.pack(pady=(10,10))
        register_button.configure(font=('poppins',12,'bold'))
        
    def register_gui(self):
       
        self.clear()
            
        heading=Label(self.root,text='Register',bg='black',fg='white')
        heading.pack(pady=(50,50))
        heading.configure(font=('poppins',24,'bold'))
        
        label0=Label(self.root,text='Enter Name:',bg='black',fg='white')
        label0.configure(font=('poppins',15,'bold'))
        label0.pack(pady=(10,10))
        
        self.name_input=Entry(self.root,width=50)
        self.name_input.pack(pady=(10,10),ipady=4)
        
        label1=Label(self.root,text='Enter email:',bg='black',fg='white')
        label1.configure(font=('poppins',15,'bold'))
        label1.pack(pady=(10,10))
        
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(10,10),ipady=4)  
        
        label2=Label(self.root,text='Enter password:',bg='black',fg='white')
        label2.configure(font=('poppins',15,'bold'))
        label2.pack(pady=(10,10))
        
        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(10,10),ipady=4)  
              
        register_button=Button(self.root,text='Register',width=30,bg='black',border='5',fg='white',command=self.register_user)
        register_button.pack(pady=(30,30))
        register_button.configure(font=('poppins',12,'bold'))
        
        label3=Label(self.root,text='Already a member ?',bg='black',fg='white',font=('bold'))
        label3.configure(font=('poppins',12,'bold'))
        label3.pack(pady=(10,10))
            
        login_button=Button(self.root,text='Login',bg='white',border='5',fg='black',command=self.login_gui)
        login_button.pack(pady=(10,10))
        login_button.configure(font=('poppins',12,'bold'))
    
    def menu_bar_gui(self):
        self.clear()
        
        heading=Label(self.root,text='Menu',bg='black',fg='white')
        heading.pack(pady=(50,50))
        heading.configure(font=('poppins',24,'bold'))
        
        
        sentiment_button=Button(self.root,text='Sentiment Analysis',width=30,bg='black',border='5',fg='white',command=self.sentiment_gui)
        sentiment_button.pack(pady=(30,30))  
        sentiment_button.configure(font=('poppins',12,'bold'))
        
        ner_button=Button(self.root,text='Named Entity Recognition',width=30,bg='black',border='5',fg='white',command=self.ner_gui)
        ner_button.pack(pady=(30,30))
        ner_button.configure(font=('poppins',12,'bold'))
        
        emotion_button=Button(self.root,text='Emotional Prediction',width=30,bg='black',border='5',fg='white',command=self.emotion_gui)
        emotion_button.pack(pady=(30,30))
        emotion_button.configure(font=('poppins',12,'bold'))
        
        logout_button=Button(self.root,text='Log Out',width=30,bg='black',border='5',fg='white',command=self.login_gui)
        logout_button.pack(pady=(30,30))
        logout_button.configure(font=('poppins',12,'bold'))
            
    
    def sentiment_gui(self):
        self.clear()
        
        heading=Label(self.root,text='NLPApp',bg='black',fg='white')
        heading.pack(pady=(50,50))
        heading.configure(font=('poppins',24,'bold'))
        
        heading2=Label(self.root,text='Sentiment Analysis',bg='black',fg='white')
        heading2.pack(pady=(10,10))
        heading2.configure(font=('poppins',15))
        
        label1=Label(self.root,text='Enter the text',bg='black',fg='white',font=('bold'))
        label1.configure(font=('poppins',12,'bold'))
        label1.pack(pady=(30,30))
        
        self.sentiment_input=Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(10,10),ipady=4) 
        
        sentiment_button=Button(self.root,text='Analyze Sentiment',width=30,bg='black',border='5',fg='white',command=self.do_sentiment_analysis)
        sentiment_button.pack(pady=(30,30))
        sentiment_button.configure(font=('poppins',12,'bold'))
        
        self.sentiment_result=Label(self.root,text='',bg='black',fg='white')
        self.sentiment_result.pack(pady=(10,23))
        self.sentiment_result.configure(font=('poppins',13))
        
        
        return_button=Button(self.root,text='Return to Menu',width=30,bg='black',border='5',fg='white',command=self.menu_bar_gui)
        return_button.pack(pady=(10,10))
        return_button.configure(font=('poppins',12,'bold'))
        
    
    def ner_gui(self):
       self.clear()
        
       heading=Label(self.root,text='NLPApp',bg='black',fg='white')
       heading.pack(pady=(50,50))
       heading.configure(font=('poppins',24,'bold'))
        
       heading2=Label(self.root,text='Named Entity Recognition',bg='black',fg='white')
       heading2.pack(pady=(10,10))
       heading2.configure(font=('poppins',15))
        
       label1=Label(self.root,text='Enter the text',bg='black',fg='white',font=('bold'))
       label1.configure(font=('poppins',12,'bold'))
       label1.pack(pady=(30,30))
        
       self.ner_input=Entry(self.root,width=50)
       self.ner_input.pack(pady=(10,10),ipady=4) 
        
       ner_button=Button(self.root,text='Recognise Entity',width=30,bg='black',border='5',fg='white',command=self.do_ner)
       ner_button.pack(pady=(30,30))
       ner_button.configure(font=('poppins',12,'bold'))
       
       self.ner_result=Label(self.root,text='',bg='black',fg='white')
       self.ner_result.pack(pady=(10,23))
       self.ner_result.configure(font=('poppins',13))
        
       return_button=Button(self.root,text='Return to Menu',width=30,bg='black',border='5',fg='white',command=self.menu_bar_gui)
       return_button.pack(pady=(10,10))
       return_button.configure(font=('poppins',12,'bold'))
        
    
    def emotion_gui(self):
       self.clear()
        
       heading=Label(self.root,text='NLPApp',bg='black',fg='white')
       heading.pack(pady=(50,50))
       heading.configure(font=('poppins',24,'bold'))
        
       heading2=Label(self.root,text='Emotional Prediction',bg='black',fg='white')
       heading2.pack(pady=(10,10))
       heading2.configure(font=('poppins',15))
        
       label1=Label(self.root,text='Enter the text',bg='black',fg='white',font=('bold'))
       label1.configure(font=('poppins',12,'bold'))
       label1.pack(pady=(30,30))
        
       self.emotion_input=Entry(self.root,width=50)
       self.emotion_input.pack(pady=(10,10),ipady=4) 
        
       emotion_button=Button(self.root,text='Predict Emotion',width=30,bg='black',border='5',fg='white',command=self.do_emotion)
       emotion_button.pack(pady=(30,30))
       emotion_button.configure(font=('poppins',12,'bold'))
       
       
       self.emotion_result=Label(self.root,text='',bg='black',fg='white')
       self.emotion_result.pack(pady=(10,23))
       self.emotion_result.configure(font=('poppins',13))
        
       return_button=Button(self.root,text='Return to Menu',width=30,bg='black',border='5',fg='white',command=self.menu_bar_gui)
       return_button.pack(pady=(10,10))
       return_button.configure(font=('poppins',12,'bold'))   
             
    def clear(self):
         #clear the existing gui
        for i in self.root.pack_slaves():
            # print(i)
            i.destroy()
      
           
    def register_user(self):
         
         #Fetch data from user
         name=self.name_input.get()
         email=self.email_input.get()
         password=self.password_input.get()
         
           #  Check if any of the fields are empty
         try:
            if self.email_input.get()=="" or self.password_input.get()=="" or self.name_input.get()=="":
             raise Validation("email or password field cant be empty")
            
            response=self.dbo.add_data(name,email,password)
            if response==1:
             messagebox.showinfo('Success',"User Registered Successfully, you can login now")
            else:
             messagebox.showerror('Error',"Email already Exists")
         
         except Validation as e:
           pass
    
    
    
    def login_user(self):
        
        email=self.email_input.get()
        password=self.password_input.get()
        
        #Check if any of the fields are empty
        try:
            if self.email_input.get()=="" or self.password_input.get()=="":
             raise Validation("email or password field cant be empty")
         
        except Validation as e:
          pass
        
        else:
         response=self.dbo.login(email,password) 
         if response:
            messagebox.showinfo('Success',"User logged in successfully")
            self.menu_bar_gui()
         
         elif response==-1:
             messagebox.showerror('Error',"User does not exists")
             
         else:
             messagebox.showerror('Error',"Incorrect password")  
            
        
     #get() function is used to get the value of entry
    
    
    def do_sentiment_analysis(self):
        text=self.sentiment_input.get()
        response=self.apio.sentiment_analysis(text)
        self.sentiment_result['text']=response
        
    def do_emotion(self):
        text=self.emotion_input.get()
        response=self.apio.emotion(text)
        self.emotion_result['text']=response
        
    def do_ner(self):
        text=self.ner_input.get()
        response=self.apio.ner(text)
        self.ner_result['text']=response
       
        
        

nlp=NLPApp()      