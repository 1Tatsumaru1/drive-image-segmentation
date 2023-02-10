# October 2022
# Anthony LE DOUGUET
# Openclassrooms project 8 assignment


# Module imports
from flask import Flask, render_template, request, flash
import os
import json
import time
import pickle
import requests
import numpy as np
from PIL import Image

# Global variables
app = Flask(__name__)
app.secret_key = 'dev'
uploads_dir = os.path.join(app.root_path, 'static')
img_h = 1024
img_w = 2048


# Checks validity of image file transmitted
#
# @param filename <str> --> The name of the file
# @return boolean --> Whether the filename complies to requirements (True) or not (False)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] == 'png'


# Checks input, fetch segmentation from the API and displays the results
#
# @param request.file['img'] <FileStorage> --> Image file with mandatory dimensions (h, w, c) = (1024, 2048, 3)
# @param request.file['msk'] <FileStorage> (optional) --> Image file with mandatory dimensions
#   (h, w, c) = (1024, 2048, >=1)
# @return void
@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':

        # Checking whether the image file has been sent and seems valid enough
        proc_start = time.time()
        if 'img' not in request.files:
            flash("Il est nécessaire de fournir une image à segmenter")
            return render_template('index.html')
        filename = request.files['img'].filename
        if filename == '' or not allowed_file(filename):
            flash("Il est nécessaire de fournir une image à segmenter")
            return render_template('index.html')

        # Conversion into np.array format and dimension check
        img = Image.open(request.files['img'])
        arr = np.asarray(img, dtype='int32')
        img_dims = np.shape(arr)
        if img_dims != (img_h, img_w, 3):
            flash(f"Les dimensions de l'image fournie en entrée doivent être (1024, 2048, 3), ici: {img_dims}")
            return render_template('index.html')

        # Saving the image if everything is fine up to now
        img.save(os.path.join(uploads_dir, 'org.png'))

        # Checking the mask (optional sending)
        msk_bucket = ''
        msk_show = False  # Boolean sent with the rendering process to indicate the need of loading msk's div block
        if 'msk' in request.files:
            filename = request.files['msk'].filename
            if filename != '' and allowed_file(filename):
                msk = Image.open(request.files['msk'])
                msk_arr = np.asarray(msk, dtype='int32')
                msk_dims = np.shape(msk_arr)
                if msk_dims[0] == img_h and msk_dims[1] == img_w:
                    msk_arr = ((msk_arr - msk_arr.min()) * (1 / (msk_arr.max() - msk_arr.min()) * 255)).astype('uint8')
                    msk = Image.fromarray(msk_arr)
                    msk.save(os.path.join(uploads_dir, 'msk.png'))
                    msk_show = True

        # Prepare for API dialog
        json_img = json.dumps(pickle.dumps(arr).decode('latin-1'))
        url = 'http://34.65.52.225:5000/predict'
        headers = {"Content-Type": "application/json"}

        # API request
        req_send = time.time()
        response = requests.request(method='POST', headers=headers, url=url, json={'img': json_img})
        req_resp = time.time()
        if int(response.status_code) != 200:
            flash(f"La segmentation a échoué. Code: {response.status_code}")
            return render_template('index.html')

        # Get the predicted segmentation image out of the received JSON and saves it to storage
        res = response.json()
        r_arr = pickle.loads(json.loads(res['data']).encode('latin-1'))
        r_arr = ((r_arr - r_arr.min()) * (1 / (r_arr.max() - r_arr.min()) * 255)).astype('uint8')
        r_img = Image.fromarray(r_arr)
        r_img = r_img.resize((img_w, img_h))
        r_img.save(os.path.join(uploads_dir, 'seg.png'))
        tps_rec = res['tps_rec']
        tps_start = res['tps_start']
        tps_pred = res['tps_pred']
        tps_proc = res['tps_proc']
        proc_end = time.time()

        # Displays result
        t1 = int(np.round(req_send - proc_start, 0))
        t2 = int(np.round(tps_rec - req_send, 0))
        t3 = int(np.round(tps_start - tps_rec, 0))
        t4 = int(np.round(tps_pred - tps_start, 0))
        t5 = int(np.round(tps_proc - tps_pred, 0))
        t6 = int(np.round(req_resp - tps_proc, 0))
        t7 = int(np.round(proc_end - req_resp, 0))
        tt = t1 + t2 + t3 + t4 + t5 + t6 + t7
        return render_template('result.html', msk_show=msk_show, t1=t1, t2=t2, t3=t3,
                               t4=t4, t5=t5, t6=t6, t7=t7, tt=tt)
        return render_template('result.html', msk_show=msk_show, i_blob=i_blob, m_blob=m_blob)
    return render_template('index.html')


# Default route, renders image loading form
#
# @return void
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# Application startup
if __name__ == '__main__':
    app.run()
