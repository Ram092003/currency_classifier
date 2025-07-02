
Currency Classification Web App
================================

This is a machine learning-based web application built using TensorFlow and Flask.
It classifies Indian currency notes (₹20, ₹50, ₹100, ₹500) using a Convolutional Neural Network (CNN).

--------------------------------
Features
--------------------------------
- Upload Indian currency note images.
- Predicts denominations: ₹20, ₹50, ₹100, and ₹500.
- Simple web interface using Flask and HTML/CSS.
- CNN model trained using TensorFlow and Keras.

--------------------------------
Technologies Used
--------------------------------
- Python 3.10
- TensorFlow 2.10 (or compatible)
- Flask
- Keras
- NumPy, Pillow, Scikit-learn

--------------------------------
Folder Structure
--------------------------------
currency-classification/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── upload/
│   └── styles.css (optional)
├── currency_classifier_cnn.h5
├── requirements.txt
├── render.yaml
└── README.txt

--------------------------------
How to Run Locally
--------------------------------
1. Clone this repository.
2. Install dependencies using: pip install -r requirements.txt
3. Run the app: python app.py
4. Open browser: http://127.0.0.1:5000

--------------------------------
Deployment
--------------------------------
To deploy on Render:
- Use Python 3.10
- Include `render.yaml`, `requirements.txt`, and `runtime.txt`

--------------------------------
License
--------------------------------
This project is licensed under the MIT License.
