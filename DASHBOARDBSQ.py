# import pandas as pd
# import streamlit as st
# import altair as alt
# import matplotlib.pyplot as plt

# # ==========================================
# # KONFIGURASI HALAMAN
# # ==========================================
# st.set_page_config(
#     page_title="Dashboard Monitoring BSQ",
#     page_icon="📊",
#     layout="wide"
# )

# # ==========================================
# # SIDEBAR
# # ==========================================
# st.sidebar.image("logo.png", width=170)
# st.sidebar.title("Dashboard BSQ")

# st.title("📊 Dashboard Monitoring BSQ")
# st.markdown("### Business Service Quality (BSQ) Customer Service")

# uploaded_file = st.file_uploader(
#     "Upload Data BSQ (.xlsx)",
#     type=["xlsx", "xls"]
# )

# # ==========================================
# # JIKA FILE BELUM DIUPLOAD
# # ==========================================
# if uploaded_file is None:
#     st.info("Silakan upload file Excel terlebih dahulu.")
#     st.stop()

# # ==========================================
# # LOAD DATA
# # ==========================================
# df = pd.read_excel(uploaded_file)

# df["Tanggal"] = pd.to_datetime(df["Tanggal"], dayfirst=True)

# # ==========================================
# # FILTER
# # ==========================================
# st.sidebar.subheader("Filter Data")

# def selectbox_all(label, column):

#     pilihan = st.sidebar.selectbox(
#         label,
#         ["All"] + sorted(column.unique())
#     )

#     if pilihan == "All":
#         return column.unique()

#     return [pilihan]

# cso_filter = selectbox_all("Nama CSO", df["Nama CSO"])
# cabang_filter = selectbox_all("Cabang", df["Cabang"])
# produk_filter = selectbox_all("Produk", df["Produk yang Diminati"])

# df = df[
#     df["Nama CSO"].isin(cso_filter) &
#     df["Cabang"].isin(cabang_filter) &
#     df["Produk yang Diminati"].isin(produk_filter)
# ]

# # ==========================================
# # KPI
# # ==========================================

# st.subheader("Ringkasan Data")

# k1,k2,k3,k4 = st.columns(4)

# k1.metric("Total Survey", len(df))
# k2.metric("Nilai Pelayanan", round(df["Nilai Pelayanan"].mean(),2))
# k3.metric("Nilai Penyambutan", round(df["Nilai Penyambutan"].mean(),2))
# k4.metric("Jumlah CSO", df["Nama CSO"].nunique())

# st.divider()

# # ==========================================
# # GRAFIK BARIS 1
# # ==========================================

# col1,col2 = st.columns(2)

# with col1:

#     st.subheader("Survey per Cabang")

#     cabang = df.groupby("Cabang").size().reset_index(name="Jumlah")

#     chart = alt.Chart(cabang).mark_bar().encode(
#         x="Cabang:N",
#         y="Jumlah:Q",
#         color="Cabang:N",
#         tooltip=["Cabang","Jumlah"]
#     )

#     st.altair_chart(chart,use_container_width=True)

# with col2:

#     st.subheader("Survey per CSO")

#     cso = df.groupby("Nama CSO").size().reset_index(name="Jumlah")

#     chart = alt.Chart(cso).mark_bar().encode(
#         x="Jumlah:Q",
#         y=alt.Y("Nama CSO:N",sort="-x"),
#         color="Nama CSO:N",
#         tooltip=["Nama CSO","Jumlah"]
#     )

#     st.altair_chart(chart,use_container_width=True)

# # ==========================================
# # GRAFIK BARIS 2
# # ==========================================

# col3,col4 = st.columns(2)

# with col3:

#     st.subheader("Produk yang Diminati")

#     produk = df["Produk yang Diminati"].value_counts()

#     fig,ax = plt.subplots(figsize=(5,5))

#     ax.pie(
#         produk,
#         labels=produk.index,
#         autopct="%1.1f%%",
#         startangle=90
#     )

#     ax.axis("equal")

#     st.pyplot(fig)

# with col4:

#     st.subheader("Trend Survey Harian")

#     trend = df.groupby("Tanggal").size().reset_index(name="Jumlah")

