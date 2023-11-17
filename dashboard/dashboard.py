import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title('Dashboard Analisis Sewa Sepeda')
    st.text('Made by Rahmat Yuli Andika')

    # Membaca data dari file CSV
    file_path = 'all_data.csv'
    bike_sharing = pd.read_csv(file_path)

    st.markdown("""
    ## Pola Jumlah Sewa Sepeda Harian Berdasarkan Bulan
    """)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="mnth_daily", y="cnt_daily", data=bike_sharing, ci=None, ax=ax)
    plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Sewa Sepeda Harian")
    st.pyplot(fig)

    st.markdown("""
    ### Conclusion
    **Bagaimana pola penyewaan sepeda harian berubah seiring waktu (bulan dan jam)?**
    Jumlah penyewaan sepeda menunjukkan peningkatan pada bulan September dan Juni. Di sisi lain, peningkatan jumlah penyewaan sepeda terjadi sekitar pukul 8 pagi dan sekitar pukul 5 atau 6 sore jika dilihat dari perspektif jam.

    """)

    st.markdown("""
    ## Perbedaan Antara Hari Kerja dan Hari Libur dalam Jumlah Sewa Sepeda Harian
    """)
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="workingday_daily", y="cnt_daily", data=bike_sharing)
    plt.title("Perbedaan Antara Hari Kerja dan Hari Libur dalam Jumlah Sewa Sepeda Harian")
    plt.xlabel("Workingday")
    plt.ylabel("Jumlah Sewa Sepeda Harian")
    st.pyplot(fig)

    st.markdown("""
    ### Conclusion
    **Adakah perbedaan dalam frekuensi sewa sepeda harian antara hari kerja (workingday) dan hari libur (holiday)?**
    Ada peningkatan jumlah penyewaan sepeda pada hari kerja dibandingkan dengan hari libur.
    """)

if __name__ == "__main__":
    main()
