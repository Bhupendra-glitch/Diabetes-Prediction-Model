# 🩺 Diabetes Prediction using Machine Learning

## 📌 Project Overview
Diabetes is a chronic metabolic disorder characterized by high blood sugar levels over a prolonged period. Common symptoms include frequent urination, increased thirst, and increased hunger. If left untreated, diabetes can lead to severe complications such as cardiovascular disease, stroke, kidney failure, nerve damage, eye damage, and even death.

This project focuses on building a **Machine Learning model** to predict whether a patient has diabetes based on diagnostic medical measurements.

---

## 🎯 Objective
The main objective of this project is to:
- Develop a machine learning model that can **accurately predict diabetes** in patients.
- Analyze medical features to understand their impact on diabetes prediction.
- Provide a data-driven approach to early diabetes detection.

---

## 📊 Dataset Description
The dataset used in this project is originally from the **National Institute of Diabetes and Digestive and Kidney Diseases**.

### 🔍 Dataset Characteristics
- **Population**: Female patients of Pima Indian heritage
- **Age Constraint**: At least 21 years old
- **Total Observations**: 768
- **Total Variables**: 9 (8 input features + 1 target variable)

---

## 🧾 Feature Information

| Feature Name | Description |
|--------------|------------|
| **Pregnancies** | Number of times the patient has been pregnant |
| **Glucose** | Plasma glucose concentration after 2 hours in an oral glucose tolerance test |
| **BloodPressure** | Diastolic blood pressure (mm Hg) |
| **SkinThickness** | Triceps skin fold thickness (mm) |
| **Insulin** | 2-hour serum insulin (mu U/ml) |
| **BMI** | Body Mass Index (kg/m²) |
| **DiabetesPedigreeFunction** | Diabetes pedigree function (genetic influence) |
| **Age** | Age of the patient (years) |
| **Outcome** | Target variable (0 = Non-diabetic, 1 = Diabetic) |

---

## 🛠️ Methodology
1. **Data Loading & Exploration**
2. **Data Preprocessing**
   - Handling missing or zero values
   - Feature scaling
3. **Exploratory Data Analysis (EDA)**
4. **Model Building**
   - Logistic Regression
   - K-Nearest Neighbors (KNN)
   - Support Vector Machine (SVM)
   - Decision Tree
   - Random Forest
5. **Model Evaluation**
   - Accuracy
   - Confusion Matrix
   - Precision, Recall, F1-score
6. **Model Selection**
   - Choosing the best-performing model

---

## 📈 Results
The trained machine learning models are evaluated based on performance metrics, and the best model is selected for diabetes prediction. The results demonstrate that machine learning can be effectively used to assist in early diagnosis of diabetes.

---

## 🚀 Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib / Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 📂 Project Structure
