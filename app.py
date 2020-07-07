# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle
import os

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("base.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            crim = float(request.form['crim'])
            zn = float(request.form['zn'])
            indus = float(request.form['indus'])
            chas = float(request.form['chas'])
            nox = float(request.form['nox'])
            rm = float(request.form['rm'])
            age = float(request.form['age'])
            dis = float(request.form['dis'])
            rad = float(request.form['rad'])
            tax = float(request.form['tax'])
            ptratio = float(request.form['ptratio'])
            b = float(request.form['b'])
            lstat = float(request.form['lstat'])

            filename = 'finalised_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])
            # showing the prediction results in a UI
            return render_template('prediction.html', value=round(1000*prediction[0]))

        except:
            return ('Something Went Wrong')
    else:
        return render_template('base.html')


port = int(os.getenv("PORT"))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)