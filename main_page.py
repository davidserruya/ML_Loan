from ctypes import alignment
import streamlit as st  
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import streamlit.components.v1 as components
import pandas as pd
from streamlit_option_menu import option_menu

# Settings
st.set_page_config(layout="wide")
st.markdown(""" <style> .block-container {padding-top: 2.5rem; padding-bottom: 0rem;} </style> """, unsafe_allow_html=True)

# recovery of dataset
@st.cache_data  
def load_data():
    df = pd.read_csv("datasets/loan_final.csv")
    X = df.drop(columns='Loan_Status')
    y = df['Loan_Status']
    return X,y

#function for the result of the form
@st.cache_resource
def fit_model(tabValues):
    X,y=load_data()
    clf=RandomForestClassifier()
    clf.fit(X.values,y)
    result=clf.predict(tabValues)
    return result

#Functions of navbar menu
def do_home():
    HtmlFile = open("home_page.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code,height=3000)   

def do_dashboard():
    st.markdown("<h1 style='text-align: center;padding-top:0rem;padding-bottom:0rem'>DASHBOARD</h1>", unsafe_allow_html=True) 
    components.iframe("https://lookerstudio.google.com/embed/reporting/0fb09256-3d8b-4fbd-80c6-a81300c7f525/page/8MFGD", width=1200, height=1000, scrolling=True)
    

def do_dataset():
    col1, col2 = st.columns([3,1])

    with col1:  
        st.markdown("<h1 style='text-align: center;padding-top:0rem'>DATASET</h1>", unsafe_allow_html=True)  
        components.iframe("https://lookerstudio.google.com/embed/reporting/b358e800-4264-449c-8bd8-78279bc1c681/page/knFGD", width=850, height=850, scrolling=True)

    with col2:
        st.markdown("<h1 style='text-align: center;padding-top:0rem;padding-bottom:2rem'>DATA DESCRIPTION</h1>", unsafe_allow_html=True)
        data = pd.read_csv("datasets/dataset_description.csv") 
        st.write(data)
    
def do_BLAForm():
  col1, col2 = st.columns([1,1])
  with col1:
    with st.form("my_form"):
         st.markdown("<h1 style='text-align: center;padding-top:0rem'>Bank Loan Application Form</h1>", unsafe_allow_html=True)
         gender = st.radio("Sex:",('Female','Male'),horizontal=True)
         married=st.selectbox('Marital status:',('Married', 'Divorced', 'Single','Widowed'))
         dependents = st.selectbox('Dependant people in the household:',('0','1', '2', '3 or +'))
         education = st.radio("Graduated ?", ('Yes', 'No'),horizontal=True)
         selfEmployed = st.radio("Self-employed ?",('Yes', 'No'),horizontal=True)
         applicantIncome=st.number_input('Monthly salary:')
         coapplicantIncome=st.number_input('Co-applicant monthly salary:')
         loanAmount=st.number_input('Amount requested:')
         loanAmountTerm=st.number_input(' Loan duration term in months:')
         creditHistory= st.checkbox("Credit History",help="Credit history meets guidelines")
         propertyArea=st.selectbox('Property area:',('Urban','Semi-Urban', 'Rural'))
         # Every form must have a submit button.
         submitted = st.form_submit_button("Submit")
         if submitted:
            if gender=="Male":
                gender=0
            else:
                gender=1
            if married=="Married":
                married=1
            else:
                married=0
            if education=="Yes":
                education=1
            else:
                education=0
            if selfEmployed=="Yes":
                selfEmployed=1
            else:
                selfEmployed=0
            if creditHistory==True:
                creditHistory=1
            else:
                creditHistory=0
            if propertyArea=="Rural":
                propertyArea=2
            elif propertyArea=='Semi-Urban':
                propertyArea=0
            else:
                propertyArea=1
            if dependents=='0':
                dependents=0
            elif dependents=='1':
                dependents=1
            elif dependents=="2":
                dependents=2
            else:
                dependents=3
            formValues=[gender,married,dependents,education,selfEmployed,applicantIncome,coapplicantIncome,loanAmount,loanAmountTerm,creditHistory,propertyArea]
            tabFormValues=[formValues]
            result=fit_model(tabFormValues)
            with col2:
              col3, col4, col5 = st.columns([2,6,1])

            with col4:
              if result==1:
                st.image("pictures/approved.png", width = 480)
              else:
                st.image("pictures/rejected.png", width = 480)


# Display navbar menu 
with st.sidebar:
 with st.expander("Main Menu"):
  selected = option_menu("Main Menu", 
    ["Home", "Dashboard","BLA Form","Dataset"], 
    icons=["house", "bi bi-file-earmark-bar-graph","bi bi-file-earmark-text","server"],
    default_index=0,
    styles={
        "icon": {"color": "black", "font-size": "30px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#f4f4f4"},
        "nav-link-selected": {"background-color": "#dcdcdc","color":"black"}
    })  

menu_dict = {
    "Home" : {"fn": do_home},
    "Dashboard" : {"fn": do_dashboard},
    "BLA Form" : {"fn": do_BLAForm},
    "Dataset": {"fn": do_dataset}
} 



if selected in menu_dict.keys():
    menu_dict[selected]["fn"]()

    







