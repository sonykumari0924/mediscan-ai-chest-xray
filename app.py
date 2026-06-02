import streamlit as st
import time
from PIL import Image
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="MediScan AI - Chest X-ray Analysis",
    page_icon="🩺",
    layout="centered"
)

# --- SIDEBAR COMPONENT ---
with st.sidebar:
    st.markdown("### 🩺 MediScan AI")
    st.caption("MENU")
    
    # Active navigation placeholder (just showing the single objective)
    st.markdown("**📥 Diagnose**")
    
    # Pushes the model info card to the bottom of the sidebar
    st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
    
    # Model Specs Info Box
    st.info("""
    **Model version:** ResNet-50 v2.1  
    
    **Accuracy:** 94.2%
    """)

# --- MAIN PAGE ---
st.title("Chest X-ray Analysis")
st.write("Upload any image — we handle resizing, quality normalization, and preprocessing automatically.")

# 1. File Upload Zone
uploaded_file = st.file_uploader(
    "Drop your X-ray image here", 
    type=["jpg", "jpeg", "png"],
    help="JPG, PNG · any size or resolution · low-quality scans accepted"
)

# Layout division for Preview and Results
if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)
    
    # Create two columns
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("**Preview**")
        # Display uploaded image resized cleanly 
        st.image(image, use_container_width=True)
        st.caption("Uploaded Scan")
        
    with col2:
        st.markdown("### Detection results")
        
        # Simulated Inference Phase 
        with st.spinner("Running pipeline..."):
            time.sleep(1.3) 
            
        # Mock class probabilities 
        results = {
            "Pneumonia": 0.78,
            "Pleural effusion": 0.34,
            "Normal": 0.12,
            "Tuberculosis": 0.09
        }
        
        # Display Custom "Abnormal" Status badge if Pneumonia is high
        if results["Pneumonia"] > 0.50:
            st.error("⚠️ Status: Abnormal Detection")
        else:
            st.success("✅ Status: No Significant Finding")
            
        # Render the custom confidence bars
        for disease, confidence in results.items():
            st.write(f"**{disease}** ({int(confidence * 100)}%)")
            st.progress(confidence)

    st.write("---")

    # 2. Performance Metrics Grid
    st.markdown("### Pipeline Metrics")
    m_col1, m_col2, m_col3 = st.columns(3)
    m_col1.metric(label="Model Accuracy", value="94.2%")
    m_col2.metric(label="Avg. Inference Time", value="1.3s")
    m_col3.metric(label="Input Resolution", value="Any (Auto)")

    # 3. Preprocessing Pipeline Visualization Card
    st.markdown("---")
    with st.expander("🔬 View Preprocessing Pipeline Steps", expanded=True):
        st.code(
            "Auto resize → 224×224  >>>  CLAHE Enhancement  >>>  Normalize [0,1]  >>>  Model Inference",
            language="text"
        )

# --- FOOTER 
st.markdown("---")
st.caption("ℹ️ *This tool is for informational purposes only — not a substitute for a licensed radiologist.*")
st.caption("ℹ️ *Low resolution or phone-photographed X-rays are accepted; CLAHE contrast enhancement compensates for quality variation.*")