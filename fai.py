import streamlit as st
from PIL import Image
from pymongo import MongoClient
from datetime import datetime as dt
import requests

# Fungsi Streamlit
def streamlit_app():
    st.set_page_config(page_title='Smart Hidroponik', layout='wide')

    # Koneksi ke MongoDB
    client = MongoClient('mongodb+srv://SmartHidroponik:MERA_X@smarthidroponik.hdetbis.mongodb.net/?retryWrites=true&w=majority&appName=SmartHidroponik')
    db = client['Smart_Hidroponik']
    collection = db['Sensor']
    # flask_url = "http://192.168.1.22:5000"
    # try:
    #     response = requests.get(flask_url)
    #     if response.status_code == 200:
    #         data = response.json()
    #         latest_data = data[-1] if data else None
    #         st.write("Data terbaru:", latest_data)
    #     else:
    #         st.error("Gagal mendapatkan data dari server Flask")
    # except requests.exceptions.ConnectionError as e:
    #     st.error(f"Terjadi kesalahan dalam menghubungi server Flask p: {e}")
    # Ambil data dari MongoDB
    # data = list(collection.find({}, {'_id': 0, 'pH': 1, 'suhu': 1, 'tds': 1, 'timestamp': 1}).sort('timestamp', -1).limit(10))
    # latest_data = data[-1] if data else None
   # latest_data = collection.find_one({}, {'_id': 0, 'pH': 1, 'suhu': 1, 'tds': 1, 'timestamp': 1}, sort=[('timestamp', -1)])
    latest_data_cursor = collection.find({}, {'_id': 0, 'pH': 1, 'suhu': 1, 'tds': 1, 'timestamp': 1}).sort('timestamp', -1).limit(1)
    latest_data = list(latest_data_cursor)[0] if latest_data_cursor.count() > 0 else None
    
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
                 height: 120px;
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
              input[type=range] {
                 -webkit-appearance: none;
                 width: 100%;
                 margin: 30px 0;
              }
              input[type=range]:focus {
                 outline: none;
              }
              input[type=range]::-webkit-slider-runnable-track {
                 width: 100%;
                 height: 8.4px;
                 cursor: pointer;
                 border-radius: 10px;
                 border: 0.2px solid #010101;
                 background: linear-gradient(to right, 
                               red 0%, rgb(255, 149, 0) 20%,
                               rgb(36, 249, 3) 30%, rgb(2, 82, 2) 50%,
                               rgb(45, 1, 76) 80%, purple 100%);
              }
              input[type=range]::-webkit-slider-thumb {
                 -webkit-appearance: none;
                 height: 20px;
                 width: 20px;
                 border-radius: 50%;
                 background-color: transparent;
                 background-image: url('https://raw.githubusercontent.com/Yeahthu/tes-streamlit/main/kursor.png');
                 background-size: cover;
                 cursor: pointer;
                 box-shadow: 0 0 2px rgba(0, 0, 0, 0.3);
                 margin-top: -18px;
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
                    <input type="range" min="1" max="14" value="5" class="scrollbar-horizontal" id="myRange" data-testid="ph-range">
                    <div class="ph-labels custom-text">
                        <div class="ph-label">Kadar rendah</div>
                        <div class="ph-label">Kadar sesuai</div>
                        <div class="ph-label">Kadar tinggi</div>
                    </div>
                    <div class="ph-labels custom-text">
                        <div class="ph-label">[1-4]</div>
                        <div class="ph-label">[5-7]</div>
                        <div class="ph-label">[9-14]</div>
                    </div>
                    <p class="custom-text">pH tanamanmu: <span id="demo">5</span></p>
                </div>
            </div>
        </div>
        <script>
            var slider = document.getElementById("myRange");
            var output = document.getElementById("demo");
            output.innerHTML = slider.value;

            slider.oninput = function() {{
                output.innerHTML = this.value;
            }} 
        </script>
        """
    st.markdown(html_content, unsafe_allow_html=True)

if __name__ == "__main__":
    # Jalankan Streamlit
    streamlit_app()
