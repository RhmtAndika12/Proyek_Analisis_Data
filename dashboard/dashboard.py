import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title('Dashboard Sederhana')
    st.text('made by Rahmat Yuli Andika')
    
    # Membaca data dari file CSV
    file_path = 'https://github.com/RhmtAndika12/Proyek_Analisis_Data/blob/main/dashboard/all_data.csv' 
    data = pd.read_csv(file_path)

    # Menampilkan opsi visualisasi menggunakan radio button
    st.sidebar.title('Pilih Visualisasi')
    option = st.sidebar.radio('',
                              ('Histogram Jumlah Sewa Sepeda', 'Perbandingan Musim dengan Jumlah Sewa Sepeda'))

    # Visualisasi berdasarkan opsi yang dipilih
    if option == 'Histogram Jumlah Sewa Sepeda':
        plot_histogram(data)
        st.markdown("""
        ### Conclusion
        **Bagaimana pola penyewaan sepeda harian berubah seiring waktu (bulan dan jam)?**
        Jumlah penyewaan sepeda menunjukkan peningkatan pada bulan September dan Juni. Di sisi lain, peningkatan jumlah penyewaan sepeda terjadi sekitar pukul 8 pagi dan sekitar pukul 5 atau 6 sore jika dilihat dari perspektif jam.

        """)
    elif option == 'Perbandingan Musim dengan Jumlah Sewa Sepeda':
        plot_perbandingan_musim(data)
        st.markdown("""
        ### Conclusion
        
        **Adakah perbedaan dalam frekuensi sewa sepeda harian antara hari kerja (workingday) dan hari libur (holiday)?**
        Ada peningkatan jumlah penyewaan sepeda pada hari kerja dibandingkan dengan hari libur.
        """)

def plot_histogram(data):
    st.subheader('Histogram Jumlah Sewa Sepeda')
    # Visualisasi menggunakan histogram dengan seaborn
    sns.histplot(data['cnt_daily'], bins=30, kde=True)
    plt.xlabel('Jumlah Sewa Sepeda Harian')
    plt.ylabel('Frekuensi')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

def plot_perbandingan_musim(data):
    st.subheader('Perbandingan Musim dengan Jumlah Sewa Sepeda')
    # Visualisasi menggunakan boxplot untuk perbandingan musim dengan seaborn
    fig, ax = plt.subplots()
    sns.boxplot(x="season_daily", y="cnt_daily", data=data, ax=ax)
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Sewa Sepeda Harian')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
