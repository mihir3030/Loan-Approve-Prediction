import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.metrics import accuracy_score, f1_score
from LoanApproval.utils import save_reports
import os
from LoanApproval import log

STAGE_NAME = "Training Stage"

class Training:
    def __init__(self, config):
        self.config = config

    def splitting_data(self):
        data_path = self.config['dataset_load']
        df = pd.read_csv(data_path)
        self.train, self.test = train_test_split(df, test_size=0.2, random_state=33)
        root_dir = self.config['root_dir']
        test_data = self.config['test_data']
        test_data_save_file = os.path.join(root_dir, test_data)
        log.info(f"Splitting done and test data save at {test_data_save_file}")
        self.test.to_csv(test_data_save_file, index=False)    
    
   
    def training(self):
        x = self.train.drop('Loan_Status', axis=1)
        y = self.train['Loan_Status']

        self.lr_model = LogisticRegression()
        self.lr_model.fit(x, y)
        log.info(f"Training done ith Elastic model")

        # saving model
        root_dir = self.config['root_dir']
        local_model_file = self.config['local_model_file']
        local_model_save_path = os.path.join(root_dir, local_model_file)
        joblib.dump(self.lr_model, local_model_save_path)
        log.info(f"model save at {local_model_save_path}")

     #Function to evaluate the models and output the accuracy score of the model
    def evaluate(self):
        x_test = self.test.drop("Loan_Status", axis=1)
        y_test = self.test['Loan_Status']

        y_pred = self.lr_model.predict(x_test)
        test_accuracy_score = accuracy_score(y_test, y_pred)
        f1_test_score = f1_score(y_test, y_pred)
        
        scores = {
            'test_accuracy': test_accuracy_score,
            'f1_score': f1_test_score
        }
        raw_path = self.config['root_dir']
        score_save_file = self.config['score_save']

        score_save_path = os.path.join(raw_path, score_save_file)

        save_reports(scores, score_save_path)
        log.info(f"model test_score save at {score_save_path}")

        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} compleated successfully compleated\n")