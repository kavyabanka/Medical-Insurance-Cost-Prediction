# **Medical Insurance Cost Prediction Using AdaBoost Regressor**

## **Project Overview**

This project predicts medical insurance costs based on various factors such as age, gender, BMI, number of children, smoking habits, and more. We use a machine learning model, specifically the **AdaBoost Regressor**, to build the prediction system. The dataset used is sourced from real-world data on insurance charges, and the project showcases how feature encoding and regression models can be utilized to make accurate predictions.

During a **tech fest** organized at our college, we presented this project to demonstrate the power of machine learning in predicting real-world outcomes. Our team showcased how different algorithms could be implemented to solve regression problems, with this project being one of the highlights.

## **Dataset**

We used a dataset containing the following features:
- **Age**: Age of the primary beneficiary
- **Sex**: Gender of the beneficiary
- **BMI**: Body Mass Index
- **Children**: Number of children/dependents covered by health insurance
- **Smoker**: Whether the beneficiary is a smoker or not
- **Region**: The beneficiary's residential area in the US
- **Charges**: Medical insurance charges (target variable)

After label encoding categorical variables and standardizing the data, we trained our model using the **AdaBoost Regressor** to predict medical insurance charges based on the given features.

## **Model**

- **AdaBoost Regressor**: A machine learning model used to improve the accuracy of predictions by combining several weak learners into a strong model. In our case, it was used to predict the charges effectively, yielding an **R² score of 0.825**.

### **Model Evaluation**

The model's performance was evaluated using the **R² score** and **Mean Squared Error (MSE)**, resulting in an accuracy of **82.54%** on the test set. This demonstrated the potential of boosting algorithms in regression tasks.

## **How to Run the Project**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/insurance-cost-prediction.git
## **Usage in Tech Fest**

We utilized this project during our college's **Tech Fest** to demonstrate the practical applications of machine learning in the field of insurance and healthcare. The presentation included a live demo where participants could input values such as age, BMI, and smoking status to predict their insurance costs. The audience appreciated the ability to visualize how machine learning models like AdaBoost could handle real-world regression tasks.

