<h1 align="center">
  <br>
  <img src="https://github.com/1Tatsumaru1/drive-image-segmentation/blob/master/img/techno.png" alt="Application technologies" width="200">
  <br>
  Image Segmentation Application & API
  <br>
</h1>

<h4 align="center">
  Built from the  
  <a href="https://www.cityscapes-dataset.com/dataset-overview/" target="_blank">Cityscape dataset</a>.
</h4>

![screenshot](https://github.com/1Tatsumaru1/drive-image-segmentation/blob/master/img/screenshot.png)

<p align="center">
  <a href="#description">Description</a> •
  <a href="#contents">Contents</a> •
  <a href="#credits">Credits</a> •
  <a href="#links">Links</a>
</p>

## Description

This project was part of my IA Engineering course at OpenClassrooms. 
The aim was to :<br>
* Factorize the initial segmentation masks 32 categories of the <a href="https://www.cityscapes-dataset.com/dataset-overview/" target="_blank">Cityscape dataset</a> to 8 macro categories
* Develop a segmentation model through a comparison of various encoder-decoder architectures
* Develop a final product consisting in an application and an API both available from the cloud :
  - The **API** receives an image and returns its segmentation mask
  - The **Application** is an interface allowing the user to post a picture and compare the resulting mask with the original picture

Both the Application and the API use a technical stack made up of Flask and Docker, and have been made available from the Google Compute Engine around the time of the evaluation of this project :

![screenshot](https://github.com/1Tatsumaru1/drive-image-segmentation/blob/master/img/architecture.png)

## Contents

* **segmentation_model.ipynb** (Jupyter Notebook) : after a brief analysis of the dataset, performs the category mapping, builds a custom data generator, and compares different model alternatives in order to segment images. This task could be perform swiftly thanks to the amazing computer vision library made by <a href="https://github.com/divamgupta/image-segmentation-keras">Divam Gupta</a>
* **API** : the Flask API
* **Flask application** : the Flask Application, no surprise here :)

## Credits

This project makes use of the following packages:

- [Keras](https://keras.io/)
- [Tensorflow](https://www.tensorflow.org/?hl=fr)
- [Flask](https://pypi.org/project/Flask/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Numpy](https://numpy.org/)
- [Requests](https://docs.python-requests.org/en/latest/index.html)
- [Divam Gupta Keras code base](https://github.com/divamgupta/image-segmentation-keras)

## Links

> <a href="https://anthony.ledouguet.com"><img src="https://github.com/1Tatsumaru1/azure_reco_api/blob/main/img/world.png" alt="website" width="20" /> anthony.ledouguet.com</a><br>
> <a href="https://github.com/1Tatsumaru1"><img src="https://github.com/1Tatsumaru1/azure_reco_api/blob/main/img/github.png" alt="github" width="20" /> GitHub</a><br>
> <a href="https://www.linkedin.com/in/anthony-le-douguet/"><img src="https://github.com/1Tatsumaru1/azure_reco_api/blob/main/img/linkedin.png" alt="linkedin" width="20" />
LinkedIn</a>
