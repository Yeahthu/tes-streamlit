import streamlit as st

# Tambahkan CSS kustom
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fefbd8;
    }
    .custom-text {
        color: #ff6347; /* Warna teks: Tomato */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul aplikasi
st.title("Aplikasi Streamlit dengan Warna Teks Kustom")

# Konten aplikasi dengan gaya teks kustom
st.markdown('<p class="custom-text">Ini adalah contoh teks dengan warna kustom.</p>', unsafe_allow_html=True)
st.markdown('<p class="custom-text">Anda dapat menambahkan lebih banyak konten di sini dengan warna teks yang berbeda.</p>', unsafe_allow_html=True)

# Input dari pengguna
name = st.text_input("Masukkan nama Anda:")
if name:
    st.markdown(f'<p class="custom-text">Halo, {name}!</p>', unsafe_allow_html=True)
