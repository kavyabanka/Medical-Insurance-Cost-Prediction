import streamlit as st  
import numpy as np
import pickle
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# Prevent deprecation warning for file uploader
#st.set_option('deprecation.showfileUploaderEncoding', False)

# Load the pre-trained model using pickle
model = pickle.load(open('C:/Users/HP/Downloads/new_model.pkl', 'rb'))

def main():
    # Sidebar with header and text
    st.sidebar.header("Insurance Cost Prediction")
    st.sidebar.text("Web app that predicts your insurance cost")
    st.sidebar.header("Fill the form below")
    st.sidebar.text("The AdaBoost Regressor was used")

    # User input fields for age, gender, BMI, number of children, and smoking status
    age = st.slider("Input your age", 0, 100)
    sex = st.slider("Input your gender: 0 for male, 1 for female", 0, 1)
    bmi = st.slider("BMI", 0.0, 70.0)
    children = st.slider("How many children do you have?", 0, 10)
    smoker = st.slider("If you are a smoker, choose 0; otherwise, choose 1", 0, 1)

    # Prepare input data for prediction
    inputs = [[age, sex, bmi, children, smoker]]
    
    if st.button('Predict'):
        result = model.predict(inputs)
        updated_res = result.flatten().astype(float)
        st.success('Your predicted insurance cost is: ${}'.format(updated_res[0]))

if __name__ == '__main__':
    main()
