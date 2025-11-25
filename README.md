# 🩺 Breast Cancer Prediction 

The objective of this project is to develop a machine learning model that can accurately classify breast tumors as malignant or benign based on numerical features extracted from Fine Needle Aspiration (FNA) images.This project focuses on understanding the data, preprocessing it, training an ML model, and evaluating its performance in a practical and easy‑to‑follow way.


---

## 📌 Project Overview

Breast cancer detection is a very important real‑world problem. In this project, we use machine learning to study different characteristics of a tumor and let the model learn patterns that help classify it.

The features used in this dataset come from *Fine Needle Aspiration (FNA)* images — these are tiny samples taken from a breast mass and analyzed for different cell measurements.

This project shows:

•⁠  ⁠How the dataset is structured
•⁠  ⁠How the ML pipeline is built
•⁠  ⁠How the SVM model makes predictions
•⁠  ⁠How to evaluate model performance in a meaningful way

---

## 🎯 Main Objectives

•⁠  ⁠Understand the dataset and the tumor features
•⁠  ⁠Preprocess the data before training
•⁠  ⁠Visualize important trends and correlations
•⁠  ⁠Build and train an SVM classifier
•⁠  ⁠Test the model using unseen data
•⁠  ⁠Present results in a clean and organized way

---

## 📂 Folder & File Structure

The structure of the project is kept simple and organized:

⁠ bash
📁 Breast-Cancer-Prediction
│── README.md              → Project documentation
│── LICENSE                → Apache License 2.0
│── .gitignore             → Files excluded from Git
│── main.py                → Entry point of the project
│── train.py               → Model training script
│── model.py               → Model creation logic
│── dataload.py            → Loads and prepares dataset
│── preprocessing.py       → Cleans and preprocesses data
│── data-analysis.py       → Performs exploratory data analysis
│── visualize.py           → Generates plots & visualizations
│── evaluate.py            → Evaluates performance metrics
│── statement.md           → Additional statements/report details
 ⁠

Each script handles one responsibility, keeping the project clean and modular.

---

## 🔍 Understanding the Dataset

The dataset contains:

•⁠  ⁠*569 samples* of breast tumor biopsies
•⁠  ⁠*30 numerical features* such as:

  * radius, texture, perimeter, area
  * smoothness, compactness, concavity
  * symmetry, fractal dimension
•⁠  ⁠*Two output classes*:

  * ⁠ 0 ⁠ → malignant (cancerous)
  * ⁠ 1 ⁠ → benign (non‑cancerous)

This dataset is widely used for ML learning and medical classification tasks.

---

## ⚙️ Model Overview — Why SVM?

We use an *SVM (Support Vector Machine)* classifier because:

•⁠  ⁠It works extremely well for binary classification
•⁠  ⁠It handles small to medium datasets efficiently
•⁠  ⁠It creates a clear separation boundary between classes
•⁠  ⁠It avoids overfitting when tuned properly

The model learns patterns from tumor features and uses them to predict the final classification.

---

## Features of the Project 

✨ Key Features

- Clean dataset loading using the built-in Breast Cancer Wisconsin dataset from scikit-learn.

- Easy-to-understand data exploration to get a feel for all 30 diagnostic features.

- Visualizations (heatmaps, pair plots, distribution graphs) to understand patterns and relationships.

- Preprocessing pipeline with splitting features and labels, then dividing data into train/test sets.

- SVM-based classification model that learns the difference between malignant and benign tumors.

- Model evaluation using accuracy score, confusion matrix, and classification metrics.

- Simple, modular code structure so each part (loading, visualization, training, prediction) stays readable.

- Fast & lightweight — no external database or heavy dependencies required.



---

## ✅ Tools Used 

🛠️ Tools & Technologies Used

Python – main programming language

Pandas – for handling tabular data

NumPy – for numerical computations

Matplotlib & Seaborn – for plots and visual insights

scikit-learn –

To load the breast cancer dataset

To build the SVM model

To split data and evaluate results

Jupyter Notebook 

---

## 🛠️ Steps to install & run the Project 


### 1️⃣ Install all the required Libraries


pip install pandas numpy matplotlib seaborne scikit-learn

### 2️⃣ Run the Main File


python main.py


This runs the full prediction pipeline.

### 3️⃣ Train the Model Separately


python train.py


### 4️⃣ Visualize the Data


python visualize.py


### 5️⃣ Evaluate Model Performance


python evaluate.py


---

## 📊 Visualizations

Visualizations helps us to understand relationships between the features.

![heatmap](<img width="1082" height="693" alt="Screenshot 2025-11-25 at 4 49 22 PM" src="https://github.com/user-attachments/assets/5c3fc094-a51b-4a09-a559-acc3e67f6eaf" />
)
![pairplot](<img width="784" height="724" alt="Screenshot 2025-11-25 at 4 50 59 PM" src="https://github.com/user-attachments/assets/6130f1c6-4e6d-4519-b145-7e178ba9f8d0" />
)
![scatter plot](<img width="803" height="518" alt="Screenshot 2025-11-25 at 4 50 42 PM" src="https://github.com/user-attachments/assets/05988671-6de1-4f22-9cc5-f9dc11421f19" />
)⁠


---

## 🧪 Model Performance Summary

The SVM model typically performs very well on this dataset, often achieving:

•⁠  ⁠High accuracy
•⁠  ⁠Good precision and recall
•⁠  ⁠Strong generalization to test data


---

## 🌟 Key Highlights of the Project

- Modular and readable code
- ⁠Clean ML workflow (load → preprocess → train → evaluate)
- Human‑friendly explanations
- ⁠Easy to extend with more models or features
