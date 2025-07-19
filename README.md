# Rice Classifier Web Application 🍚

A user-friendly, responsive web application built with Flask and TensorFlow to classify different varieties of rice from an uploaded image. This project features a modern single-page design for information and a dedicated page for the AI-powered prediction tool.


*(You can replace this with a GIF or screenshot of your own application)*

---

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Setup and Installation](#-setup-and-installation)
- [Running the Application](#-running-the-application)
- [How to Use](#-how-to-use)
- [License](#-license)

---

## ✨ Features

- **Responsive Single-Page Design:** A modern, mobile-friendly interface for Home, About, Testimonials, and Contact sections.
- **AI-Powered Classification:** Utilizes a trained Keras/TensorFlow model (`.h5` file) to predict the rice variety.
- **Image Upload & Preview:** Users can easily upload an image and preview it before making a prediction.
- **Instant Results:** Displays the predicted rice name and the model's confidence score.
- **Interactive UI:** Smooth scrolling and a clean, attractive interface with gradient backgrounds and hover effects.
- **Error Handling:** Provides clear feedback for common issues like invalid file types or server errors.
- **Contact Form:** A functional contact form that captures user queries (backend logic prints to console).

---

## 💻 Technology Stack

### Backend
- **Python 3.x**
- **Flask:** A lightweight WSGI web application framework.
- **TensorFlow / Keras:** For loading the pre-trained deep learning model (`.h5`).
- **Pillow (PIL):** For image manipulation and preprocessing.
- **NumPy:** For numerical operations.

### Frontend
- **HTML5**
- **CSS3:** With custom styles for animations, gradients, and layout.
- **Bootstrap 5:** For responsive design and pre-styled components.
- **JavaScript (ES6):** For handling frontend logic like image preview and API calls (`fetch`).
- **Font Awesome:** For icons.

---

## 📁 Project Structure
rice_classifier_project/
├── app.py # Main Flask application file
├── rice_model.h5 # Your trained Keras model
├── requirements.txt # Python dependencies
├── README.md # This file
│
├── static/ # All static files (CSS, JS, Images)
│ ├── css/
│ │ └── style.css # Custom stylesheets
│ └── js/
│ └── script.js # Frontend JavaScript for prediction page
│
└── templates/ # HTML templates
├── base.html # Master template with Navbar and Footer
├── index.html # Main single-page content (Home, About, etc.)
└── predict.html # The image upload and prediction page

---

## 🚀 Setup and Installation

Follow these steps to get the application running on your local machine.

### Prerequisites
- Python 3.8+
- `pip` package manager
- `git` (optional, for cloning)

### 1. Set Up the Project Folder
Create the project folder and the sub-folders (`static/css`, `static/js`, `templates`) as shown in the structure above. Place all the corresponding code files into their correct locations.

### 2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

- **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  
- **On Windows:**
   python -m venv venv
   .\venv\Scripts\
### 3. Install Dependencies
Create a requirements.txt file in the root directory with the following content:

flask
tensorflow
numpy
Pillow
Then, install all the required Python libraries using this file:

pip install -r requirements.txt
# Running the Application
python app.py
