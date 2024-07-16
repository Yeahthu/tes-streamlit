import streamlit as st
from PIL import Image
from pymongo import MongoClient
from datetime import datetime as dt
import time

# Fungsi Streamlit
def streamlit_app():
    st.set_page_config(page_title='Smart Hidroponik', layout='wide')

    # Koneksi ke MongoDB
    client = MongoClient('mongodb+srv://SmartHidroponik:MERA_X@smarthidroponik.hdetbis.mongodb.net/?retryWrites=true&w=majority&appName=SmartHidroponik')
    db = client['Smart_Hidroponik']
    collection = db['Sensor']
    
    latest_data_cursor = collection.find({}, {'_id': 0, 'pH': 1, 'suhu': 1, 'tds': 1, 'timestamp': 1}).sort('waktu',-1).limit(96)
    latest_data = list(latest_data_cursor)
    if latest_data:
        latest_data = latest_data[0]
    else:
        latest_data = None
    
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
              #Tampilan {
                 position: relative;
                 width: 100%;
                 margin: 10px auto;
                 background-color: #ffffff;
                 border-radius: 10px;
                 box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, 
                             rgba(0, 0, 0, 0.12) 0px -12px 30px, 
                             rgba(0, 0, 0, 0.12) 0px 4px 6px,
                             rgba(0, 0, 0, 0.17) 0px 12px 13px, 
                             rgba(0, 0, 0, 0.09) 0px -3px 5px;
              }
              .bagian-header {
                 background-image: url("https://raw.githubusercontent.com/Yeahthu/tes-streamlit/main/bgHidroponik.jpg");
                 border-radius: 10px 10px 0 0;
                 border-bottom: 2px solid #eb0e0e;
                 margin: 0;
                 padding: 10px;
                 background-position: center;
                 background-repeat: no-repeat;
                 background-size: cover;
                 text-align: center;
                 height: 350px;
              }
              #logo {
                 width: 15%;
                 border-radius: 30px;
              }
              .bagian-utama {
                 margin: 8px;
                 padding: 10px;
                 display: flex;
                 flex-wrap: wrap;
                 justify-content: space-between;
                 gap: 10px;
                 flex-direction: row;
              }
              .bagian-utama > * {
                 flex: 1;
                 text-align: center;
              }
              .judul-overview {
                 font-size: 24px;
                 font-weight: bold;
                 width: 100%;
                 text-align: center;
                 margin: 20px;
              }
              #icon_pH, #icon_suhu, #icon_nutrisi {
                 width: 25%;
              }
              .bagian_ph, .bagian_suhu, .bagian_nutrisi {
                 font-size: 24px;
                 font-weight: bold;
                 margin: 10px;
              }
              .unit {
                 font-size: 12px;
                 color: #eb0e0e;
                 vertical-align: middle;
              }
              .value {
                 color: rgb(0, 255, 30);
              }
              .bagian-akhir {
                 margin: 20px;
                 padding: 15px;
                 height: 20%;
                 background-color: #ffffff;
              }
              .status-hidroponik {
                 font-size: 24px;
                 font-weight: bold;
                 width: 100%;
                 text-align: left;
                 margin: 20px;
              }
              .batas-text {
                 font-family: 'Courier New', Courier, monospace;
                 font-size: 20px;
                 text-align: left;
                 margin: 0px;
              }
              .batas-ph {
                 width: 100%;
                 border-radius: 20px;
                 box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
                 background-color: antiquewhite;
              }
              .scrollbar-horizontal {
                 width: 100%;
                 height: 10px;
                 margin: 0px;
              }
              .stSlider .stSliderTrack, .stSlider .stSliderTrackValue, .stSlider .stSliderLabel {
                 background: linear-gradient(to right, 
                               red 0%, rgb(255, 149, 0) 20%,
                               rgb(36, 249, 3) 30%, rgb(2, 82, 2) 50%,
                               rgb(45, 1, 76) 80%, purple 100%);
                 border-radius: 10px;
              }
              .stSlider .stSliderTrackValue {
                 background: none;
              }
              .stSlider .stSliderLabelValue {
                 color: rgb(0, 255, 30);
              }
              .ph-labels {
                 display: flex;
                 justify-content: space-between;
                 margin-bottom: 10px;
                 font-size: 14px;
              }
              .ph-label {
                 width: 33.33%;
                 text-align: center;
              }
              .custom-text {
                 color: #ff6347; /* Warna teks: Tomato */
              }
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
            <h1 class="status-hidroponik custom-text" data-testid="status-title">Status hidroponik</h1>
            <div class="bagian-akhir" data-testid="footer">
                <div class="batas-ph" data-testid="ph-boundary">
                    <h1 class="batas-text custom-text">Batas pH</h1>
                    <div class="ph-labels custom-text">
                        <div class="ph-label">Kadar rendah</div>
                        <div class="ph-label">Kadar sesuai</div>
                        <div class="ph-label">Kadar tinggi</div>
                    </div>
                    <div class="ph-labels custom-text">
                        <div class="ph-label">[1-4]</div>
                        <div class="ph-label">[5-7]</div>
                        <div class="ph-label">[8-14]</div>
                    </div>
                    <p class="custom-text">pH tanamanmu: <span id="demo">{ph_value}</span></p>
                </div>
            </div>
        </div>"""
        
    st.markdown(html_content, unsafe_allow_html=True)

    # Membuat slider pH dengan Streamlit
    st.subheader("pH tanamanmu")
    if ph_value != 'N/A':
        ph_value = st.slider(
            'pH tanamanmu', 
            min_value=1.0, 
            max_value=14.0, 
            value=float(ph_value), 
            step=0.1, 
            key='auto_slider', 
            disabled=True
        )
    else:
        st.write('Tidak ada data pH yang tersedia saat ini.')

    # Delay sebelum mengambil data terbaru lagi
    time.sleep(10) 

if __name__ == "__main__":
    # Jalankan Streamlit
    streamlit_app()
