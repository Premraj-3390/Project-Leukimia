[![IEEE Published](https://img.shields.io/badge/IEEE-Published-blue)](https://doi.org/10.1109/RAEEUCCI67649.2026.11504871)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)](https://www.tensorflow.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Classifier-green)](https://xgboost.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Acute Lymphoblastic Leukemia Detection Using FCM Segmentation, EfficientNetB4 and XGBoost

This repository contains the **official implementation** of our **IEEE-published research** on automated **Acute Lymphoblastic Leukemia (ALL)** detection from microscopic blood smear images.

The proposed hybrid framework combines **Fuzzy C-Means (FCM) Segmentation**, **EfficientNetB4 Deep Feature Extraction**, and **GPU-Accelerated XGBoost Classification** to accurately distinguish **Benign** and **Malignant** blood smear samples.

---

# 📄 Published Research

**Title**

**Effective Hybrid Pipeline for Acute Lymphoblastic Leukemia Detection using FCM Segmentation, EfficientNet Features, and XGBoost Classification**

**Conference**

2026 5th International Conference on Recent Advances in Electrical, Electronics, Ubiquitous Communication, and Computational Intelligence (RAEEUCCI)

**DOI**

https://doi.org/10.1109/RAEEUCCI67649.2026.11504871

**IEEE Xplore**

https://ieeexplore.ieee.org/document/11504871

---

# 📊 Project Highlights

- 🎯 Test Accuracy: **95.53%**
- 🧠 EfficientNetB4 for Deep Feature Extraction
- ⚡ GPU-Accelerated XGBoost Classification
- 🔬 Fuzzy C-Means Image Segmentation
- 🩸 Binary Classification (Benign vs Malignant)
- 📄 Official IEEE Published Research
- 🐍 Developed using Python, TensorFlow, Scikit-learn and XGBoost

---

# 📌 Dataset

**Dataset Used**

Blood Cell Cancer (ALL 4-Class)

https://www.kaggle.com/datasets/mohammadamireshraghi/blood-cell-cancer-all-4class

This dataset is used strictly for **research, educational and academic purposes**.

### Class Mapping

| Original Class | Converted Label |
|---------------|-----------------|
| Benign | 0 |
| Early Pre-B | 1 |
| Pre-B | 1 |
| Pro-B | 1 |

---

# ⚙️ Methodology

The proposed pipeline consists of the following stages:

1. Image Preprocessing
2. Fuzzy C-Means (FCM) Segmentation
3. Deep Feature Extraction using EfficientNetB4
4. Feature Classification using GPU-Accelerated XGBoost
5. Performance Evaluation using Classification Metrics
6. Qualitative Error Analysis

---

# 🚀 Features

- Fuzzy C-Means based nucleus segmentation
- Transfer Learning using EfficientNetB4
- GPU Accelerated XGBoost Training
- Binary Classification Pipeline
- Precision, Recall, F1-Score Evaluation
- Confusion Matrix Generation
- Qualitative Prediction Analysis
- End-to-End Reproducible Workflow

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ALL-Detection-EfficientNet-XGBoost.git

cd ALL-Detection-EfficientNet-XGBoost
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Open the notebook

```text
segmentation_and_classification.ipynb
```

The notebook includes:

- Data Preprocessing
- FCM Segmentation
- EfficientNetB4 Feature Extraction
- XGBoost Model Training
- Model Evaluation
- Performance Analysis

---

# 📈 Performance

**Final Test Accuracy**

**95.53%**

Evaluation Metrics include:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

---

# 📂 Repository Structure

```
ALL-Detection-EfficientNet-XGBoost/
│
├── src/
│   ├── preprocessing.py
│   ├── fcm_segmentation.py
│   ├── feature_extraction.py
│   ├── xgboost_classifier.py
│   └── utils.py
│
├── results/
│
├── segmentation_and_classification.ipynb
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 📚 Citation

If you use this repository in your research, please consider citing our paper.

```
Effective Hybrid Pipeline for Acute Lymphoblastic Leukemia Detection using FCM Segmentation, EfficientNet Features, and XGBoost Classification.

2026 5th International Conference on Recent Advances in Electrical, Electronics, Ubiquitous Communication, and Computational Intelligence (RAEEUCCI)

DOI:
https://doi.org/10.1109/RAEEUCCI67649.2026.11504871
```

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ⚠️ Disclaimer

This repository is intended **solely for research, educational and academic purposes**.

It is **not** intended for clinical diagnosis or medical decision-making.

---

# 👨‍💻 Author

**Premraj**-**24AD153**

**Sandeep Bharathi**-**24AD175**

**Sakthi Vishal**-**24AD173**

**Mohamed Irfan**-**24AD122**

B.Tech Artificial Intelligence And Data Science
Machine Learning | Deep Learning | Computer Vision

Open to **Machine Learning Engineer**, **AI Engineer**, and **Research Engineer** opportunities.

GitHub: https://github.com/Premraj-3390
