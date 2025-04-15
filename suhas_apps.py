# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 00:33:14 2025

@author: Chaithra
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

wine_model = pickle.load(open('C:/ML-Models and Apps/wine_model.sav','rb'))
loan_model = pickle.load(open('C:/ML-Models and Apps/loan_prediction.sav','rb'))
diab_model = pickle.load(open('C:/ML-Models and Apps/diabetes_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Suhas Multi Apps System',['Wine Test','Loan Prediction', 'Diabetes Test'],default_index=0)
    
#Wine Prediction Page
if (selected == 'Wine Test'):
    st.title('🍾 Wine Quality Test')
    fixed_acidity = st.text_input('Fixed Acidity')
    volatile_acidity = st.text_input('Volatile Acidity')
    citric_acid = st.text_input('Citric Acid')
    residual_sugar = st.text_input('Residual Sugar')
    chlorides = st.text_input('Chlorides')
    free_sulfur_dioxide = st.text_input('Free Sulfur Dioxide')
    total_sulfur_dioxide = st.text_input('Total Sulfur Dioxide')
    density = st.text_input('Density')
    pH = st.text_input('pH')
    sulphates = st.text_input('Sulphates')
    alcohol = st.text_input('Alcohol')
    
    wine_result = ''
    
    if st.button('Wine Quality Result'):
        
        wine_pred = wine_model.predict([[fixed_acidity,volatile_acidity,citric_acid	,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]])
        
        if (wine_pred[0]==1):
            wine_result = 'Good Wine'
            
        else:
            wine_result = 'Bad Wine'
            
        st.success(wine_result)
        

        
    
if (selected == 'Loan Prediction'):
    
    st.title('💲 Loan Prediction App')
    
    Gender = st.text_input('Gender')
    Married = st.text_input('Married')
    Dependents = st.text_input('Dependents')
    Education = st.text_input('Education')
    Self_Employed = st.text_input('Self Employed')
    ApplicantIncome = st.text_input('Applicant Income')
    CoapplicantIncome = st.text_input('Coapplicant Income')
    LoanAmount = st.text_input('Loan Amount')
    Loan_Amount_Term = st.text_input('Loan Amount Term')
    Credit_History = st.text_input('Credit History')
    Property_Area = st.text_input('Property Area')
    
    loan_res = ''
    
    if st.button('Loan Prediction Result'):
        loan_pred = loan_model.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
        if (loan_pred[0]==0):
            loan_res = 'Loan Approval Rejected  👎'
        else:
            loan_res = 'Loan Approval Successfully  😀'
    st.success(loan_res)
      

    
    
if (selected == 'Diabetes Test'):
    st.title('🏥 Diabetes Test')
    Pregnancies = st.text_input('Pregnancies')
    Glucose = st.text_input('Glucose')
    BloodPressure = st.text_input('BloodPressure')
    SkinThickness = st.text_input('SkinThickness')
    Insulin = st.text_input('Insulin')
    BMI = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    Age = st.text_input('Age')
    
    diab_results = ''
    if st.button('Diabetic Test Results'):
        
        diab_pred = diab_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_pred[0] == 1):
            diab_results = 'The Person is Diabetic'
        else:
            diab_results = 'The person is non Diabetic'
            
    st.success(diab_results)
        

