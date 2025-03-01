# Linear Regression Analysis

This code performs simple linear regression analysis manually and tests the significance of the model with the following steps:

### 1. Data Preparation
- Read the dataset consisting of 30 or more observations
- Independent (X) and dependent (Y) variables are stored in DataFrame
- Calculating the mean of X and Y

### Regression Coefficient Calculation
**Regression Equation**: Ŷ = a + bX
- Calculate the slope (b) using the formula:
  
  ``math
  
  b = Σ[(X_i - X̄)(Y_i - Ȳ)] / Σ(X_i - X̄)²
  
- Calculate the intercept (a) using:

  a = Ȳ - bX̄

### Model Evaluation
  a. Mean Squared Error (MSE): Measures the average squared error
  
  b. R-squared (R²): Measures the proportion of variance explained by the model
  
  c. F-statistic: Tests the significance of the model as a whole F = (R²/k) / [(1-R²)/(n-k-1)] where k = the number of independent variables.

### Significance Test
  a. Calculate the p-value using the F distribution
  
  b. Comparing the p-value with α = 0.05
  
  c. Drawing conclusions on the significance of the linear relationship

### Visualization
  a. Displaying scatter plot of actual data
  
  b. Displaying the linear regression line
  
  c. Presents the error (ε) for each observation

Main Output
  1. Model parameters (a and b)
     
  2. Evaluation metrics (MSE and R²)
     
  3. Statistical test results (F-statistic and p-value) 3.
     
  4. Visualization of X-Y relationship
     
  5. List of errors for each data point

Usage of

This code can be used for:
  1. Understand the manual implementation of linear regression
  2. Analyzing the relationship between two numerical variables
  3. Perform significance test of regression model
  5. Visualizing linear regression results
