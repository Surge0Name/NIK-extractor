import streamlit as st
import cv2
import numpy as np
from image_extraction import NIKExtractor
import os

st.title("Aplikasi ekstraksi NIK KTP")



uploaded_img = st.file_uploader("Upload KTP", type=["jpg", "jpeg", "png"])

if uploaded_img is not None:
    file_byte = np.asarray(bytearray(uploaded_img.read()), dtype=np.uint8)
    image = cv2.imdecode(file_byte, 1)

    st.image(image, caption="uploaded image", use_column_width=True)

    extractor = NIKExtractor(image)
    #process gambar
    input = extractor.inputImage()
    cropped = extractor.cropping_img(input)
    st.image(cropped, caption="cropped Image", use_column_width=True)

    binarize = extractor.binarization(cropped)
    st.image(binarize, caption="Thresholded Image", use_column_width=True)

    NIK = extractor.extraction(binarize)
    
    if NIK:
        NIK_str = ', '.join(NIK)
        # st.success(f"**Extracted NIK:** {NIK_str}")
        st.markdown(f"""<div style="text-align: center; background-color: #d4edda; padding: 10px; border-radius: 5px; color: #155724;">Extracted NIK:
                    <strong>{NIK_str}</strong></div>"""
                    ,unsafe_allow_html=True)
    else:
        # st.error("**NIK tidak ditemukan. Tolong pastikan bahwa kondisi di bawah telah terpenuhi: **")
        st.markdown(f"""<div style="text-align: center; background-color: #3e2428; padding: 10px; border-radius: 5px;">
                    NIK tidak ditemukan. Tolong pastikan bahwa kondisi di bawah telah terpenuhi: 
                    </div>"""
                    ,unsafe_allow_html=True)
        #menunjukan kondisi ideal
        st.markdown("""
            - Pastikan gambar jelas dan tidak kabur
            - Gambar KTP harus berada pada posisi tepat (tidak miring), contoh seperti di bawah
            - Text NIK harus dapat dibaca dan berkontras tinggi (pencahaayaan baik)
            - Warna background KTP harus memiliki warna yang berbeda dengan background KTP
        """)

        #gambar ideal
        st.markdown("Contoh gambar ideal")

        example_image_path = "place-holder.jpg" 
        if os.path.exists(example_image_path):
            st.image(example_image_path, caption = "Gambar ideal", use_column_width = True)
        else:
            st.error("Gambar ideal tidak ditemukan. Pastikan path yang benar telah digunakan")

