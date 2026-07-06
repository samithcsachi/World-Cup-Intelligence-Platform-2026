import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

PROJECT_NAME = "world_cup_intelligence_platform_2026"
SRC = f"src/{PROJECT_NAME}"

FILES = [

    f"{SRC}/__init__.py",

    # Core
    f"{SRC}/core/__init__.py",
    f"{SRC}/core/exceptions.py",     
    f"{SRC}/core/logger.py",          
    f"{SRC}/core/utils.py",           

    # Config
    f"{SRC}/config/__init__.py",
    f"{SRC}/config/configuration.py",  
    f"{SRC}/config/constants.py",   
    f"{SRC}/config/settings.yaml",   


    # Pipelines
    f"{SRC}/pipeline/__init__.py",
    f"{SRC}/pipeline/training_pipeline.py",
    f"{SRC}/pipeline/prediction_pipeline.py", 
    f"{SRC}/pipeline/evaluation_pipeline.py", 
    f"{SRC}/pipeline/feature_pipeline.py",

    # Ingestion
    f"{SRC}/ingestion/__init__.py",
    f"{SRC}/ingestion/fifa_rankings.py",      
    f"{SRC}/ingestion/elo_ratings.py", 
    f"{SRC}/ingestion/historical_matches.py", 
    f"{SRC}/ingestion/live_results.py", 
    f"{SRC}/ingestion/ingestion_pipeline.py",  

    # Validation 

    f"{SRC}/validation/__init__.py",
    f"{SRC}/validation/schema_validation.py",  
    f"{SRC}/validation/data_quality.py",       
    f"{SRC}/validation/validation_report.py",  

    # Preprocessing
    f"{SRC}/preprocessing/__init__.py",
    f"{SRC}/preprocessing/clean_matches.py",         
    f"{SRC}/preprocessing/clean_rankings.py",  
    f"{SRC}/preprocessing/merge_datasets.py",
    f"{SRC}/preprocessing/preprocessing_pipeline.py",

    # Features
    f"{SRC}/features/__init__.py",
    f"{SRC}/features/base_features.py",
    f"{SRC}/features/elo_features.py",       
    f"{SRC}/features/ranking_features.py",     
    f"{SRC}/features/form_features.py",     
    f"{SRC}/features/h2h_features.py",      
    f"{SRC}/features/tournament_features.py",
    f"{SRC}/features/feature_store.py",   
    f"{SRC}/features/build_features.py",       

    # Models
    f"{SRC}/models/__init__.py",        

    # Poisson
    f"{SRC}/models/poisson/__init__.py",
    f"{SRC}/models/poisson/train.py",         
    f"{SRC}/models/poisson/predict.py",       
    f"{SRC}/models/poisson/evaluate.py",      

    # Dixon-Coles
    f"{SRC}/models/dixon_coles/__init__.py",
    f"{SRC}/models/dixon_coles/train.py",     
    f"{SRC}/models/dixon_coles/predict.py",    
    f"{SRC}/models/dixon_coles/evaluate.py",   

    # XGBoost
    f"{SRC}/models/xgboost/__init__.py",
    f"{SRC}/models/xgboost/train.py",    
    f"{SRC}/models/xgboost/predict.py",    
    f"{SRC}/models/xgboost/evaluate.py",

    # Ensemble
    f"{SRC}/models/ensemble/__init__.py",
    f"{SRC}/models/ensemble/combine.py",   
    f"{SRC}/models/ensemble/predict.py", 

    # Model Registry
    f"{SRC}/models/registry/__init__.py",
    f"{SRC}/models/registry/model_registry.py",
    f"{SRC}/models/registry/model_loader.py",  

    # Simulation
    f"{SRC}/simulation/__init__.py",
    f"{SRC}/simulation/match_simulator.py",     
    f"{SRC}/simulation/group_stage.py",   
    f"{SRC}/simulation/knockout_stage.py",
    f"{SRC}/simulation/monte_carlo.py",      
    f"{SRC}/simulation/tournament_simulator.py",

    # Evaluation
    f"{SRC}/evaluation/__init__.py",
    f"{SRC}/evaluation/metrics.py",         
    f"{SRC}/evaluation/calibration.py",   
    f"{SRC}/evaluation/reliability_curve.py",
    f"{SRC}/evaluation/surprise_index.py",  

    # Retraining
    f"{SRC}/retraining/__init__.py",
    f"{SRC}/retraining/fetch_latest_results.py", 
    f"{SRC}/retraining/train_challenger.py",  
    f"{SRC}/retraining/compare_models.py",   
    f"{SRC}/retraining/promote_model.py",   
    f"{SRC}/retraining/retraining_pipeline.py",  

    # Monitoring
    f"{SRC}/monitoring/__init__.py",
    f"{SRC}/monitoring/data_drift.py",         
    f"{SRC}/monitoring/prediction_drift.py",   
    f"{SRC}/monitoring/model_performance.py", 
    f"{SRC}/monitoring/monitoring_pipeline.py",

    # API
    f"{SRC}/api/__init__.py",
    f"{SRC}/api/main.py",                    

    # Routers
    f"{SRC}/api/routers/__init__.py",
    f"{SRC}/api/routers/predict.py",           
    f"{SRC}/api/routers/simulate.py",          
    f"{SRC}/api/routers/teams.py",       
    f"{SRC}/api/routers/results.py",     

    # Services
    f"{SRC}/api/services/__init__.py",
    f"{SRC}/api/services/prediction_service.py", 
    f"{SRC}/api/services/simulation_service.py",

    # Schemas
    f"{SRC}/api/schemas/__init__.py",
    f"{SRC}/api/schemas/prediction_schema.py", 
    f"{SRC}/api/schemas/simulation_schema.py", 

    # Orchestration
    f"{SRC}/orchestration/__init__.py",
    f"{SRC}/orchestration/full_pipeline_runner.py",
    f"{SRC}/orchestration/daily_update_pipeline.py",

    # Serving
    f"{SRC}/serving/__init__.py",
    f"{SRC}/serving/inference.py", 

    # Utils
    f"{SRC}/utils/__init__.py",
    f"{SRC}/utils/io_utils.py",  
    f"{SRC}/utils/data_utils.py",  
    f"{SRC}/utils/model_utils.py",  

    # Streamlit App
    "streamlit_app/__init__.py",
    "streamlit_app/app.py",                                      

    "streamlit_app/pages/__init__.py",
    "streamlit_app/pages/01_match_predictor.py",                 
    "streamlit_app/pages/02_tournament_simulator.py",
    "streamlit_app/pages/03_live_results.py", 
    "streamlit_app/pages/04_model_performance.py", 
    "streamlit_app/pages/05_model_monitoring.py", 
    "streamlit_app/pages/06_team_analysis.py", 
    "streamlit_app/pages/07_model_error_analysis.py", 

    # Notebooks
    "notebooks/01_data_exploration.ipynb",
    "notebooks/02_data_cleaning.ipynb",
    "notebooks/03_feature_engineering.ipynb",
    "notebooks/04_poisson_model.ipynb",
    "notebooks/05_dixon_coles.ipynb",
    "notebooks/06_xgboost.ipynb",
    "notebooks/07_ensemble_model.ipynb",
    "notebooks/08_model_comparison.ipynb",
    "notebooks/09_tournament_simulation.ipynb",

    # Tests
    "tests/__init__.py",
    "tests/test_ingestion.py",  
    "tests/test_features.py",
    "tests/test_models.py",
    "tests/test_simulator.py",
    "tests/test_api.py",
    "tests/test_monitoring.py",


    # Docker
    "docker/Dockerfile.api",       
    "docker/Dockerfile.streamlit",  
    "docker/docker-compose.yml", 

    # Github Actions Workflows
    ".github/workflows/ci.yml",     
    ".github/workflows/cd.yml", 
    ".github/workflows/train.yml",
    ".github/workflows/deploy.yml", 

    # Configs 
    "configs/paths.yaml",          
    "configs/model_config.yaml", 
    "configs/simulation_config.yaml", 
    "configs/api_config.yaml", 
    "configs/monitoring_config.yaml", 
    "configs/ensemble_weights.yaml", 

    # Root Files 
    "Makefile",       
    "pyproject.toml",  
    "dvc.yaml",     
    "params.yaml",
    "README.md",
    ".gitignore",
    ".env.example", 
]

