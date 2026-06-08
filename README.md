# Chest X-Ray Multi-Label Classification Pipeline

This repository contains a full-stack Python application that processes chest X-ray images, passes them through a deep learning model to predict 15 distinct pathology categories simultaneously, and visualizes model focus areas using Grad-CAM.

---

## 📁 Project Directory Structure

* **`app.py`** – The main Streamlit web application interface. It handles image uploads, runs the end-to-end inference pipeline, displays pathology confidences, and renders interactive visualization maps.
* **`requirements.txt`** – The dependency manifest file specifying required library versions (`torch`, `streamlit`, `grad-cam`, etc.).
* **`.gitignore`** – Configured to prevent tracking environment binaries (`xray-venv/`), local python caches (`__pycache__/`), and heavy weight matrices (`*.pth`).
* **`model/`** – Main backend neural network utilities folder:
    * `train.py` – Script used to train the baseline model weights on labeled medical data.
    * `predict.py` – Module containing `load_model()` and `predict()` logic to handle tensor transformations and calculate raw classification values.
    * `optimize_thresholds.py` – Calibration script that runs an evaluation sweep to calculate optimized per-class decision boundaries.
    * `evaluate.py` – Performance auditing script that calculates final metrics across validation data splits.
    * `optimal_thresholds.json` – Saved JSON matrix containing the fine-tuned decision boundaries for each disease class.
    * `model.pth` – The local serialized model weights file (binary).
* **`preprocessing/`** – Data engineering components folder:
    * `pipeline.py` – Handles dataset loading functions (`XRayDataset`) and initial image matrix parsing logic.
* **`data/`** – Local storage folder intended for holding target medical images and labels sheet arrays.
* **`utils/`** – Helper configuration scripts folder.

---

## ⚙️ Local Installation & Environment Setup

To recreate and run this environment locally, execute the following commands in sequence within your terminal:

### 1. Initialize the Virtual Environment
```bash
python -m venv xray-venv

```

### 2. Activate the Environment (Windows Git Bash Syntax)

```bash
source ./xray-venv/Scripts/activate

```

### 3. Update Package Installer & Install Dependencies

```bash
python -m pip install -r requirements.txt

```

---

## How to Run the Application Scripts

Ensure your virtual environment is active `(xray-venv)` before running any of the execution commands below.

### To Launch the User Interface Dashboard:

Run this command from the root directory to open the interactive frontend app in your local web browser:

```bash
python -m streamlit run app.py

```

### To Run the Statistical Performance Audit:

To verify macro/micro scores and print the full class breakdown metrics report directly in your terminal, execute:

```bash
python model/evaluate.py

```

---

ℹ️ *Disclaimer: This project is built strictly for research, benchmarking, and educational evaluation purposes. It does not provide clinical medical advice or substitute for diagnostic reviews by licensed medical professionals.*
