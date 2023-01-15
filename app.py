from flask import Flask, request
import os
from flask import render_template
from AppFlow.pipeline.pipeline import Pipeline
from AppFlow.logger import logging
from AppFlow.exception import CreditcardException
from AppFlow.logger import get_log_dataframe
from AppFlow.predictor.creditcard_predictor import CreditcardDefaultPredictor,CreditcardData

#For getting the path of the trained model.
ROOT_DIR = os.getcwd()
TRAINED_MODEL_DIR_NAME = "trained_model"
TRAINED_MODEL_FILE_NAME = "model.pkl"
MODEL_DIR = os.path.join(ROOT_DIR, TRAINED_MODEL_DIR_NAME,TRAINED_MODEL_FILE_NAME)

CREDITCARD_DATA_KEY = "creditcard_data"
DEFAULTERS_VALUE_KEY = "credicard_default_value"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/predict', methods=['GET','POST'])
def predict():
    context = {
        CREDITCARD_DATA_KEY: None,
        DEFAULTERS_VALUE_KEY: None
    }
    if request.method == 'POST':
        LIMIT_BAL = float(request.form['LIMIT_BAL'])
        SEX = request.form['SEX']
        EDUCATION = request.form['EDUCATION']
        MARRIAGE = request.form['MARRIAGE']
        AGE = float(request.form['AGE'])
        PAY_1 = float(request.form['PAY_1'])
        PAY_2 = float(request.form['PAY_2'])
        PAY_3 = float(request.form['PAY_3'])
        PAY_4 = float(request.form['PAY_4'])
        PAY_5 = float(request.form['PAY_5'])
        PAY_6 = float(request.form['PAY_6'])
        BILL_AMT1 = float(request.form['BILL_AMT1'])
        PAY_AMT1 = float(request.form['PAY_AMT1'])
        PAY_AMT2 = float(request.form['PAY_AMT2'])
        PAY_AMT3 = float(request.form['PAY_AMT3'])
        PAY_AMT4 = float(request.form['PAY_AMT4'])
        PAY_AMT5 = float(request.form['PAY_AMT5'])
        PAY_AMT6 = float(request.form['PAY_AMT6'])

        creditcard_data = CreditcardData(LIMIT_BAL = LIMIT_BAL,
                                        SEX = SEX,
                                        EDUCATION = EDUCATION,
                                        MARRIAGE = MARRIAGE,
                                        AGE = AGE,
                                        PAY_1 = PAY_1,
                                        PAY_2 = PAY_2,
                                        PAY_3 = PAY_3,
                                        PAY_4 = PAY_4,
                                        PAY_5 = PAY_5,
                                        PAY_6 = PAY_6,
                                        BILL_AMT1 = BILL_AMT1,
                                        PAY_AMT1 = PAY_AMT1,
                                        PAY_AMT2 = PAY_AMT2,
                                        PAY_AMT3 = PAY_AMT3,
                                        PAY_AMT4 = PAY_AMT4,
                                        PAY_AMT5 = PAY_AMT5,
                                        PAY_AMT6 = PAY_AMT6,
                                        )
        creditcard_df = creditcard_data.get_creditcard_input_data_frame()
        creditcard_predictor = CreditcardDefaultPredictor(model_dir=MODEL_DIR)
        credicard_default_value = creditcard_predictor.predict(X_test=creditcard_df)
        context = {
            CREDITCARD_DATA_KEY: creditcard_data.get_creditcard_data_as_dict(),
            DEFAULTERS_VALUE_KEY: credicard_default_value, 
        }
        return render_template('predict.html', context=context)
    return render_template('predict.html', context=context)
    #     return render_template('predict.html',context=credicard_default_value)
    # return render_template('predict.html',context="ravi")

@app.route('/about', methods=['GET', 'POST'])
def about():
    try:
        return render_template('about.html')
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)


