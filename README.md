![GitHub stars](https://img.shields.io/github/stars/rzr06/Regresi-Linear-Sederhana?style=for-the-badge)

[![GitHub forks](https://img.shields.io/github/forks/rzr06/Regresi-Linear-Sederhana?style=for-the-badge)](https://github.com/rzr06/Regresi-Linear-Sederhana/network)

[![GitHub issues](https://img.shields.io/github/issues/rzr06/Regresi-Linear-Sederhana?style=for-the-badge)](https://github.com/rzr06/Regresi-Linear-Sederhana/issues)

**A Python script for performing and visualizing simple linear regression analysis on a dataset.**

</div>

## 📖 Overview

This repository contains a simple Python script designed to demonstrate and perform linear regression analysis. It reads data from an Excel file, applies a simple linear regression model to predict a dependent variable based on an independent variable, evaluates the model's performance, and visualizes the results. This project is ideal for learning fundamental machine learning concepts and data analysis techniques using popular Python libraries.

## ✨ Features

-   📊 **Data Loading from Excel**: Seamlessly imports datasets from `.xlsx` files using `pandas`.
-   ✂️ **Data Splitting**: Divides the dataset into training and testing sets (80/20 split) to validate model performance.
-   📈 **Simple Linear Regression Model**: Trains a robust linear regression model using `scikit-learn`.
-   🔍 **Coefficient Extraction**: Accurately calculates and displays the slope and intercept of the regression line.
-   🎯 **Model Evaluation**: Quantifies model performance using Mean Squared Error (MSE) and R-squared score.
-   📉 **Interactive Data Visualization**: Generates and displays a plot showing the original data points alongside the fitted regression line using `matplotlib`.

## 🛠️ Tech Stack

**Core:**
-   <img src="https://img.shields.io/badge/Python-3.x-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">

**Libraries:**
-   <img src="https://img.shields.io/badge/Pandas-1.x%2B-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
-   <img src="https://img.shields.io/badge/NumPy-1.x%2B-013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
-   <img src="https://img.shields.io/badge/Matplotlib-3.x%2B-11557C.svg?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
-   <img src="https://img.shields.io/badge/scikit--learn-1.x%2B-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">

## 🚀 Quick Start

### Prerequisites
-   Python 3.x installed on your system.
-   The `Statistika.xlsx` data file located in the same directory as the script.

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/rzr06/Regresi-Linear-Sederhana.git
    cd Regresi-Linear-Sederhana
    ```

2.  **Install dependencies**
    It's recommended to use a virtual environment.
    ```bash
    # Create a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`

    # Install the required Python libraries
    pip install pandas numpy matplotlib scikit-learn
    ```
    *Alternatively, you can create a `requirements.txt` file:*
    ```
    pandas>=1.0
    numpy>=1.18
    matplotlib>=3.0
    scikit-learn>=1.0
    ```
    *And then install with:*
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Ensure data file is present**
    Make sure `Statistika.xlsx` is in the same directory as `RegresiLinear.py`.

2.  **Run the script**
    ```bash
    python RegresiLinear.py
    ```

3.  **Output**
    The script will print the calculated regression coefficients (intercept and slope), model evaluation metrics (Mean Squared Error, R-squared score), and display a Matplotlib plot showing the data points and the fitted regression line.

## 📁 Project Structure

```
Regresi-Linear-Sederhana/
├── RegresiLinear.py   # Main Python script for linear regression analysis
├── Statistika.xlsx    # Input dataset for the analysis
└── README.md          # Project documentation
```

## ⚙️ Configuration

The script uses a hardcoded Excel file (`Statistika.xlsx`) for its data input. The columns used for the independent variable `X` (`Biaya Promosi (X)`) and dependent variable `Y` (`Penjualan (Y)`) are also hardcoded within `RegresiLinear.py`.

To use different data or columns, you would need to:
1.  Replace `Statistika.xlsx` with your own `.xlsx` file.
2.  Modify the `filename` variable in `RegresiLinear.py`.
3.  Adjust the column names for `X_column` and `Y_column` within `RegresiLinear.py` to match your dataset.

## 🤝 Contributing

We welcome contributions to enhance this project! If you have suggestions for improvements, new features, or bug fixes, please open an issue or submit a pull request.

## 📄 License

This project currently has no specific license. For future contributions or use in other projects, consider adding a suitable open-source license.

## 🙏 Acknowledgments

-   **pandas**: For robust data manipulation and analysis.
-   **NumPy**: For fundamental numerical computing.
-   **Matplotlib**: For creating static, interactive, and animated visualizations in Python.
-   **scikit-learn**: For powerful machine learning tools and algorithms.

## 📞 Support & Contact

If you encounter any issues or have questions, please use the [GitHub Issues](https://github.com/rzr06/Regresi-Linear-Sederhana/issues) page.

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [rzr06](https://github.com/rzr06)

</div>

