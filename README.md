# Machine Learning Project Workflow :

## 1. Problem Understanding


The objective of this project is to build a machine learning regression model that predicts house prices in India based on property characteristics such as number of bedrooms, bathrooms, location and related features.

This model can help buyers, sellers, and real estate companies make data-driven pricing decisions.

---

## 2. Data Loading

In this step the dataset is imported into the environment.


* Read the dataset from a file (CSV, Excel, database, etc.) isong read_filetpe.

* Store the dataset in a structured format such as a DataFrame
* Verify that the dataset loaded correctly using head and shape.


---

## 3. Data Understanding

This step helps to understand the structure of the dataset.

* Identify numerical and categorical features
* Check data types
* Observe the dataset size
* Understand what each feature represents

---



## 4. Data Cleaning

* Handle missing values - no missing in dataframe
  
* Remove duplicate rows - sucessfulfull removed all duplicated rows
  
* Handle outliers - deteced and handling suclessfully


---
## 5. Exploratory Data Analysis (EDA)

EDA is used to analyze and visualize the dataset.

Houses with large living area + high grade have highest prices.

Location (latitude & longitude) significantly influences price.

Basement area also contributes to higher house prices.

Most houses have 3–4 bedrooms.

Price distribution is right-skewed.

Grade values mostly fall between 7–9.

Most houses do not have waterfront views.


---

## 6. Feature Engineering

Convert categorical data into numerical form using onehot Encoding .

Numerical date we need  scaling (min_max) and etc

In this , no need encoding(no categorical column/features) or scaling(numerical are realted land and space so no need )


---

## 7. Feature Selection

Identify the most important variables and remove irrelevant or redundant features

all features are useful.

---

## 8. Train–Test Splitting

The dataset is divided into two parts:

Training Data
Used to train the machine learning model.

Testing Data
Used to evaluate the model performance.

Typical split:

* 80% Training
* 20% Testing

---

## 9. Model Selection

Different machine learning algorithms are tested to find the best one.

* Linear Regression
* Random Forest
* XGBoost
* Decision Tree

Choose the model that gives the best prediction performance

---

## 10. Model Training

In this step the algorithm learns patterns from the training data.

* Fit the model to the training dataset
* Learn relationships between features and target variable

---

## 11. Model Evaluation

After training, the model is evaluated using the test dataset.

Measure how accurate the model predictions are.
 
I used R² Score as metric to evaluate he model

---

## 12. Hyperparameter Tuning

Machine learning models have parameters that control their behavior to overcome the overfiting.

It improve model performance and find optimal parameter values

I used  Grid Search

---

## 13. Model Saving

After selecting the best model, it is saved.

Store the trained model using pickle 

---

## 14. Model Deployment

Build applications like web apps.

A Streamlit web app(hugging space) where users input house features and get predicted price.
