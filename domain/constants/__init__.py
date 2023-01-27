## storing all the constants at one place

import os
from datetime import datetime


ROOT_DIR = os.getcwd() # Working directory of app.py

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)


CURRENT_TIME_STAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

## Training Pipeline related variables

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"


## Data Ingestion related variables
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config" # Upper level for getting dictionary for data ingestion
DATA_INGESTION_ARTIFACT_DIR_KEY = "data_ingestion" # Special variable, Directory where we store the artifacts with respect to Data Ingestion
DATA_INGESTION_DATASET_DIR_KEY  = "dataset_dir"
DATA_INGESTION_DATASET_NAME_KEY = "dataset_name"
DATA_INGESTION_TABLE_NAME_KEY = "table_name"
DATA_INGESTION_TOP_FEATURES_KEY = "top_features"
DATA_INGESTION_INGESTED_DIR_KEY = "ingested_dir"
DATA_INGESTION_INGESTED_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_INGESTED_TEST_DIR_KEY = "ingested_test_dir"



## Data Validation related variables
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_SCHEMA_DIR_KEY = "schema_dir"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY = "schema_file_name"
DATA_VALIDATION_ARTIFACT_DIR_NAME = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME_KEY = "report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY = "report_page_file_name"


## Data Transformation related variables
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION_ARTIFACT_DIR_NAME = "data_transformation"
DATA_TRANSFORMATION_USE_BOX_COX_KEY = "use_box_cox_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY = "tranformed_dir"
DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR_KEY = "transformed_train_dir"
DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY = "preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSING_OBJECT_FILE_NAME_KEY = "preprocessed_object_file_name"
BOX_COX_FEATURES = ['length_url']

SCHEMA_COLUMNS_KEY = "columns"
SCHEMA_TARGET_COLUMN_KEY = "target_column"
SCHEMA_TARGET_COLUMN_TYPE_KEY = "target_column_type"

## Model Trainer Related Variables
MODEL_TRAINER_CONFIG_KEY = "model_trainer_config"
MODEL_TRAINER_ARTIFACT_DIR = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR_KEY = "trained_model_dir"
MODEL_TRAINER_MODEL_FILE_NAME_KEY = "model_file_name"
MODEL_TRAINER_SCORING_PARAMETER_FOR_GRID_SEARCH_CV_KEY = "scoring_parameter_for_grid_search_cv"
MODEL_TRAINER_BASE_RECALL_KEY = "base_recall"
MODEL_TRAINER_BASE_PRECISION_KEY =  "base_precision"
MODEL_TRAINER_MODEL_CONFIG_DIR_KEY = "model_config_dir"
MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY = "model_config_file_name"
MODEL_TRAINER_CUSTOM_THRESHOLD = "custom_threshold"


### Model Evaluation Related Keys
MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_EVALUATION_CONFIG_ARTIFACT_DIR_KEY = "model_evaluation"
MODEL_EVALUATION_FILE_NAME_KEY = "model_evaluation_file_name"

BEST_MODEL_KEY = "best_model"
HISTORY_KEY = "history"
MODEL_PATH_KEY = "model_path"

### Model Pusher variables
MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
MODEL_PUSHER_MODEL_EXPORT_DIR_KEY = "model_export_dir"


### Experiment Variables
EXPERIMENT_DIR_NAME = "experiment"
EXPERIMENT_FILE_NAME = "experiment.csv"

