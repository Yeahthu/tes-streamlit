import streamlit as st
from PIL import Image

def load_image(image_path):
    return Image.open(image_path)

def main():
    st.set_page_config(page_title='Smart Hidroponik', layout='wide')
    
    # Load images
    bg_image = load_image("bgHidroponik.jpg")
    logo_image = load_image("logo fixx1.png")
    icon_ph = load_image("icon_pH.png")
    icon_suhu = load_image("icon_suhu_air.png")
    icon_nutrisi = load_image("icon_tds.png")

    # Render images using st.image
    st.image(bg_image, caption='Background Image', use_column_width=True)
    st.image(logo_image, caption='Logo', width=100)
    st.image(icon_ph, caption='Icon pH', width=50)
    st.image(icon_suhu, caption='Icon Suhu', width=50)
    st.image(icon_nutrisi, caption='Icon Nutrisi', width=50)
    
    # CSS custom
    desain = """
         <style>
              body {
                 font-family: sans-serif;
                 margin: 0;
                 padding: 0;
                 background-color: #ffffff;
              }
              .custom-text {
                 color: #ff6347; /* Warna teks: Tomato */
              }
         </style>
    """
    st.markdown(desain, unsafe_allow_html=True)
    
    # HTML content with data-testid
    st.markdown("""
        <div id="Tampilan" data-testid="main-container">
            <div class="bagian-header" data-testid="header">
                <img src="data:image/png;base64,{logo_image}" alt="logo" id="logo" data-testid="logo">
            </div>
            <h1 class="judul-overview custom-text" data-testid="overview-title">Ringkasan Hidroponik</h1>

            <div class="bagian-utama" data-testid="main-content">
                <div class="sensor" data-testid="sensor-ph">
                    <img src="data:image/png;base64,{icon_ph}" alt="icon_pH" id="icon_pH" data-testid="icon-ph" />
                    <h2 class="custom-text">pH Air</h2>
                    <div class="bagian_ph custom-text">
                        <span class="value">7.0</span>
                        <span class="unit">pH</span>
                    </div>
                </div>
                <div class="sensor" data-testid="sensor-suhu">
                    <img src="data:image/png;base64,{icon_suhu}" alt="icon_suhu" id="icon_suhu" data-testid="icon-suhu" /> 
                    <h2 class="custom-text">Suhu Air</h2>
                    <div class="bagian_suhu custom-text">
                        <span class="value">22</span>
                        <span class="unit">°C</span>
                    </div>
                </div>
                <div class="sensor" data-testid="sensor-nutrisi">
                    <img src="data:image/png;base64,{icon_nutrisi}" alt="icon_nutrisi" id="icon_nutrisi" data-testid="icon-nutrisi" />
                    <h2 class="custom-text">Nutrisi</h2>
                    <div class="bagian_nutrisi custom-text">
                        <span class="value">100</span>
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

            slider.oninput = function() {
              output.innerHTML = this.value;
            }
        </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
