from LoanApproval import log
from LoanApproval.utils import read_yam_file, create_directories
from LoanApproval import CONFIG_FILE_PATH
from pathlib import Path
import os

STAGE_NAME = "Data Preprocessing Stage"

class DataPreprocessConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} started")
        self.config = read_yam_file(config_file_path)
        self.dataset_load = os.path.join(self.config['data_ingestion']['root_dir'], self.config['data_ingestion']['local_files'])
        create_directories([self.config['artifacts_root']])
    
    def data_preprocess_config(self):
        config = self.config['data_preprocessing']
        create_directories([Path(config['root_dir'])])

        data_preprocess_config = {"root_dir": Path(config['root_dir']), "dataset_load": Path(self.dataset_load),
                                 "local_file": Path(config['local_file'])}
        return data_preprocess_config
   