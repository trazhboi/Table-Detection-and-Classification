import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="Table Detector")

st.title("Bordered / Borderless Table Detector")

model = YOLO("best.pt")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Input", use_container_width=True)

    img = np.array(image)

    results = model.predict(img)

    annotated = results[0].plot()

    st.image(
        annotated,
        caption="Prediction",
        use_container_width=True
    )

    st.subheader("Detected Tables")

    for box in results[0].boxes:

        cls = int(box.cls)

        conf = float(box.conf)

        label = model.names[cls]

        st.write(
            f"**{label}** - {conf:.2f}"
        )