#     chart = alt.Chart(trend).mark_line(
#         point=True
#     ).encode(
#         x="Tanggal:T",
#         y="Jumlah:Q",
#         tooltip=["Tanggal","Jumlah"]
#     )

#     st.altair_chart(chart,use_container_width=True)

# st.divider()

# # ==========================================
# # TABEL
# # ==========================================

# st.subheader("Detail Data BSQ")

# st.dataframe(
#     df,
#     use_container_width=True,
#     hide_index=True
# )

# csv = df.to_csv(index=False).encode("utf-8")

# st.download_button(
#     "📥 Download CSV",
#     csv,
#     "Data_BSQ.csv",
#     "text/csv"
# )



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
# =====================================================
# BARIS PERTAMA VISUALISASI
# =====================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("📈 Trend Survey Harian")

    trend_harian = (
        df.groupby("Tanggal")
        .size()
        .reset_index(name="Jumlah Survey")
    )

    chart = (
        alt.Chart(trend_harian)
        .mark_line(
            point=True,
            color="#005BAC",
            strokeWidth=3
        )
        .encode(
            x=alt.X("Tanggal:T", title="Tanggal"),
            y=alt.Y("Jumlah Survey:Q"),
            tooltip=["Tanggal", "Jumlah Survey"]
        )
        .properties(height=350)
    )

    st.altair_chart(chart, use_container_width=True)

with col2:

    st.subheader("🏢 Survey per Cabang")

    cabang = (
        df.groupby("Cabang")
        .size()
        .reset_index(name="Jumlah")
    )

    chart = (
        alt.Chart(cabang)
        .mark_bar(cornerRadiusTopLeft=5,
                  cornerRadiusTopRight=5)
        .encode(
            x="Cabang:N",
            y="Jumlah:Q",
            color=alt.Color(
                "Cabang:N",
                legend=None
            ),
            tooltip=["Cabang", "Jumlah"]
        )
        .properties(height=350)
    )

    st.altair_chart(chart, use_container_width=True)

st.markdown("---")

# =====================================================
# BARIS KEDUA
# =====================================================

col3, col4 = st.columns(2)

with col3:

    st.subheader("👩 Survey per Customer Service")

    cso = (
        df.groupby("Nama CSO")
        .size()
        .reset_index(name="Jumlah")
        .sort_values("Jumlah")
    )

    chart = (
        alt.Chart(cso)
        .mark_bar()
        .encode(
            x="Jumlah:Q",
            y=alt.Y(
                "Nama CSO:N",
                sort="-x"
            ),
            color=alt.Color(
                "Nama CSO:N",
                legend=None
            ),
            tooltip=["Nama CSO", "Jumlah"]
        )
        .properties(height=380)
    )

    st.altair_chart(chart, use_container_width=True)

with col4:

    st.subheader("💳 Produk yang Diminati")

    produk = df["Produk yang Diminati"].value_counts()

    fig, ax = plt.subplots(figsize=(5,5))

    ax.pie(
        produk,
        labels=produk.index,
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops=dict(edgecolor="white")
    )

    ax.axis("equal")

    st.pyplot(fig)

st.markdown("---")

# =====================================================
# BARIS KETIGA
# =====================================================

col5, col6 = st.columns(2)

with col5:

    st.subheader("📅 Trend Survey Bulanan")

    bulan = (
        df.groupby("Bulan")
        .size()
        .reset_index(name="Jumlah")
    )

    urutan = [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]

    chart = (
        alt.Chart(bulan)
        .mark_bar(color="#005BAC")
        .encode(
            x=alt.X(
                "Bulan:N",
                sort=urutan
            ),
            y="Jumlah:Q",
            tooltip=["Bulan","Jumlah"]
        )
        .properties(height=350)
    )

    st.altair_chart(chart, use_container_width=True)

