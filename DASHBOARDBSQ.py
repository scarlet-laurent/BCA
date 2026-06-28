import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Dashboard Monitoring BSQ",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.image("logo.png", width=170)
st.sidebar.title("Dashboard BSQ")

st.title("📊 Dashboard Monitoring BSQ")
st.markdown("### Business Service Quality (BSQ) Customer Service")

uploaded_file = st.file_uploader(
    "Upload Data BSQ (.xlsx)",
    type=["xlsx", "xls"]
)

# ==========================================
# JIKA FILE BELUM DIUPLOAD
# ==========================================
if uploaded_file is None:
    st.info("Silakan upload file Excel terlebih dahulu.")
    st.stop()

# ==========================================
# LOAD DATA
# ==========================================
df = pd.read_excel(uploaded_file)

df["Tanggal"] = pd.to_datetime(df["Tanggal"], dayfirst=True)

# ==========================================
# FILTER
# ==========================================
st.sidebar.subheader("Filter Data")

def selectbox_all(label, column):

    pilihan = st.sidebar.selectbox(
        label,
        ["All"] + sorted(column.unique())
    )

    if pilihan == "All":
        return column.unique()

    return [pilihan]

cso_filter = selectbox_all("Nama CSO", df["Nama CSO"])
cabang_filter = selectbox_all("Cabang", df["Cabang"])
produk_filter = selectbox_all("Produk", df["Produk yang Diminati"])

df = df[
    df["Nama CSO"].isin(cso_filter) &
    df["Cabang"].isin(cabang_filter) &
    df["Produk yang Diminati"].isin(produk_filter)
]

# ==========================================
# KPI
# ==========================================

st.subheader("Ringkasan Data")

k1,k2,k3,k4 = st.columns(4)

k1.metric("Total Survey", len(df))
k2.metric("Nilai Pelayanan", round(df["Nilai Pelayanan"].mean(),2))
k3.metric("Nilai Penyambutan", round(df["Nilai Penyambutan"].mean(),2))
k4.metric("Jumlah CSO", df["Nama CSO"].nunique())

st.divider()

# ==========================================
# GRAFIK BARIS 1
# ==========================================

col1,col2 = st.columns(2)

with col1:

    st.subheader("Survey per Cabang")

    cabang = df.groupby("Cabang").size().reset_index(name="Jumlah")

    chart = alt.Chart(cabang).mark_bar().encode(
        x="Cabang:N",
        y="Jumlah:Q",
        color="Cabang:N",
        tooltip=["Cabang","Jumlah"]
    )

    st.altair_chart(chart,use_container_width=True)

with col2:

    st.subheader("Survey per CSO")

    cso = df.groupby("Nama CSO").size().reset_index(name="Jumlah")

    chart = alt.Chart(cso).mark_bar().encode(
        x="Jumlah:Q",
        y=alt.Y("Nama CSO:N",sort="-x"),
        color="Nama CSO:N",
        tooltip=["Nama CSO","Jumlah"]
    )

    st.altair_chart(chart,use_container_width=True)

# ==========================================
# GRAFIK BARIS 2
# ==========================================

col3,col4 = st.columns(2)

with col3:

    st.subheader("Produk yang Diminati")

    produk = df["Produk yang Diminati"].value_counts()

    fig,ax = plt.subplots(figsize=(5,5))

    ax.pie(
        produk,
        labels=produk.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

with col4:

    st.subheader("Trend Survey Harian")

    trend = df.groupby("Tanggal").size().reset_index(name="Jumlah")

    chart = alt.Chart(trend).mark_line(
        point=True
    ).encode(
        x="Tanggal:T",
        y="Jumlah:Q",
        tooltip=["Tanggal","Jumlah"]
    )

    st.altair_chart(chart,use_container_width=True)

st.divider()

# ==========================================
# TABEL
# ==========================================

st.subheader("Detail Data BSQ")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download CSV",
    csv,
    "Data_BSQ.csv",
    "text/csv"
)
