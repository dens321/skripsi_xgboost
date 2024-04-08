# Car Price Prediction API
Car Price Prediction API is a FastAPI application that hosts a XGBoost model for predicting used car prices. It provides a simple and efficient way to get estimated prices for used cars based on various features.

## Features
1. Accepts input parameters such as car brand, model year, mileage, fuel type, etc.
2. Utilizes XGBoost models for efficient and accurate price predictions.
3. Provides a RESTful API interface for easy integration into other applications.
4. Provides preprocess interface to preprocess data.

## Installation
To run the Car Price Prediction API, follow these steps: 
1. Clone the repository:
   ```
   $ git clone https://github.com/dens321/skripsi_xgboost.git
   $ cd skripsi_xgboost
   ```
2. Install dependencies:
   ```
   $ pip install fastapi
   $ pip install sklearn
   $ pip install joblib
   $ pip install pandas
   ```
3. Start the FastAPI server:
   ```
   $ uvicorn app:app --reload
   ```
   
# About the Model
## XGBoost Model & Data Collection
The model was trained using data collected from indonesian car marketplace (mobil123.com). The data collected spans from February 2024 to March 2024.
The features that were used to train the model are: 
- tahun kendaraan (car year)
- kilometer (milage)
- warna (color)
- Transmisi (transmition)
- Kapasitas_kursi (seat capacity)
- cc_mesin (engine cubic centimeters)
- tipe_bahan_bakar (fuel type)
- Merek (brand)
The label or target variable is:
- harga_jual (car_price in Rupiah)
### Hyperparameter Tuning
Hyperparameter tuning was conducted using GridSearchCV, resulting in the optimal parameters for the dataset: {'gamma': 0, 'learning_rate': 0.1, 'max_depth': 15, 'n_estimators': 400, 'reg_lambda': 1.0}. The tuning process was based on minimizing the Mean Absolute Error (MAE)

## Train and Testing Results
The dataset was splitted into 90% for training set and 10% for testing set.
After training the model using the optimized hyperparameters, the following performance metrics were obtained:
- **R2 Score**: 0.97
- **Mean Absolute Percentage Error (MAPE)**: 0.05
- **Mean Absolute Error (MAE)**: 21,616,172.506 (in Rupiah)
