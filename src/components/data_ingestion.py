import pandas as pd
import os
import sys
from dataclasses import dataclass 
from src.logger import logging
from src.exception import CustomException

from sklearn.model_selection import train_test_split


## intialize the data ingestion configuration
@dataclass

class DataIngestionconfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')
    


## create a data ingestion class  

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig() 
        
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method is starts")
        
        
        try:
            
            df=pd.read_csv(os.path.join('notebooks/data','Raw_Housing_Prices.csv'))
            logging.info("Dataset read as pandas DataFrame")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            
            logging.info('Train Test Split')
            
            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)
        
            logging.info("Ingestion of data in completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        
        
        except Exception as e:
            logging.info("Error occured in Data Ingestion Config")