import streamlit as st
import joblib
import numpy as np

def main():

    st.markdown("""# Health Insurance Cost Prediction:hospital:""", True)
    
    model = joblib.load('model_joblib_gr')
    
    st.markdown("""
    *This web app will predict the cost of health insurance according to certain classes. Data set used is a continuous dependent variable and the model applied to this activity is Gradient Boosting Regression.*""",True)
    
    p1 = st.slider('Enter Your Age',18,100)
    
    s1 = st.selectbox('Sex',('Male','Female'))
    
    if s1=='Male':
        p2=1
    else:
        p2=0
        
    p3 = st.number_input("Enter Your BMI Value")
    
    
    
    p4 = st.slider("Enter Number of Children",0,4)
    
    
    s2 = st.selectbox("Smoker",("Yes","No"))
    
    
    if s2=='Yes':
        p5=1
    else:
        p5=0

    p6 = st.slider("Enter Your Region. 1:Southwest, 2:Southeast, 3:Northwest, 4:Northeast",1,4)
    
    if st.button('Predict'):
        pred= model.predict([[p1,p2,p3,p4,p5,p6]])
        
        st.balloons()
        st.success('Your Insurance Cost is {}'.format(round(pred[0],2)))
        
    
    
        
    
    
    
if __name__ == '__main__':
    main()
