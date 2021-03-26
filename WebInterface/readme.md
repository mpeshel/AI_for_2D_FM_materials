## Web Interface
After the completion of the machine learning and deep learning models, it is important to deploy the models so that it is available to the end-users. In this case, the models are deployed via web interfaces. With the web interfaces, users would be able to predict the results for their inputs without installing any models or downloading any code on their own computer.
The model is deployed such that other users can easily access them through an API (application programming interface) to make predictions. This was done using Flask and Heroku — Flask is a micro web framework that does not require particular tools or libraries to create web applications and Heroku is a cloud platform that can host web applications
In this web application,  20 of the most important features were used as the input parameters. It is noted that some features may be unavailable to users and hence an option to enter NA has been provided. The reason that the model works with only the 20 features is because the other features have negligible contribution to the model, as was understood after creating the feature importance plot of all the features.

The best model that was obtained by the author can be found here:
- [Model to classify into Magnetic and Non Magnetic Materials](https://github.com/RiyaBOT/ME4101A-ShethRiyaNimish/blob/master/WebInterface/model.pkl)
- [Model to classify into Ferromagnetic and Anti-Ferromagnetuc Materials](https://github.com/RiyaBOT/ME4101A-ShethRiyaNimish/blob/master/WebInterface/model2.pkl)

However, it is much easier to use the web interface created by the author for the prediction of the magnetic orientation, which can be found here:
- [Web Interface](https://twodferromagnetism-model.herokuapp.com)
