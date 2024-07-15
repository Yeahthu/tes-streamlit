import streamlit as st
from pymongo import MongoClient
from PIL import Image

# Fungsi Streamlit
def streamlit_app():
    st.set_page_config(page_title='Smart Hidroponik', layout='wide')

    # Koneksi ke MongoDB
    client = MongoClient('mongodb+srv://SmartHidroponik:MERA_X@smarthidroponik.hdetbis.mongodb.net/?retryWrites=true&w=majority&appName=SmartHidroponik')
    db = client['Smart_Hidroponik']
    collection = db['Sensor']

    # Ambil data terbaru dari MongoDB
    latest_data = collection.find_one({}, {'_id': 0, 'pH': 1, 'suhu': 1, 'tds': 1, 'timestamp': 1}, sort=[('timestamp', -1)])

    # Load images
    logo_url = "https://raw.githubusercontent.com/Yeahthu/tes-streamlit/main/logo%20fixx1.png"
    icon_ph_url = "https://raw.githubusercontent.com/Yeahthu/tes-streamlit/main/icon_pH.png"
    icon_suhu_url = "https://raw.githubusercontent.com/Yeahthu/tes-streamlit/main/icon_suhu_air.png"
    icon_nutrisi_url = "https://raw.githubusercontent.com/Yeahthu/tes-streamlit/main/icon_tds.png"

    # CSS custom
    desain_css = """
         <style>
              body {
                 font-family: sans-serif;
                 margin: 0;
                 padding: 0;
                 background-color: #ffffff;
              }
              /* CSS custom lainnya sesuai kebutuhan */
         </style>
    """
    st.markdown(desain_css, unsafe_allow_html=True)

    if latest_data:
        ph_value = latest_data.get('pH', 'N/A')
        suhu_value = latest_data.get('suhu', 'N/A')
        nutrisi_value = latest_data.get('tds', 'N/A')
    else:
        ph_value = 'N/A'
        suhu_value = 'N/A'
        nutrisi_value = 'N/A'

    # HTML content
    html_content = f"""<div id="Tampilan" data-testid="main-container">
            <div class="bagian-header" data-testid="header">
                <img src="{logo_url}" alt="logo" id="logo" data-testid="logo">
            </div>
            <h1 class="judul-overview custom-text" data-testid="overview-title">Ringkasan Hidroponik</h1>
            <div class="bagian-utama" data-testid="main-content">
                <div class="sensor" data-testid="sensor-ph">
                    <img src="{icon_ph_url}" alt="icon_pH" id="icon_pH" data-testid="icon-ph" />
                    <h2 class="custom-text">pH Air</h2>
                    <div class="bagian_ph custom-text">
                        <span class="value">{ph_value}</span>
                        <span class="unit">pH</span>
                    </div>
                </div>
                <div class="sensor" data-testid="sensor-suhu">
                    <img src="{icon_suhu_url}" alt="icon_suhu" id="icon_suhu" data-testid="icon-suhu" /> 
                    <h2 class="custom-text">Suhu Air</h2>
                    <div class="bagian_suhu custom-text">
                        <span class="value">{suhu_value}</span>
                        <span class="unit">°C</span>
                    </div>
                </div>
                <div class="sensor" data-testid="sensor-nutrisi">
                    <img src="{icon_nutrisi_url}" alt="icon_nutrisi" id="icon_nutrisi" data-testid="icon-nutrisi" />
                    <h2 class="custom-text">Nutrisi</h2>
                    <div class="bagian_nutrisi custom-text">
                        <span class="value">{nutrisi_value}</span>
                        <span class="unit">ppm</span>
                    </div>
                </div>
            </div>
        </div>
        """
    st.markdown(html_content, unsafe_allow_html=True)

if __name__ == "__main__":
    # Jalankan Streamlit
    streamlit_app()
