# Handwritten Digit Recognition System

>     This project is a deep learning–based handwritten digit recognition system built using Python and TensorFlow. The model is trained on the MNIST dataset and can accurately predict digits (0–9) from grayscale images. A simple web-based user interface allows users to upload handwritten digit images and receive instant predictions.

---

Key Features

    Trained a Convolutional Neural Network (CNN) for digit classification

    Achieves high accuracy on unseen test data

    Supports prediction from PNG and JPG images

    Includes an interactive UI for real-time digit prediction

    End-to-end pipeline from data preprocessing to deployment

---

Tech Stack

    Language: Python

    Deep Learning: TensorFlow, Keras

    Dataset: MNIST Handwritten Digits

    UI: Streamlit

    Libraries: NumPy, Pillow, Matplotlib

---

How It Works

    Handwritten digit images are converted to grayscale and resized to 28×28 pixels

    Pixel values are normalized and reshaped for CNN input

    The trained CNN extracts spatial features and classifies the digit

    The UI displays the predicted digit along with the uploaded image

---

Use Cases

    Learning and understanding CNN-based image classification

    Academic projects and viva demonstrations

    Beginner-friendly deep learning application

    Foundation for OCR and handwriting recognition systems

---

1. Step-by-Step Setup Instructions:
   Clone the Repository - Git commands to download the repo

   Set Up Python Environment - Instructions for virtual environment setup (both Unix and Windows)

   Install Dependencies - Lists all required packages:

   TensorFlow
   Matplotlib
   NumPy
   Pillow (for GUI)
   Run the Jupyter Notebook - Complete steps to:

   Install Jupyter
   Launch and run the training notebook
   Train the model from scratch
   Run the GUI Application - Instructions to launch the interactive GUI

---

2. Additional Notes
   Prerequisites for running the GUI (digit_model.h5 file)
