from LoanApproval.data_ingestion import DataIngestionConfigurationManager, DataIngestion
from LoanApproval.data_preprocessing import DataPreprocessConfigurationManager, DataPreprocessing
from LoanApproval import log

#STAGE_NAME = "Data Ingestion Stage"

def start_training_pipeline():
    
    # data_ingestion_stage
    config = DataIngestionConfigurationManager()
    data_ingestion_config = config.data_ingestion_config()
    data_ingestion = DataIngestion(config = data_ingestion_config)
    data_ingestion.download_data()
    data_ingestion.save_data()

    # data preprocessing stage
    config = DataPreprocessConfigurationManager()
    data_preprocess_config = config.data_preprocess_config()
    data_preprocess = DataPreprocessing(config=data_preprocess_config)
    data_preprocess.handle_missing_value()
    data_preprocess.cat_to_numeric()
    data_preprocess.handle_imbalanced_data()
    data_preprocess.scaling_data()
    data_preprocess.save_preprocess_data()

if __name__ == "__main__":
    try:
        log.info(f">>>>>>>>>>>>>>>>> Training Pipeline started")
        start_training_pipeline()
        log.info(f">>>>>>>>>>>>>>>>>> Training Pipeline compleated successfully\n\n X========================X\n\n")
    except Exception as e:
        log.exception(e)
        raise e