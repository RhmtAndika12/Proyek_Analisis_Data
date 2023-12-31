# Dashboard Analisis Sewa Sepeda
Ini adalah dashboard analisis sewa sepeda yang dibuat oleh Rahmat Yuli Andika menggunakan Streamlit. Dashboard ini memanfaatkan data sewa sepeda dari file CSV yang disediakan.

## Tentang Kode
1. Source RAW Data : https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset
2. Hasil Dashboard : https://a9avt3zz4oxpwg6vzktots.streamlit.app/
3. Proses Analisis : https://github.com/RhmtAndika12/Proyek_Analisis_Data/blob/main/data/Proyek_Analisis_Data.ipynb
4. Streamlit       : https://streamlit.io/
5. Pandas          : https://pandas.pydata.org/
6. Seaborn         : https://seaborn.pydata.org/
7. matplotlib      : https://matplotlib.org/

### Library yang Digunakan
- `streamlit` untuk membuat aplikasi web.
- `pandas` untuk manipulasi dan analisis data.
- `seaborn` dan `matplotlib` untuk visualisasi data.

### Setup environment
```
conda create --name main-ds python=3.12
conda activate main-ds
pip install numpy
pip install pandas
pip install seaborn
pip install matplotlib
pip install streamlit
pip install jupyter

```
### Run Streamlit App
```
streamlit run dashboard.py
```
### Cara Menggunakan 
1. Pastikan Anda memiliki semua library yang diperlukan terinstall.
2. buka kode editor(spt : Visual Studio) untuk menjalankan dashboard.py , pastikan membuka kode editor dengan satu folder dashboard ketika membuka agar ketika membuka dashboard.py, streamlit dapat terbaca dan berjalan,jika tidak maka akan terbaca file not found,untuk menambahkan folder tekan ctrl+k ctrl+o, kemudian cari folder dashboard.
3. Jalankan kode pada terminal menggunakan Python dengan kode :
  ```
  streamlit run dashboard.py
  ```
4. Dashboard akan ditampilkan dalam browser secara lokal.

