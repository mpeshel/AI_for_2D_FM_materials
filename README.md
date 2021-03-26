# ME4101A-ShethRiyaNimish
# Final Year Project


The package implements three different techniques to classify two dimensional materials into ferromagnetic materials, anti-ferromagnetic materials and non-magnetic materials. 

The three techniques are:

- Classical Machine Learning.
- Deep Learning.
- Graph Networks.


## Table of Contents

- [Prerequisites](#prerequisites)
- [Files](#files)
- [Usage](#usage)
  - [Data Featurizing](#define-a-customized-dataset)
  - [Classical Machine Learning](#train-a-cgcnn-model)
  - [Deep Learning](#predict-material-properties-with-a-pre-trained-cgcnn-model)
  - [MEGNET](#megnet)
  - [CGCNN](#cgcnn)
- [Web Interface](#wi)
- [Data](#data)
- [Authors](#authors)




##  Prerequisites

This package requires:

- [PyTorch](http://pytorch.org)
- [scikit-learn](http://scikit-learn.org/stable/)
- [pymatgen](http://pymatgen.org)
- [keras](https://keras.io)
- [matminer](https://matminer.readthedocs.io/en/latest/)


If you are new to Python, the easiest way of installing the prerequisites is via [conda](https://conda.io/docs/index.html). Other minor requirements are mentioned in the requirements.txt document

## Files
- Data Preparation.ipynb:  Jupyter notebook used for data preparation
- Machine Learning.ipynb:  Jupyter notebook used for conducting classical ma-chine learning
- Deep  Learning.ipynb:  Jupyter  notebook  used  for  conducting  deep  learningalgorithms.
- CGCNN
  – CIF Data 
  – Crystal Graph Convolutional Nueral Netwroks.ipynb:  Jupyter notebookfor optimising and predicting the accuracy of CGCNN
  – Miscellaneous files such as the model, predict.py written by [21].
- Web Interface
 –model.pkl: Best model obtained during training to classify materials intomagnetic and non-magnetic.
 –model2.pkl:  Best  model  obtained  during  training  to  classify  magneticmaterials into ferromagnetic and anti-ferromagnetic materials.
 –averages.csv:  Stores the average value of the data stored.
 –data.csv:  The data used for training the above models
 –app.py:  The python file which helps in reading the input from the file.
 –index.html:  Stores the format of the app
 –mlmodel.py:  Helps in the facilitation of app.py
 –static:  Contains the fonts used in the web interface
- Documents
 –DFDP2DMatpedia.docx: Document containing results after data featurizing on 2DMatpedia.
 –DFDPC2DB.docx:  Document  containing  results  after  data  featurizingon C2DB.
 –ML.docx: Example Document containing results after Machine Learning.
 –DL.docx:  Example Document containing results after Deep Learning.
- Pictures:  Contains various graphics which are used in the jupyter notebooks
- Requirements  Text:  The  python  libraries  which  are  needed  to  execute  mycode.
- Data:
- Miscellaneous Data:  Data(NM/M)for ML, DL
 –CIF Data for CGCNN
 –DatawithFM/AFMClassification.csv
 –Data.json json file obtained from 2Dmatpdia
 –c2db.db a database obtained from computational 2d materials databse
- Surface Plots:  Matlab Code
- MEGNET
 –Graph Network.ipynb: Jupyter notebook to compute the accuracy of theMEGNET model.

## Usage





## Authors

The code was primarily written by Sheth Riya Nimish who was advised by Prof. Shen Lei. 
Appropriate citations can be found in the code itself for borrowed code.

