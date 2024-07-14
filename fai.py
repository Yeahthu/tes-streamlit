import streamlit as st

# Tambahkan CSS kustom
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fefbd8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul aplikasi
st.title("Aplikasi Streamlit dengan Latar Belakang Kustom")

# Konten aplikasi
st.write("Ini adalah contoh aplikasi Streamlit dengan latar belakang yang telah diubah warnanya.")
st.write("Anda dapat menambahkan lebih banyak konten di sini.")

# Input dari pengguna
name = st.text_input("Masukkan nama Anda:")
if name:
    st.write(f"Halo, {name}!")
