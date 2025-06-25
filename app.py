from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
import joblib
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# Set upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load trained model and label encoder
model = load_model("currency_classifier_cnn.h5")
label_encoder = joblib.load("label_encoder.pkl")

# Prediction function
def predict_image(filepath):
    img = Image.open(filepath).convert("RGB")
    img = img.resize((100, 100))  # Resize to match training input
    img_array = np.array(img).reshape(1, 100, 100, 3) / 255.0  # Normalize
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    class_name = label_encoder.inverse_transform([class_index])[0]
    return class_name

# Flask routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('index.html', result="No file part.")

        file = request.files['image']
        if file and file.filename != "":
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Predict and return result
            result = predict_image(filepath)
            return render_template('index.html', result=result, image_path=filepath)
        else:
            return render_template('index.html', result="No file selected.")
    return render_template('index.html', result=None)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
