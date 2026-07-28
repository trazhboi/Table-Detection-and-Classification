# 📑 Table Detection and Classification using YOLO

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-red?logo=streamlit)](https://table-detection-and-classification.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)]
[![YOLO](https://img.shields.io/badge/YOLO-Ultralytics-green)]
[![License](https://img.shields.io/badge/License-MIT-yellow)]

> 🚀 **Live Demo:** https://table-detection-and-classification.streamlit.app/

---

## 📌 Overview

Tables are a crucial component of many documents such as invoices, research papers, financial reports, and forms. Accurately detecting tables and distinguishing between bordered and borderless layouts is an important preprocessing step for document understanding and information extraction.

This project leverages a custom-trained YOLO model to:

- Detect tables in document images
- Classify each detected table as:
  - **Bordered**
  - **Borderless**
- Display bounding boxes with confidence scores
- Provide an easy-to-use Streamlit web interface

---

## ✨ Features

- Detect multiple tables in a single image
- Classify tables into bordered or borderless
- Display confidence scores
- Interactive Streamlit interface
- Fast inference using YOLO
- Supports JPG, JPEG, and PNG images

---

## 🛠️ Tech Stack

- Python
- YOLO (Ultralytics)
- PyTorch
- OpenCV
- NumPy
- Pillow
- Streamlit

---

## 📂 Project Structure

```
Table-Detection-and-Classification/
│
├── app.py                 # Streamlit application
├── best.pt                # Trained YOLO model
├── requirements.txt
├── README.md
│
├── images/
│   ├── sample1.jpg
│   ├── sample2.jpg
│
└── runs/
```

---

## 🌐 Live Demo

Try the deployed application here:

**🔗 https://table-detection-and-classification.streamlit.app/**

No installation is required—simply upload a document image containing tables, and the model will detect and classify each table as **Bordered** or **Borderless**.

## 🧠 Model

The project uses a custom-trained **YOLO** model trained on a dataset containing bordered and borderless tables.

### Classes

| Class ID | Label |
|----------:|-------|
| 0 | Bordered |
| 1 | Borderless |

---

## 📈 Example Output

The application displays:

- Original uploaded image
- Detected tables
- Bounding boxes
- Confidence scores
- Table classification

Example:

```
Bordered    0.96
Borderless  0.91
Bordered    0.88
```

---

## 📦 Requirements

Main libraries used:

- streamlit
- ultralytics
- torch
- torchvision
- opencv-python-headless
- pillow
- numpy

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Applications

- Document Analysis
- Invoice Processing
- OCR Pipelines
- Research Paper Parsing
- Financial Statement Analysis
- Automated Form Processing
- Intelligent Document Processing (IDP)

---

## 🔮 Future Improvements

- PDF document support
- Batch image processing
- Export detection results as JSON or CSV
- Table structure recognition
- Integration with OCR engines
- REST API deployment
- Docker support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Kishalay Kashyap**

Computer Science Engineering Student

GitHub: https://github.com/your-username
