import streamlit as st

# Create a Streamlit app
st.title("Smart Hidroponik")

# Create a container for the app
container = st.container()

# Add a header section
with container:
    st.markdown("""
        <div class="bagian-header">
            <img src="logo fixx1.png" alt="logo" id="logo" style="width:100%;">
        </div>
    """, unsafe_allow_html=True)

# Create a section for the overview
with container:
    st.markdown("""
        <h1 class="judul-overview">Ringkasan Hidroponik</h1>
    """, unsafe_allow_html=True)

# Create a section for the sensors
with container:
    st.markdown("""
        <div class="bagian-utama">
            <div class="sensor">
                <img src="icon_pH.png" alt="icon_pH" id="icon_pH" style="width:100%;" />
                <h2>pH Air</h2>
                <div class="bagian_ph">
                    <span class="value">7.0</span>
                    <span class="unit">pH</span>
                </div>
            </div>
            <div class="sensor">
                <img src="icon_suhu_air.png" alt="icon_suhu" id="icon_suhu" style="width:100%;" /> 
                <h2>Suhu Air</h2>
                <div class="bagian_suhu">
                    <span class="value">22</span>
                    <span class="unit">°C</span>
                </div>
            </div>
            <div class="sensor">
                <img src="icon_tds.png" alt="icon_nutrisi" id="icon_nutrisi" style="width:100%;" />
                <h2>Nutrisi</h2>
                <div class="bagian_nutrisi">
                    <span class="value">100</span>
                    <span class="unit">ppm</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Create a section for the status
with container:
    st.markdown("""
        <h1 class="status-hidroponik">Status hidroponik</h1>
    """, unsafe_allow_html=True)

# Create a section for the pH range slider
ph_value = st.slider('Batas pH', min_value=1, max_value=14, value=5)
st.markdown(f"<p>pH tanamanan mu: <span>{ph_value}</span></p>", unsafe_allow_html=True)

# Add some CSS to style the app
st.write("""
    <style>
        body {
            font-family: sans-serif;
            margin: 0;
            padding: 0;
            background-color: #ffffff;
        }
        #Tampilan{
            position:relative;
            width: 50%;
            margin: 10px auto;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, 
            rgba(0, 0, 0, 0.12) 0px -12px 30px, 
            rgba(0, 0, 0, 0.12) 0px 4px 6px,
            rgba(0, 0, 0, 0.17) 0px 12px 13px, 
            rgba(0, 0, 0, 0.09) 0px -3px 5px;
        }
       .bagian-header{
            background-image: url("bgHidroponik.jpg");
            border-radius: 10px 10px 0 0;
            border-bottom: 2px solid #eb0e0e;
            margin : 0;
            padding:10;
                    }
       .bagian-utama{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin: 20px;
        }
       .sensor{
            background-color: #ffffff;
            border: 1px solid #dddddd;
            border-radius: 10px;
            padding: 20px;
            margin: 20px;
            width: 250px;
        }
       .bagian-ph, .bagian_suhu, .bagian_nutrisi{
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
        }
       .value{
            font-size: 24px;
            font-weight: bold;
        }
       .unit{
            font-size: 18px;
        }
       .batas-ph{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }
       .ph-labels{
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
        }
       .ph-label{
            font-size: 18px;
        }
    </style>
""")
