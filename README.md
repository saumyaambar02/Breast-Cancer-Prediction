# Breast-Cancer-Prediction

# Project Overview** 

The objective of this project is to develop a machine learning model that can accurately classify breast tumors as malignant or benign based on numerical features extracted from Fine Needle Aspiration (FNA) images .  

Objectives :   

- Analyses tumor characteristics such as radius, texture, perimeter, area, and smoothness.    

- Learns the patterns differentiating malignant and benign tumors.    

- Achieves higher accuracy than manual diagnosis     

- Helps in early detection and reduces human error. 

 

## FEATURES  

These are the 30 input features extracted from FNA (Fine Needle Aspiration) cell images.Each feature describes some physical property of the cell nuclei. 

Feature Group: Description 

- Radius Mean: distance from center to perimeter points 
- Texture : Variation in pixel intensity (gray level) 
- Perimeter: Length of the cell boundary 
- Area: Total area of the nucleus 
- Smoothness	: Local variation in radius length 
- Compactness: Measure of shape compactness 
- Concavity: Severity of concave parts of the nucleus 
- Concave Points: Number of concave portions 
- Symmetry: How symmetrical the nucleus is 
- Fractal Dimension: Complexity of the boundary 

 

## TOOLS USED : 

- Python 
- Numpy 
- Pandas 
- Matplotlib 
- Seaborn 
- Scikit-learn 
- SVM classfier 

## Steps to install and run the project 

1.⁠ ⁠Clone or Download the Project 

git clone https://github.com/saumyaambar02/Breast-Cancer-Prediction.git 

2.⁠ ⁠Create a Virtual Environment  

python3 -m venv venv source venv/bin/activate 

3.⁠ ⁠Install Required Libraries 

pip install numpy pandas matplotlib seaborn scikit-learn 

4.⁠ ⁠Run the Project Code 

5.⁠ ⁠View Results 

## Instructions for Testing:

- Split the dataset into training (80%) and testing (20%) sets.  

- Then evaluate the SVM model on test data to measure its accuracy.  

- After that compare the predicted results against true labels using confusion matrix and classification reports. 
