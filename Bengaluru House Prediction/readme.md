# Bengaluru House Price Prediction (ML Project)

This project predicts house prices in Bengaluru using machine learning. It follows a clean, class-based structure and includes data cleaning, univariate and bivariate analysis, model training (Linear & Random Forest), evaluation, and deployment via Streamlit.

---

## Project Structure

bengaluru_price_prediction/
│
├── data/
│ └── Bengaluru_House_Data.csv
│
├── main.ipynb # Jupyter Notebook for step-by-step development
├── streamlit_app.py # Streamlit app file
├── model/
│ └── random_forest_model.pkl # Pickled trained model
│
├── utils/
│ ├── data_cleaning.py # Class for loading and cleaning data
│ ├── univariate_analysis.py # Class for univariate visualizations
│ ├── bivariate_analysis.py # Class for bivariate visualizations
│ ├── model_training.py # Class to train and evaluate model
│ └── model_pickle.py # Class to save and load model
│
├── requirements.txt # All dependencies
└── README.md # This file

## How It Works

### 1. Data Preprocessing
- Cleaned outliers, missing values, and inconsistent entries.
- Extracted BHK and Total Square Feet.
- Encoded categorical columns.

### 2. Exploratory Data Analysis (EDA)
- **Univariate Analysis:** Price distribution, BHK count, area type, availability.
- **Bivariate Analysis:** Price vs BHK, Price vs Location, Price vs Sqft.

### 3. Model Training
- Implemented both **Linear Regression** and **Random Forest Regressor**.
- Achieved R² Score: `0.75` (Random Forest)

### 4. Model Persistence
- Used `pickle` to save and reload the trained model for deployment.

### 5. Streamlit App
- Predict house price using simple UI.
- Takes inputs: location, sqft, BHK, bath.
- Returns prediction in **PKR (₨)**.

---

## Sample Output

Predicted House Price: ₨ 42.28 Lakhs

## Requirements

- Python 3.x
- Pandas
- Numpy
- Scikit-learn
- Seaborn
- Matplotlib
- Streamlit
