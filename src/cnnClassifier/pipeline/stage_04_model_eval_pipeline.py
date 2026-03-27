from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_eval_component import Evaluation
from src.cnnClassifier import logger
import os


STAGE_NAME = "Evaluation stage"




class EvaluationPipeline:
    def __init__(self):
        os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Vivekbhandare2338/kidney_tumor_prediction.mlflow"
        # Set your DagsHub credentials (MLflow uses HTTP Basic Auth)
        os.environ["MLFLOW_TRACKING_USERNAME"] = "Vivekbhandare2338"
        os.environ["MLFLOW_TRACKING_PASSWORD"] = "2f026ec118f9b37c641403d506af757274590b7b"
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()

