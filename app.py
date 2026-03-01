import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Analisis Nilai", layout="wide")

st.title("📊 Dashboard Analisis 50 Siswa - 20 Soal")

# Load data langsung dari file
@st.cache_data
def load_data():
    return pd.read_excel("data_simulasi_50_siswa_20_soal.xlsx")

try:
    df = load_data()
except:
    st.error("File data_simulasi_50_siswa_20_soal.xlsx tidak ditemukan.")
    st.stop()

st.subheader("📋 Data Mentah")
st.dataframe(df)

# Ambil hanya kolom numerik (nilai soal)
df_numerik = df.select_dtypes(include="number")

# ===============================
# SIDEBAR FILTER
# ===============================
st.sidebar.header("Pengaturan Analisis")

kolom = st.sidebar.selectbox(
    "Pilih Soal untuk Analisis Individu",
    df_numerik.columns
)

# ===============================
# STATISTIK DESKRIPTIF
# ===============================
st.subheader("📈 Statistik Deskriptif")
st.write(df_numerik.describe())

# ===============================
# RATA-RATA PER SOAL
# ===============================
st.subheader("📊 Rata-rata Skor Per Soal")
mean_per_soal = df_numerik.mean()

fig1, ax1 = plt.subplots(figsize=(10,5))
mean_per_soal.plot(kind='bar', ax=ax1)
ax1.set_ylabel("Rata-rata")
ax1.set_xlabel("Soal")
st.pyplot(fig1)

# ===============================
# DISTRIBUSI TOTAL NILAI
# ===============================
st.subheader("🎯 Distribusi Total Nilai Siswa")
df["Total_Nilai"] = df_numerik.sum(axis=1)

fig2, ax2 = plt.subplots()
ax2.hist(df["Total_Nilai"], bins=10)
ax2.set_xlabel("Total Nilai")
ax2.set_ylabel("Jumlah Siswa")
st.pyplot(fig2)

# ===============================
# ANALISIS PER SOAL (PILIHAN SIDEBAR)
# ===============================
st.subheader(f"📌 Analisis {kolom}")

col1, col2 = st.columns(2)

with col1:
    fig3, ax3 = plt.subplots()
    ax3.hist(df[kolom], bins=10)
    ax3.set_title("Histogram")
    st.pyplot(fig3)

with col2:
    fig4, ax4 = plt.subplots()
    ax4.boxplot(df[kolom])
    ax4.set_title("Boxplot")
    st.pyplot(fig4)

# ===============================
# HEATMAP KORELASI
# ===============================
st.subheader("🔥 Heatmap Korelasi Antar Soal")

fig5, ax5 = plt.subplots(figsize=(12,8))
sns.heatmap(df_numerik.corr(), cmap="coolwarm", annot=False, ax=ax5)
st.pyplot(fig5)

# ===============================
# RANKING SISWA
# ===============================
st.subheader("🏆 Ranking Siswa Berdasarkan Total Nilai")

df_ranking = df.sort_values(by="Total_Nilai", ascending=False)
st.dataframe(df_ranking)