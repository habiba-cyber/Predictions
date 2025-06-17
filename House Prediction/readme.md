# House Price Prediction Project

## Overview

This project focuses on predicting house prices in Bengaluru using machine learning models. It includes complete data preprocessing, feature engineering, model training, and evaluation. The project demonstrates how to clean real-world messy datasets, prepare them for regression tasks, and build an effective predictive model using Support Vector Regression (SVR).

---

## Objectives

- Load and explore the raw dataset
- Clean columns like `total_sqft` and `size`
- Encode categorical variables
- Handle missing values and data types
- Train different regression models (Linear, Random Forest, SVR)
- Evaluate models using metrics like MSE and R² Score
- Use SVR as the final prediction model

---

## Dataset Description

The dataset includes the following key columns:

- `area_type`: Type of the property area
- `availability`: When the property is available
- `location`: Property location
- `size`: BHK or Bedroom count (e.g., "2 BHK", "4 Bedroom")
- `society`: Name of the residential society
- `total_sqft`: Total area of the property
- `bath`: Number of bathrooms
- `balcony`: Number of balconies
- `price`: Price in lakhs (target column)

---

## Technologies Used

- Python
- Pandas and NumPy (data manipulation)
- Matplotlib and Seaborn (visualization)
- scikit-learn (modeling and evaluation)

---

## Model Pipeline

1. **Preprocessing**  
   - Convert `size` to numeric format (e.g., "2 BHK" → 2)
   - Clean `total_sqft`, handling ranges and text units like "Sq. Yards"
   - Drop rows with critical missing values
   - Encode categorical features using one-hot encoding
   - Scale features using `StandardScaler`

2. **Modeling**  
   - Support for three model types:
     - Linear Regression
     - Random Forest Regressor
     - SVR (Support Vector Regression)
   - Trained using 80/20 train-test split

3. **Evaluation**  
   - Mean Squared Error (MSE)
   - R² Score

---

## Final Model

The final model used is **SVR (Support Vector Regression)** with RBF kernel, after trying out multiple models. It performed well on scaled numerical and encoded categorical features.

---

## File Structure

- `PricePredictionModel` class: Encapsulates all steps from data preparation to model evaluation
- Notebook cells:
  - Importing libraries
  - Reading and exploring dataset
  - Preprocessing
  - Model training
  - Evaluation results

---

## Conclusion

This project automates the entire machine learning pipeline for real estate price prediction using structured data. It can serve as a strong foundation for further enhancements like hyperparameter tuning, feature selection, or model deployment