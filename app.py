import os
import numpy as np
from PIL import Image
import tensorflow as tf
from flask import Flask, request, render_template, jsonify, url_for, redirect

# --- Basic Setup ---
app = Flask(__name__)

# --- Model Loading and Configuration ---
try:
    model_path = 'rice_model.h5'
    model = tf.keras.models.load_model(model_path)

    # Update class names as per your model
    CLASS_NAMES = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']
    IMG_SIZE = 224  # Change if your model expects a different size

except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    CLASS_NAMES = []
    IMG_SIZE = 0

# --- Helper Function for Image Preprocessing ---
def preprocess_image(image_file):
    try:
        img = Image.open(image_file.stream).convert('RGB')  # RGB for 3 channels
        img = img.resize((50, 50))  # Match model input shape
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 50, 50, 3)
        return img_array
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None

# --- Web Page Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Contact form submission: Name={name}, Email={email}, Message={message}")
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/predict', methods=['GET'])
def predict_page():
    return render_template('predict.html')

# --- API Endpoint for Prediction ---
@app.route('/api/predict', methods=['POST'])
def api_predict():
    if model is None:
        return jsonify({'error': 'Model is not loaded. Please check server logs.'}), 500

    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected.'}), 400

    allowed_extensions = {'png', 'jpg', 'jpeg'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({'error': 'Invalid file type. Please upload a .png, .jpg, or .jpeg image.'}), 400

    try:
        processed_image = preprocess_image(file)
        if processed_image is None:
            return jsonify({'error': 'Could not process the image.'}), 500

        print("Processed image shape:", processed_image.shape)

        prediction = model.predict(processed_image)
        predicted_class_index = np.argmax(prediction[0])
        predicted_class_name = CLASS_NAMES[predicted_class_index]
        confidence = np.max(prediction[0]) * 100

        return jsonify({
            'prediction': predicted_class_name,
            'confidence': f"{confidence:.2f}%"
        })

    except Exception as e:
        import traceback
        traceback.print_exc()  # Will print full error in terminal
        return jsonify({'error': str(e)}), 500  # Return actual error in response

# --- Main Application Runner ---
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
