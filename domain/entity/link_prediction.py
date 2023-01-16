import pandas as pd
import pickle
import numpy as np
from datetime import datetime
import re
from domain.pipeline.link_prediction import start_batch_prediction
from domain.entity.feature_extractor import FeatureExtractor
# It is used for checking whether the link can be accesable or not
from urllib.request import urlopen
from urllib.error import *
from domain.logger import logging

class Prediction_from_link:
    def __init__(self,link):
        self.link = link
    def check_link(self):
        '''
            This function is to check whether the link is working or not!
        '''
        try:
            html = urlopen(self.link)
            return "0"

        except HTTPError as e:
            print("HTTP error", e)
            return "2"

        except URLError as e:
            print("Opps ! Page not found!", e)

            return "4"

        except Exception as e:
            print("Exception errored in checking the link",e)
            return "3"

    def check_http(self):
        check = re.findall("https|http",self.link)
        if(check):
            return 0
        else:
            return 1

    def predict(self,url_list):
        try:
            print("Prediction from link started")
            '''checking_http = self.check_http()
            if(checking_http):
                return "5"
            test = self.check_link()
            print("test is:", test)
            print(type(test))
            if(test == "4" or test == "2" or test == "3"):
                return test'''
            extractor = FeatureExtractor()
            features_from_url_df = extractor.generate_dataframe_from_urls(url_list)
            x = features_from_url_df.copy()
            x.to_csv("output.csv")
            print(x)
            logging.info(x)
            #output_file,pre,pre1 = start_batch_prediction(input_file_path='output.csv')
            output_file,pre,pre1 = start_batch_prediction(input_file_path=x)
            print(output_file)
            print("Phishing")
            print(output_file)
            logging.info("batch_prediction from link is done...")
            return output_file,pre,pre1

        except Exception as e:
            print("error in predict function")
            print(e)
            return e
