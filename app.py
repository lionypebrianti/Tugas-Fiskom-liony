import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Analisis Nilai Siswa", layout="wide")

st.title("📊 Dashboard Analisis Data 50 Siswa - 20 Soal")

# Upload file
uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.subheader("📋 Data Mentah")
    st.dataframe(df)

    # Statistik Deskriptif
    st.subheader("📈 Statistik Deskriptif")
    st.write(df.describe())

    # Sidebar untuk memilih kolom
    st.sidebar.header("Pengaturan Visualisasi")
    kolom = st.sidebar.selectbox("Pilih Kolom", df.columns)

    # Diagram Batang
    st.subheader("📊 Diagram Batang")
    fig1, ax1 = plt.subplots()
    df[kolom].value_counts().sort_index().plot(kind='bar', ax=ax1)
    st.pyplot(fig1)

    # Histogram
    st.subheader("📉 Histogram")
    fig2, ax2 = plt.subplots()
    ax2.hist(df[kolom], bins=10)
    ax2.set_xlabel(kolom)
    ax2.set_ylabel("Frekuensi")
    st.pyplot(fig2)

    # Boxplot
    st.subheader("📦 Boxplot")
    fig3, ax3 = plt.subplots()
    ax3.boxplot(df[kolom])
    ax3.set_title(f"Boxplot {kolom}")
    st.pyplot(fig3)

    # Rata-rata per Soal
    st.subheader("📌 Rata-rata Skor Per Soal")
    mean_per_soal = df.mean()
    fig4, ax4 = plt.subplots(figsize=(10,5))
    mean_per_soal.plot(kind='bar', ax=ax4)
    ax4.set_ylabel("Rata-rata")
    st.pyplot(fig4)

    # Distribusi Total Nilai per Siswa
    st.subheader("🎯 Distribusi Total Nilai per Siswa")
    df["Total_Nilai"] = df.sum(axis=1)
    fig5, ax5 = plt.subplots()
    ax5.hist(df["Total_Nilai"], bins=10)
    ax5.set_xlabel("Total Nilai")
    ax5.set_ylabel("Jumlah Siswa")
    st.pyplot(fig5)

    # Heatmap Korelasi
    st.subheader("🔥 Heatmap Korelasi Antar Soal")
    fig6, ax6 = plt.subplots(figsize=(12,8))
    sns.heatmap(df.corr(), annot=False, cmap="coolwarm", ax=ax6)
    st.pyplot(fig6)

else:
    st.info("Silakan upload file Excel terlebih dahulu.")