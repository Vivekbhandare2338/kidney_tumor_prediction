from src.cnnClassifier.pipeline.stage_01_dataingpipeline import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_preparebasepipeline import PrepareBaseModelTrainingPipeline
from src.cnnClassifier import *



STAGE_NAME = "Data Ingestion stage"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  data_ingestion = DataIngestionTrainingPipeline()
  data_ingestion.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e



STAGE_NAME = "prepare base model"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  prepare_base_model = PrepareBaseModelTrainingPipeline()
  prepare_base_model.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e