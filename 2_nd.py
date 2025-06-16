# grohaics_app.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Page Title
st.set_page_config(page_title="Grohaics", layout="centered")
st.title("🎨 Grohaics - A Simple Graphics App")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Plot Generator", "Image Viewer"])

# Home Section
if page == "Home":
    st.subheader("Welcome to Grohaics!")
    st.write("""
        This is a simple web app to explore Python graphics using Streamlit.
        
        - Generate basic plots
        - Upload and display images
    """)

# Plot Generator Section
elif page == "Plot Generator":
    st.subheader("📈 Generate a Sine Wave Plot")

    freq = st.slider("Frequency", 1, 20, 5)
    amp = st.slider("Amplitude", 1, 10, 2)
    x = np.linspace(0, 2*np.pi, 500)
    y = amp * np.sin(freq * x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"Sine Wave: freq={freq}, amp={amp}")
    st.pyplot(fig)

# Image Viewer Section
elif page == "Image Viewer":
    st.subheader("🖼️ Upload and View Image")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)