DIRECTORIES = [

    # Artifacts 
    "artifacts/raw_data", 
    "artifacts/interim_data",  
    "artifacts/processed_data",
    "artifacts/features",
    "artifacts/models",
    "artifacts/models/production", 
    "artifacts/models/staging",  
    "artifacts/models/archive",
    "artifacts/metrics",
    "artifacts/predictions",
    "artifacts/simulations",
    "artifacts/calibration",
    "artifacts/monitoring",
    "artifacts/reports",
    "artifacts/figures", 
    "artifacts/logs",

   #Mlflow
    "mlruns",  

]


def create_directories() -> None:
    for directory in DIRECTORIES:
        path = Path(directory)
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory  : {path}")


def create_files() -> None:
    for file in FILES:
        file_path = Path(file)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if not file_path.exists():
            file_path.touch()
            logging.info(f"Created file       : {file_path}")
        else:
            logging.info(f"File already exists: {file_path}")


if __name__ == "__main__":
    logging.info("=" * 60)
    logging.info("World Cup Intelligence Platform 2026")
    logging.info("Creating project structure...")
    logging.info("=" * 60)

    create_directories()
    create_files()

    logging.info("=" * 60)
    logging.info("Project structure created successfully.")
    logging.info(f"Total files    : {len(FILES)}")
    logging.info(f"Total directories: {len(DIRECTORIES)}")
    logging.info("=" * 60)