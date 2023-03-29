from LoanApproval.data_ingestion import DataIngestionConfigurationManager, DataIngestion
from LoanApproval.data_preprocessing import DataPreprocessConfigurationManager, DataPreprocessing
from LoanApproval.training import TrainingConfigurationManager, Training
from LoanApproval import log

#STAGE_NAME = "Data Ingestion Stage"

def start_training_pipeline():
    
    # data_ingestion_stage
    data_ingestion_config_manager = DataIngestionConfigurationManager()
    data_ingestion_config = data_ingestion_config_manager.data_ingestion_config()
    data_ingestion = DataIngestion(config = data_ingestion_config)
    data_ingestion.download_data()
    data_ingestion.save_data()

    # data preprocessing stage
    data_preprocess_config_manager = DataPreprocessConfigurationManager()
    data_preprocess_config = data_preprocess_config_manager.data_preprocess_config()
    data_preprocess = DataPreprocessing(config=data_preprocess_config)
    data_preprocess.handle_missing_value()
    data_preprocess.cat_to_numeric()
    data_preprocess.handle_imbalanced_data()
    data_preprocess.scaling_data()
    data_preprocess.save_preprocess_data()

    # Training Stage
    training_config_manager = TrainingConfigurationManager()
    training_config = training_config_manager.get_training_config()
    training = Training(training_config)
    training.splitting_data()
    training.training()
    training.evaluate()


if __name__ == "__main__":
    try:
        log.info(f">>>>>>>>>>>>>>>>> Training Pipeline started")
        start_training_pipeline()
        log.info(f">>>>>>>>>>>>>>>>>> Training Pipeline compleated successfully\n\n X========================X\n\n")
    except Exception as e:
        log.exception(e)
        log.info("\n\nX========================X\n\n")
        raise e