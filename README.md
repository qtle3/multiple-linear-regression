# Multiple Linear Regression for Startup Profit Prediction

This project demonstrates the use of multiple linear regression to predict the profit of startups based on their spending in R&D, Administration, Marketing, and the state where the startup operates. The script processes the dataset, encodes categorical data, and trains a linear regression model to predict profit based on these independent variables.

## Detailed Summary

The dataset used in this project contains data from 50 startups, including information on spending in R&D, Administration, Marketing, the State they are located in, and the resulting Profit. The script performs the following steps:
- Imports the dataset and splits it into independent variables (spending and state) and the dependent variable (profit).
- Encodes the categorical "State" column into numerical values using one-hot encoding.
- Splits the dataset into training and test sets.
- Trains a multiple linear regression model on the training data to establish relationships between spending and profits.
- Predicts the profits for the test data and compares them with the actual profits.
- Allows for a single prediction based on specified input values for R&D, Administration, and Marketing spend for a specific state.
- Outputs the regression coefficients and intercept to give insights into the relationships between the independent variables and the predicted profit.
  
## Key Concepts Covered

- **Multiple Linear Regression:** A statistical technique that models the relationship between multiple independent variables (spending in different departments and the state) and a dependent variable (profit).
- **Data Preprocessing:** Includes splitting the data into features (independent variables) and target (dependent variable), encoding categorical data (state), and dividing the dataset into training and testing sets.
- **Model Training and Evaluation:** The linear regression model is trained on the training set and then used to predict values for the test set, allowing comparison between predicted and actual results.
- **Feature Engineering:** The script demonstrates how to handle categorical variables using one-hot encoding to allow a regression model to interpret non-numeric data like "State".
- **Prediction and Interpretation:** It shows how to make specific predictions using new data inputs and outputs the regression coefficients to interpret the impact of each feature on the predicted result.
-  **Regression Coefficients and Intercept:** The script outputs the coefficients and intercept of the regression model, which describe how each variable influences the profit.
