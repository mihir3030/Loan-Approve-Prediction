import os
import pandas as pd
from LoanApproval import log
from pathlib import Path

STAGE_NAME = "Data Ingestion Stage"

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_data(self):
        url = self.config['source_url']
        log.info(f"dataset downloading from {url}")
        path = self.config['url_path']+url.split('/')[-2]
        self.df = pd.read_csv(path)
        log.info(f"dataset download successfully from {url}")
    
    def save_data(self):
        data_ingestion_root_dir = Path(self.config['root_dir'])
        local_file_dir = Path(self.config['local_files'])

        raw_local_file_path = os.path.join(data_ingestion_root_dir, local_file_dir)

        self.df.to_csv(raw_local_file_path, index=False)
        log.info(f"data saved successfully at {raw_local_file_path}")

        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} compleated successfully compleated")