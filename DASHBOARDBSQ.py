import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO

# Set judul dan ikon pada browser
st.set_page_config(
    page_title='BSQ BCA KCU GADING SERPONG',
    page_icon='📈',
    layout='wide'
)

# Sidebar logo (tampilan lebih proporsional)
st.sidebar.image('logo.png', width=150)

# Judul
st.title("📊 Dashboard Analisis - BSQ BCA KCU GADING SERPONG")

# Upload file Excel
uploaded_file = st.file_uploader("Unggah file Excel", type=["xlsx", "xls"])
