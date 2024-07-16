import streamlit as st
from pymongo import MongoClient
import time

# Fungsi Streamlit
def streamlit_app():
    st.set_page_config(page_title='Smart Hidroponik', layout='wide')

    # Koneksi ke MongoDB
    client = MongoClient('mongodb+srv://SmartHidroponik:MERA_X@smarthidroponik.hdetbis.mongodb.net/?retryWrites=true&w=majority&appName=SmartHidroponik')
    db = client['Smart_Hidroponik']
    collection = db['Sensor']

    # Ambil data dari MongoDB
    def get_latest_ph():
        latest_data_cursor = collection.find({}, {'_id': 0, 'pH': 1}).sort('waktu', -1).limit(1)
        latest_data = list(latest_data_cursor)
        return latest_data[0]['pH'] if latest_data else None

    # CSS custom
    desain_css = """
    <style>
        body {
            font-family: sans-serif;
            margin: 0;
            padding: 0;
            background-color: white;
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
        .custom-text {
            color: #ff6347; /* Warna teks: Tomato */
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

    while True:
        # Load initial pH value
        ph_value = get_latest_ph()

        if ph_value is not None:
            # HTML content
            html_content = f"""<div id="Tampilan" data-testid="main-container">
                    <div class="bagian-header" data-testid="header">
                        <img src="https://raw.githubusercontent.com/Yeahthu/tes-streamlit/main/logo%20fixx1.png" alt="logo" id="logo" data-testid="logo">
                    </div>
                    <h1 class="judul-overview custom-text" data-testid="overview-title">Ringkasan Hidroponik</h1>
                    <div class="bagian-utama" data-testid="main-content">
                        <div class="sensor" data-testid="sensor-ph">
                            <h2 class="custom-text">pH Air</h2>
                            <div class="bagian_ph custom-text">
                                <span class="value">{ph_value}</span>
                                <span class="unit">pH</span>
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
                </div>
                <script>
        setInterval(function() {{
            var ph_value = {ph_value};
            document.getElementById("demo").textContent = ph_value;
        }}, 5000); 
        </script>
                """

            st.markdown(html_content, unsafe_allow_html=True)

            # Delay sebelum mengambil data terbaru lagi
            time.sleep(10)

        else:
            st.write('Tidak ada data pH yang tersedia saat ini.')

if __name__ == "__main__":
    # Jalankan Streamlit
    streamlit_app()
