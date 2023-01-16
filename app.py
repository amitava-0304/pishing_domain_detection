########### NOTE: #####################
# Install packages from requirements.txt only otherwise it will give version error
from wsgiref import simple_server
import os,sys
from flask import Flask, session, request, Response, jsonify, render_template,redirect,url_for,flash,Markup,send_file
import json
from domain.pipeline.batch_prediction import start_batch_prediction
from domain.logger import logging
from domain.entity.uploadsValidation import Validation
from domain.entity.json_values import Json_values
from domain.pipeline.url_prediction import Prediction_from_link
from domain.entity.phishing_estimator import PhishingEstimator
from domain.exception import PishingException
from flask_cors import CORS,cross_origin
from flask import Flask, render_template,request,redirect,url_for
ROOT_DIR = os.getcwd()
model_directory = "domain"
pipeline_folder = "entity"
MODEL_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, model_directory,pipeline_folder ,"predict_cols_validation.json")
saved_directory = "saved_models"
app = Flask(__name__)


@app.route('/',methods = ['GET'])
#@cross_origin()
def home_page():
    return render_template('home.html')

@app.route('/columns_details',methods =['GET'])
#@cross_origin()
def cols():
    print(ROOT_DIR)
    json_values_obj = Json_values(MODEL_CONFIG_FILE_PATH)
    keys, values,description = json_values_obj.data()
    with open(MODEL_CONFIG_FILE_PATH, 'r') as f:
        dic = json.load(f)
        f.close()
    return render_template('column_details.html',values= values,keys = keys,description = description)

@app.route('/predict_main',methods = ['GET'])
#@cross_origin()
def prediction_main():
    return render_template('predict_main.html')


@app.route('/predict_from_csv',methods =['GET','POST'])
#@cross_origin()
def predict():
    if(request.method == 'GET'):
        return render_template('predict_from_csv.html')
    elif(request.method == 'POST'):
        try:
            
            #start_training_pipeline()
            print(request.files['csvfile'].filename)
            global output_file
            output_file = start_batch_prediction(input_file_path=request.files['csvfile'].filename)
            print(output_file)
            logging.info(f"start_training_pipeline")
            return render_template('result_of_add.html',data = "Data Has been added and file is validated",check = True)

        except (UnicodeDecodeError,TypeError) as x:
            print("checking")
            return render_template('result_of_add.html',data = "Please enter a .csv extension",check = False)
        except Exception:
            print("Exception checking",repr(Exception))
            render_template('result_of_add.html',data = "Exception",check = False)


@app.route('/predict_from_link',methods = ['GET','POST'])
#@cross_origin()
def predict_from_link():
    if(request.method == 'GET'):
        return render_template('predict_from_link.html')
    elif(request.method == 'POST'):
        try:
            link = request.form.get("link")
            predict_obj = Prediction_from_link()
            phishing,pre,pre1 = predict_obj.predict(link)
            print(phishing,pre,pre1)
            print("Phishing or not:" + str(phishing[0]))

            return render_template('result_predict_link.html',result = str(phishing[0]),link = link,xx =round(pre,2),xx1 =round(pre1,2))


        except Exception as e:
            print(e)

@app.route('/download',methods = ['GET'])
#@cross_origin()
def download_file():
    return send_file(output_file,as_attachment=True)

#port =int(os.getenv("PORT",5001))

'''if __name__ == '__main__':
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host, port = port, app = app)
    print("http://localhost:5001/" )
    httpd.serve_forever()
    app.run()'''

if __name__ == '__main__':  # Script executed directly?
    app.run(debug=True)  # Launch built-in web server and run this Flask webapp