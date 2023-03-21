from LoanApproval import CONFIG_FILE_PATH
from LoanApproval.utils import read_yam_file, create_directories
from LoanApproval import log
from pathlib import Path

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} started")
        self.config = read_yam_file(config_file_path)
        create_directories([self.config['artifacts_root']])

    def data_ingestion_config(self):
        config = self.config['data_ingestion']
        config_root_dir = Path(config['root_dir'])
        create_directories([config_root_dir])

        data_ingestion_config = {"root_dir": Path(config['root_dir']), "source_url": config['source_url'], 
                                 "local_files": Path(config['local_files']), 'url_path':config['url_path']}

        return data_ingestion_config 
    