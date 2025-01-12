import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import f

# Dataset dengan 30 data
data = {
    'X':    [7.0, 7.0, 6.0, 6.0, 4.0, 8.0, 6.0, 5.0, 6.0, 5.0, 7.0, 7.0, 5.0, 4.0, 7.0, 5.0, 8.0, 6.0, 6.0, 6.0, 7.0, 6.0, 6.0, 5.0, 4.0, 5.0, 8.0, 10.0, 7.0, 7.0, 6.0],
    'Y':    [3.1, 3.6, 3.4, 3.6, 2.8, 4.0, 3.5, 3.4, 3.6, 3.4, 3.3, 3.8, 3.8, 3.4, 3.0, 3.6, 3.5, 3.3, 3.6, 3.3, 4.0, 3.7, 3.9, 2.8, 3.0, 3.3, 3.5, 4.0, 3.4, 4.0, 3.2]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menghitung rata-rata X dan Y
X_mean = df['X'].mean()
Y_mean = df['Y'].mean()

# Menghitung koefisien regresi (b)
numerator = np.sum((df['X'] - X_mean) * (df['Y'] - Y_mean))
denominator = np.sum((df['X'] - X_mean) ** 2)
b = numerator / denominator

# Menghitung intercept (a)
a = Y_mean - b * X_mean

# Membuat prediksi berdasarkan persamaan regresi manual
X = df['X']
Y_pred = a + b * X

# Menghitung error (epsilon)
epsilon = df['Y'] - Y_pred

# Menghitung MSE dan R-Squared
mse = mean_squared_error(df['Y'], Y_pred)
r2 = r2_score(df['Y'], Y_pred)

# Menghitung F-statistik
n = len(df)         # Jumlah data
DFn = 1             # Derajat kebebasan untuk model (jumlah prediktor)
DFd = n - 2         # Derajat kebebasan untuk error
F_stat = (r2 / DFn) / ((1 - r2) / DFd)

# Menghitung p-value menggunakan distribusi F
p_value = 1 - f.cdf(F_stat, DFn, DFd)

# Menampilkan hasil
print("Koefisien regresi (b):", b)
print("Intercept (a):", a)
print("Mean Squared Error (MSE):", mse)
print("R-Squared (R²):", r2)
print("\nF-statistik:", F_stat)
print("P-value:", p_value)
print("Derajat kebebasan (DFn, DFd):", (DFn, DFd))

# Menyimpulkan signifikansi hasil regresi
alpha = 0.05  # Tingkat signifikansi 5%
if p_value < alpha:
    print("Kesimpulan:  Slope signifikan secara statistik pada tingkat signifikansi 5% (p-value < 0.05).")
    print("             Ada hubungan linier yang signifikan antara X dan Y.")
else:
    print("Kesimpulan:  Slope tidak signifikan secara statistik pada tingkat signifikansi 5% (p-value >= 0.05).")
    print("             Tidak ada bukti yang cukup untuk menyimpulkan adanya hubungan linier antara X dan Y.")

print("\nError (epsilon) per data:")
print(epsilon)

# Visualisasi hasil regresi
plt.scatter(X, df['Y'], color='blue', label='Data Aktual')
plt.plot(X, Y_pred, color='red', label='Regresi Linear')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Hubungan X dengan Y (Regresi Linear)')
plt.legend()
plt.show()
