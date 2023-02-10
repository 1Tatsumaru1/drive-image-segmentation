# October 2022
# Anthony LE DOUGUET
# Openclassrooms project 8 assignment
# Snippets from https://github.com/divamgupta/image-segmentation-keras


# Module imports
from flask import Flask, request
import os
import json
import time
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array


# Global variables
app = Flask(__name__)
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
input_h = 1024
input_w = 2048
output_h = 512
output_w = 1024


# Default route to check the API is running
#
# @return JSON {'hello': 'world}
@app.route('/', methods=['GET'])
def hello_world():
    return {'Hello': 'World!'}


# Route that handles image segmentation requests
#
# @param request.json['img'] --> image in stringified numpy array format (h, w, c) = (1024, 2048, 3)
# @return <JSON> --> {'data': segmentation image in stringified numpy array format (h, w, c) = (512, 1024, 3)
@app.route('/predict', methods=['POST'])
def segmentation():
    tps_rec = time.time()
    json_data = request.json
    img_str = json_data['img']
    arr = pickle.loads(json.loads(img_str).encode('latin-1'))
    tps_start = time.time()
    pred = prediction(model=seg_model, inp=arr)
    tps_pred = time.time()
    pred = np.expand_dims(pred, -1)
    res = np.zeros((output_h, output_w, 3))
    res[..., 0] = res[..., 1] = res[..., 2] = pred[..., 0]
    tps_proc = time.time()
    return {
        'data': json.dumps(pickle.dumps(res).decode('latin-1')),
        'tps_rec': tps_rec,
        'tps_start': tps_start,
        'tps_pred': tps_pred,
        'tps_proc': tps_proc
    }


# Get a normalized array out of the input images
#
# @param img image object
# @return <image> --> normalized image
def get_image_array(img):
    img = img_to_array(img)
    img = img.astype(np.float32)
    img = np.atleast_3d(img)
    means = [103.939, 116.779, 123.68]
    for i in range(min(img.shape[2], len(means))):
        img[:, :, i] -= means[i]
    img = img[:, :, ::-1]
    return img


# Issue a segmentation mask from an input image
#
# @param model <keras.models.Model> --> the segmentation model
# @param inp <image> --> the original image to predict the segmentation from
# @return pr <image> --> the segmentation image in 2D shape (h, w) = (512, 1024)
def prediction(model, inp):
    n_classes = 8
    x = get_image_array(inp)
    pr = model.predict(np.array([x]))[0]
    pr = pr.reshape((output_h, output_w, n_classes)).argmax(axis=2)
    return pr


# Loads the stored model
#
# @return <keras.models.Model> --> the segmentation model
def get_model():
    model = load_model(f'./models/final.h5')
    return model


# Model loading at application startup
seg_model = get_model()


# Application startup
if __name__ == '__main__':
    app.run(debug=True)
