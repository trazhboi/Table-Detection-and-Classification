# 📑 Table Detection and Classification using YOLO

A deep learning-based application that detects tables in document images and classifies them as **Bordered** or **Borderless** using the YOLO object detection framework. The project includes a Streamlit web application for interactive inference.

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

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Table-Detection-and-Classification.git

cd Table-Detection-and-Classification
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit server

```bash
streamlit run app.py
```

Open the browser

```
http://localhost:8501
```

---

## 📸 Usage

1. Launch the Streamlit application.
2. Upload a document image.
3. The model detects all tables.
4. Each detected table is classified as:
   - **Bordered**
   - **Borderless**
5. The annotated image with bounding boxes and confidence scores is displayed.

---

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
