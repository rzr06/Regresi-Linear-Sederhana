import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

# Dataset dengan 30 data
data = {
    'Waktu Tidur (Jam)':    [7.0, 7.0, 6.0, 6.0, 4.0, 8.0, 6.0, 5.0, 6.0, 5.0, 7.0, 7.0, 5.0, 4.0, 7.0, 5.0,
                            8.0, 6.0, 6.0, 6.0, 7.0, 6.0, 6.0, 5.0, 4.0, 5.0, 8.0, 10.0, 7.0, 7.0, 6.0],
    'IPS':  [3.1, 3.6, 3.4, 3.6, 2.8, 4.0, 3.5, 3.4, 3.6, 3.4, 3.3, 3.8, 3.8, 3.4, 3.0, 3.6,
            3.5, 3.3, 3.6, 3.3, 4.0, 3.7, 3.9, 2.8, 3.0, 3.3, 3.5, 4.0, 3.4, 4.0, 3.2 ]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menghitung rata-rata X dan Y
X_mean = df['Waktu Tidur (Jam)'].mean()
Y_mean = df['IPS'].mean()

# Menghitung koefisien regresi (b)
numerator = np.sum((df['Waktu Tidur (Jam)'] - X_mean) * (df['IPS'] - Y_mean))
denominator = np.sum((df['Waktu Tidur (Jam)'] - X_mean) ** 2)
b = numerator / denominator

# Menghitung intercept (a)
a = Y_mean - b * X_mean

# Membuat prediksi berdasarkan persamaan regresi manual
X = df['Waktu Tidur (Jam)']
Y_pred = a + b * X

# Menghitung MSE dan R-Squared
mse = mean_squared_error(df['IPS'], Y_pred)
r2 = r2_score(df['IPS'], Y_pred)

print("Koefisien regresi (b):", b)
print("Intercept (a):", a)
print("Mean Squared Error (MSE):", mse)
print("R-Squared (R²):", r2)

# Visualisasi hasil regresi
plt.scatter(X, df['IPS'], color='blue', label='Data Aktual')
plt.plot(X, Y_pred, color='red', label='Regresi Manual')
plt.xlabel('Waktu Tidur (Jam)')
plt.ylabel('IPS')
plt.title('Hubungan Waktu Tidur dengan IPS (Regresi Manual)')
plt.legend()
plt.show()
