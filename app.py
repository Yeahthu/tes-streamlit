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
    desain = """
         <style>
              body {
                 font-family: sans-serif;
                 margin: 0;
                 padding: 0;
                 background-color: #ffffff;
         }"""
    st.markdown(desain,unsafe_allow_html=True)

if __name__ == "__main__":
    main()

#      CSS styles
#     st.markdown(

             # Tampilan {
#                 position: relative;
#                 width: 50%;
#                 margin: 10px auto;
#                 background-color: #ffffff;
#                 border-radius: 10px;
#                 box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, 
#                             rgba(0, 0, 0, 0.12) 0px -12px 30px, 
#                             rgba(0, 0, 0, 0.12) 0px 4px 6px,
#                             rgba(0, 0, 0, 0.17) 0px 12px 13px, 
#                             rgba(0, 0, 0, 0.09) 0px -3px 5px;
#             }
#             .bagian-header {
#                 border-radius: 10px 10px 0 0;
#                 border-bottom: 2px solid #eb0e0e;
#                 margin: 0;
#                 padding: 10px;
#                 background-position: center;
#                 background-repeat: no-repeat;
#                 background-size: cover;
#                 background-position: center;
#                 text-align: center;
#                 height: 120px;
#             }
#             #logo {
#                 width: 15%;
#                 border-radius: 30px;
#             }
#             .bagian-utama {
#                 margin: 8px;
#                 padding: 10px;
#                 display: flex;
#                 flex-wrap: wrap;
#                 justify-content: space-between;
#                 gap: 10px;
#                 flex-direction: row;
#             }
#             .judul-overview {
#                 font-size: 24px;
#                 font-weight: bold;
#                 width: 100%;
#                 text-align: center;
#                 margin: 20px;
#             }
#             #icon_pH, #icon_suhu, #icon_nutrisi {
#                 width: 25%;
#             }
#             .bagian_ph, .bagian_suhu, .bagian_nutrisi {
#                 font-size: 24px;
#                 font-weight: bold;
#                 margin: 10px;
#             }
#             .unit {
#                 font-size: 12px;
#                 color: #eb0e0e;
#                 vertical-align: middle;
#             }
#             .value {
#                 color: rgb(0, 255, 30);
#             }
#             .bagian-akhir {
#                 margin: 20px;
#                 padding: 15px;
#                 height: 20%;
#                 background-color: #ffffff;
#             }
#             .status-hidroponik {
#                 font-size: 24px;
#                 font-weight: bold;
#                 width: 100%;
#                 text-align: left;
#                 margin: 20px;
#             }
#             .batas-text {
#                 font-family: 'Courier New', Courier, monospace;
#                 font-size: 20px;
#                 text-align: left;
#                 margin: 0px;
#             }
#             .batas-ph {
#                 width: 100%;
#                 border-radius: 20px;
#                 box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
#                 background-color: antiquewhite;
#             }
#             .scrollbar-horizontal {
#                 width: 100%;
#                 height: 10px;
#                 margin: 0px;
#             }
#             input[type=range] {
#                 -webkit-appearance: none;
#                 width: 100%;
#                 margin: 30px 0;
#             }
#             input[type=range]:focus {
#                 outline: none;
#             }
#             input[type=range]::-webkit-slider-runnable-track {
#                 width: 100%;
#                 height: 8.4px;
#                 cursor: pointer;
#                 border-radius: 10px;
#                 border: 0.2px solid #010101;
#                 background: linear-gradient(to right, 
#                                 red 0%, rgb(255, 149, 0) 20%, 
#                                 rgb(36, 249, 3) 30%, rgb(2, 82, 2) 50%, 
#                                 rgb(45, 1, 76) 80%, purple 100%);
#             }
#             input[type=range]::-webkit-slider-thumb {
#                 -webkit-appearance: none;
#                 height: 20px;
#                 width: 20px;
#                 border-radius: 50%;
#                 background-color: transparent;
#                 cursor: pointer;
#                 box-shadow: 0 0 2px rgba(0,0,0,0.3);
#                 margin-top: -18px;
#             }
#             .ph-labels {
#                 display: flex;
#                 justify-content: space-between;
#                 margin-bottom: 10px;
#                 font-size: 14px;
#             }
#             .ph-label {
#                 width: 33.33%;
#                 text-align: center;
#             }
#         </style>
#     """, unsafe_allow_html=True)


#     # Render HTML content
#     st.markdown("""
#         <div id="Tampilan">
#             <div class="bagian-header">
#                 <img src="data:image/png;base64,{logo_image}" alt="logo" id="logo">
#             </div>
#             <h1 class="judul-overview">Ringkasan Hidroponik</h1>

#             <div class="bagian-utama">
#                 <div class="sensor">
#                     <img src="data:image/png;base64,{icon_ph}" alt="icon_pH" id="icon_pH" />
#                     <h2>pH Air</h2>
#                     <div class="bagian_ph">
#                         <span class="value">7.0</span>
#                         <span class="unit">pH</span>
#                     </div>
#                 </div>
#                 <div class="sensor">
#                     <img src="data:image/png;base64,{icon_suhu}" alt="icon_suhu" id="icon_suhu" /> 
#                     <h2>Suhu Air</h2>
#                     <div class="bagian_suhu">
#                         <span class="value">22</span>
#                         <span class="unit">°C</span>
#                     </div>
#                 </div>
#                 <div class="sensor">
#                     <img src="data:image/png;base64,{icon_nutrisi}" alt="icon_nutrisi" id="icon_nutrisi" />
#                     <h2>Nutrisi</h2>
#                     <div class="bagian_nutrisi">
#                         <span class="value">100</span>
#                         <span class="unit">ppm</span>
#                     </div>
#                 </div>
#             </div>
#             <h1 class="status-hidroponik">Status hidroponik</h1>
#             <div class="bagian-akhir">
#                 <div class="batas-ph">
#                     <h1 class="batas-text">Batas pH</h1>
#                     <input type="range" min="1" max="14" value="5" class="scrollbar-horizontal" id="myRange">
#                     <div class="ph-labels">
#                         <div class="ph-label">Kadar rendah</div>
#                         <div class="ph-label">Kadar sesuai</div>
#                         <div class="ph-label">Kadar tinggi</div>
#                     </div>
#                     <div class="ph-labels">
#                         <div class="ph-label">[1-4]</div>
#                         <div class="ph-label">[5-7]</div>
#                         <div class="ph-label">[9-14]</div>
#                     </div>
#                     <p>pH tanamanmu: <span id="demo">5</span></p>
#                 </div>
#             </div>
#         </div>

#         <script>
#             var slider = document.getElementById("myRange");
#             var output = document.getElementById("demo");
#             output.innerHTML = slider.value;

#             slider.oninput = function() {
#               output.innerHTML = this.value;
#             }
#         </script>
#     """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()
