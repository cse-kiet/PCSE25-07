import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Load the model
model = load_model('models/2.keras')

# Load and preprocess the image
img_path = 'E:/Skin/f.jpeg'  # Corrected path with forward slashes
img = image.load_img(img_path, target_size=(224, 224))  # Assuming the target size expected by your model
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

# Predict
predictions = model.predict(img_array)
print(predictions)
