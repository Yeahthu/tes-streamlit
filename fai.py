import streamlit as st

# Create a Streamlit app
st.title("Smart Hidroponik")

# Create a container for the app
container = st.container()

# Add a header section
with container:
    st.header("Ringkasan Hidroponik")
    st.image("logo fixx1.png", width=150)

# Create a section for the sensors
with container:
    st.header("Sensor Values")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("icon_pH.png", width=50)
        st.metric("pH Air", "7.0", "pH")
    with col2:
        st.image("icon_suhu_air.png", width=50)
        st.metric("Suhu Air", "22", "°C")
    with col3:
        st.image("icon_tds.png", width=50)
        st.metric("Nutrisi", "100", "ppm")

# Create a section for the pH range slider
with container:
    st.header("Batas pH")
    slider_value = st.slider("pH Range", min_value=1, max_value=14, value=5)
    st.write("pH tanaman mu:", slider_value)

    # Add some labels for the pH range
    labels = ["Kadar rendah", "Kadar sesuai", "Kadar tinggi"]
    values = ["[1-4]", "[5-7]", "[9-14]"]
    for i, label in enumerate(labels):
        st.write(label, values[i])

# Run the app
if __name__ == "__main__":
    st.run()