with col6:

    st.subheader("🏆 Leaderboard Customer Service")

    leaderboard = (
        df.groupby("Nama CSO")
        .size()
        .reset_index(name="Total Survey")
        .sort_values(
            "Total Survey",
            ascending=False
        )
        .reset_index(drop=True)
    )

    leaderboard.index += 1

    st.dataframe(
        leaderboard,
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# BARIS KEEMPAT
# =====================================================

col7, col8 = st.columns(2)

with col7:

    st.subheader("📊 Persentase Cabang")

    persen = (
        df["Cabang"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
        .reset_index()
    )

    persen.columns = ["Cabang", "Persentase"]

    chart = (
        alt.Chart(persen)
        .mark_arc(innerRadius=70)
        .encode(
            theta="Persentase:Q",
            color="Cabang:N",
            tooltip=[
                "Cabang",
                "Persentase"
            ]
        )
        .properties(height=350)
    )

    st.altair_chart(chart, use_container_width=True)

with col8:

    st.subheader("📋 Produk Terlaris")

    produk = (
        df.groupby("Produk yang Diminati")
        .size()
        .reset_index(name="Jumlah")
        .sort_values("Jumlah")
    )

    chart = (
        alt.Chart(produk)
        .mark_bar(color="#005BAC")
        .encode(
            x="Jumlah:Q",
            y=alt.Y(
                "Produk yang Diminati:N",
                sort="-x"
            ),
            tooltip=[
                "Produk yang Diminati",
                "Jumlah"
            ]
        )
        .properties(height=350)
    )

    st.altair_chart(chart, use_container_width=True)

st.markdown("---")
# =====================================================
# TOP 5 CUSTOMER SERVICE
# =====================================================

st.markdown("## 🏆 Top 5 Customer Service")

top5 = (
    df.groupby("Nama CSO")
    .size()
    .reset_index(name="Total Survey")
    .sort_values("Total Survey", ascending=False)
    .head(5)
)

top5.index = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

st.dataframe(
    top5,
    use_container_width=True,
    hide_index=False
)

st.markdown("---")

# =====================================================
# REKAP PER CABANG
# =====================================================

st.markdown("## 🏢 Rekap Monitoring per Cabang")

rekap = (
    df.groupby("Cabang")
    .agg(
        Total_Survey=("Cabang","count"),
        Nilai_Pelayanan=("Nilai Pelayanan","mean"),
        Nilai_Penyambutan=("Nilai Penyambutan","mean")
    )
    .round(2)
    .reset_index()
)

st.dataframe(
    rekap,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# =====================================================
# PRODUK TERLARIS
# =====================================================

st.markdown("## 💳 Produk yang Paling Diminati")

produk = (
    df["Produk yang Diminati"]
    .value_counts()
    .reset_index()
)

produk.columns = [
    "Produk",
    "Jumlah Survey"
]

st.dataframe(
    produk,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# =====================================================
# DETAIL DATA
# =====================================================

st.markdown("## 📋 Detail Data BSQ")

search = st.text_input(
    "🔍 Cari Nama Nasabah"
)

if search:

    hasil = df[
        df["Nama Nasabah"]
        .str.contains(
            search,
            case=False
        )
    ]

    st.dataframe(
        hasil,
        use_container_width=True,
        hide_index=True
    )

else:

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

st.markdown("---")

# =====================================================
# DOWNLOAD CSV
# =====================================================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="Data_BSQ.csv",
    mime="text/csv"
)

# =====================================================
# DOWNLOAD EXCEL
# =====================================================

from io import BytesIO

output = BytesIO()

with pd.ExcelWriter(output, engine="openpyxl") as writer:
    df.to_excel(
        writer,
        index=False,
        sheet_name="BSQ"
    )

excel = output.getvalue()

st.download_button(
    label="📥 Download Excel",
    data=excel,
    file_name="Dashboard_BSQ.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.markdown("---")

# =====================================================
# DASHBOARD INFORMATION
# =====================================================

col1,col2,col3 = st.columns(3)

with col1:

    st.info(
        f"""
### 📅 Last Update

{pd.Timestamp.now().strftime('%d %B %Y')}
"""
    )

with col2:

    st.success(
        """
### 📊 Data Source

Google Form BSQ
"""
    )

with col3:

    st.warning(
        """
### ⚡ Monitoring

Realtime Dashboard
"""
    )

st.markdown("---")

st.caption(
"""
Dashboard Monitoring BSQ

Simplifikasi Monitoring BSQ melalui Google Form dan Dashboard Digital

Unit Customer Service Tahun 2026
"""
)
