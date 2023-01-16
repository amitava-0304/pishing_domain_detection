from domain.exception import PishingException
from domain.logger import logging
from domain.predictor import ModelResolver
import pandas as pd
from domain.utils import load_object
import os,sys
from datetime import datetime

PREDICTION_DIR="prediction"

import numpy as np
def start_batch_prediction(input_file_path):
    try:
        predict=0.0
        xtx=0.0
        os.makedirs(PREDICTION_DIR,exist_ok=True)
        logging.info(f"Creating model resolver object")
        model_resolver = ModelResolver(model_registry="saved_models")
        logging.info(f"Reading file :{input_file_path}")
        #df = pd.read_csv(input_file_path)
        #df = df.drop(['Unnamed: 0'],axis=1)
        df=input_file_path
        logging.info(df.columns)
        #df.replace({"na":np.NAN},inplace=True)
        #validation
        
        logging.info(f"Loading transformer to transform dataset")
        transformer = load_object(file_path=model_resolver.get_latest_transformer_path())
        
        #input_feature_names =  list(transformer.feature_names_in_)
        input_feature_names =  df.columns
        input_arr = transformer.transform(df[input_feature_names])

        logging.info(f"Loading model to make prediction")
        model = load_object(file_path=model_resolver.get_latest_model_path())
        prediction = model.predict(input_arr)
        y_pro_phishing = model.predict_proba(input_arr)[0,0]
        y_pro_non_phishing = model.predict_proba(input_arr)[0,1]
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        logging.info(pred)
        #target_encoder = load_object(file_path=model_resolver.get_latest_target_encoder_path())
        predict=round(y_pro_phishing*100,2)
        predict1=round(y_pro_non_phishing*100,2) 
        y_pro_non_phishing=round(y_pro_non_phishing,2)
        cat_prediction = prediction
        logging.info(prediction)
        #df["prediction"]=prediction
        #df["cat_pred"]=cat_prediction
        num = y_pro_non_phishing*100
        if (0<=y_pro_non_phishing and y_pro_non_phishing<0.50):
            num = 100-y_pro_non_phishing
        elif(y_pro_non_phishing<=1 and y_pro_non_phishing>=0.50):
            xtx=num
        elif (0<=y_pro_non_phishing and y_pro_non_phishing<0.50):
            xtx=num
      

        #prediction_file_name = os.path.basename(input_file_path).replace(".csv",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.csv")
       # prediction_file_path = os.path.join(PREDICTION_DIR,prediction_file_name)
        #df.to_csv(prediction_file_path,index=False,header=True)
        logging.info("Prediction Done......")
        logging.info(prediction,predict,predict1)
        return prediction,predict,predict1
    except Exception as e:
        raise PishingException(e, sys)
