# Linear Regression Implementation

A Python implementation of simple linear regression from scratch, including model training, evaluation metrics, and prediction capabilities.

## Overview

This project provides a complete linear regression solution without external machine learning libraries. It implements the mathematical foundations of linear regression using the least squares method and includes comprehensive model evaluation metrics.

## Features

- **From-scratch implementation** - No sklearn or similar ML libraries required
- **Complete model evaluation** - Includes R², MAE, MSE, RMSE metrics
- **Automatic model rating** - Categorizes model performance as Excellent, Good, Average, or Poor
- **Prediction capabilities** - Make predictions on new data using trained model
- **Interactive input** - Command-line interface for data entry

## Classes

### LinearRegression

The main class that handles model training and evaluation.

**Key Features:**
- Calculates optimal slope and intercept using least squares method
- Computes multiple evaluation metrics automatically
- Provides model performance rating

**Evaluation Metrics:**
- **R² Score**: Coefficient of determination (0-1, higher is better)
- **MAE**: Mean Absolute Error
- **MSE**: Mean Squared Error  
- **RMSE**: Root Mean Squared Error

**Model Performance Ratings:**
- **Excellent**: R² > 0.9, MAE < 3, MSE < 25, RMSE < 5
- **Good**: R² 0.7-0.9, MAE < 10, MSE < 225, RMSE < 15
- **Average**: R² 0.5-0.7, MAE < 20, MSE < 900, RMSE < 30
- **Poor**: Below average thresholds

### Predict

A utility class for making predictions on new data using a trained model.

## Usage

### Basic Usage

```python
# Example data
X = [1, 2, 3, 4, 5]  # Independent variable
y = [2, 4, 6, 8, 10]  # Dependent variable

# Train model
model = LinearRegression(X, y)

# View results
model.PrintMainDetails()

# Make predictions on new data
new_X = [6, 7, 8]
predictions = Predict(model, new_X)
print("Predictions:", predictions.Y)
```

### Interactive Mode

Run the script directly for interactive data entry:

```bash
python linear_regression.py
```

The program will prompt you to enter:
1. Number of data points
2. Independent variable values (X)
3. Dependent variable values (y)
4. New X values for prediction

## Mathematical Foundation

The implementation uses the least squares method to find optimal parameters:

**Slope (m):**
```
m = (n∑XY - ∑X∑Y) / (n∑X² - (∑X)²)
```

**Intercept (b):**
```
b = (∑Y - m∑X) / n
```

**Prediction:**
```
y = mx + b
```

## Example Output

```
slope: 2.0
intercept: 0.0
Y_predicted_values_trained: [2.0, 4.0, 6.0, 8.0, 10.0]
R_square_value: 1.0
Mean_absolute_error: 0.0
Mean_squared_error: 0.0
Root_mean_squared_error: 0.0
Model performance: Excellent Model
```

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Download the `linear_regression.py` file
2. Run directly with Python:
   ```bash
   python linear_regression.py
   ```

## Use Cases

- **Educational**: Understanding linear regression fundamentals
- **Prototype Development**: Quick regression analysis without ML libraries
- **Simple Predictions**: Basic forecasting for linear relationships
- **Model Validation**: Compare with library implementations

## Limitations

- Only supports simple linear regression (single feature)
- No data preprocessing or validation
- Fixed model performance thresholds
- Limited to numeric data types

## Contributing

Feel free to enhance this implementation by adding:
- Multiple linear regression support
- Data validation and error handling
- Visualization capabilities
- Export functionality for results
- Additional evaluation metrics

## License

This project is available for educational and personal use.