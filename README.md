# Project Title
House Price Prediction with Deployment

## Introduction
This is one of my Machine Learning projects from [Machine Learning and Deep Learning with Deployment](https://academy.ineuron.ai/machine-learning-masters.php) course, from [iNeuron.ai](https://academy.ineuron.ai/index.php). In this project, to predict the price of a house based on the parameters given by the user, using a pre-trained Machine Learning(Multiple Linear Regression) model. The code needs to take the parameters from the user through a HTML form, use the obtained data to predict the house price, and display the predicted price to the user using other HTML page.

**Multiple Regression -**  It is an extension of simple linear regression. It is used when we want to predict the value of a variable based on the value of two or more other variables.

## Install
This project requires Python3. Also, some of the python libraries like Flask, and pickle(pre-installed with python).
All the libraries can be installed using the following commands...
```
pip install flask
```
The project also requires **Heroku CLI** for deploying the app on the cloud which can be installed from [here](https://devcenter.heroku.com/articles/heroku-cli). The download can be confirmed by running the following command in terminal/ cmd<br>
```
heroku
``` 
Also, the project requires some basic HTML knowledge to build the web pages for taking input form the user and displaying the result to the user.

## Application Architecture
![Blank Diagram](https://user-images.githubusercontent.com/50728879/86828327-b7e16300-c0b0-11ea-8d2a-09257c71e524.png)

## Code
* `Step-1` Start the flask app which will run the **"base.html"** on the cloud and get the parameters given by the user.
* `Step-2` Load the pre-trained model, stored in *finalised_model.pickle*.
* `Step-3` Prediction is made using the model loaded in Step-2
* `Step-4` Show the  to the user through **"prediction.html"**

## Deployment

To deploy the app on the cloud, the following steps are followed-
* `Step-1` Create an account on Heroku, which can be done from [here](https://signup.heroku.com/t/platform?c=7013A000000ib1xQAA&gclid=Cj0KCQjwupD4BRD4ARIsABJMmZ_Ty2TKvICQqujWmS0-eRYP6KFCy_xgRz5SI-DXg2T9BevPhJ5fsGAaAlf7EALw_wcB)
* `Step-2` Open the **Terminal(Linux/ Mac)** or **Cmd(Windows)** and navigate to the folder that contaions all the file.
* `Step-3` Run ```sudo apt install git``` to install git in the system.
* `Step-4` Run ```heroku login``` command. On execution, it will open login page on default web browser.
* `Step-5` After, logging in run the following commands and wait for some time. On successful execution, it will provide the URL for the app.
```
heroku create <app_name>
git init
git add .
git commit -m "Final commit"
git push heroku master
``` 
The link for runnig app is - https://house-price-prediction20.herokuapp.com/

|  |
|:--:|
|***App Preview***|

