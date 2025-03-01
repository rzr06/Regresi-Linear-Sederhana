## Analisis Regresi Linear

Kode ini melakukan analisis regresi linear sederhana secara manual dan menguji signifikansi model dengan langkah-langkah berikut:

### 1. Persiapan Data
- Membaca dataset yang terdiri dari 30 observasi
- Variabel independen (X) dan dependen (Y) disimpan dalam DataFrame
- Menghitung mean dari X dan Y

### 2. Perhitungan Koefisien Regresi
**Persamaan Regresi**: Ŷ = a + bX
- Menghitung slope (b) menggunakan rumus:
  ```math
  b = Σ[(X_i - X̄)(Y_i - Ȳ)] / Σ(X_i - X̄)²
  
Menghitung intercept (a) menggunakan:
a = Ȳ - bX̄

### 3. Evaluasi Model
  a. Mean Squared Error (MSE): Mengukur rata-rata kuadrat error
  b. R-squared (R²): Mengukur proporsi variansi yang dijelaskan model
  c.F-statistik: Menguji signifikansi model secara keseluruhan
  F = (R²/k) / [(1-R²)/(n-k-1)]
  dimana k = jumlah variabel independen

### 4. Uji Signifikansi
  a. Menghitung p-value menggunakan distribusi F
  b. Membandingkan p-value dengan α = 0.05
  c. Menarik kesimpulan signifikansi hubungan linier

### 5. Visualisasi
  a. Menampilkan scatter plot data aktual
  b. Menampilkan garis regresi linear
  c. Menyajikan error (ε) untuk tiap observasi

###Output Utama
  1. Parameter model (a dan b)
  2. Metrik evaluasi (MSE dan R²)
  3. Hasil uji statistik (F-statistic dan p-value)
  4. Visualisasi hubungan X-Y
  5. Daftar error untuk tiap data point

###Penggunaan
Kode ini dapat digunakan untuk:
  1. Memahami implementasi manual regresi linear
  2. Menganalisis hubungan antara dua variabel numerik
  3. Melakukan uji signifikansi model regresi
  5. Memvisualisasikan hasil regresi linear
