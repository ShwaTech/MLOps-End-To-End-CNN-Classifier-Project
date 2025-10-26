import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/main.yaml",
    ".jenkins/Jenkinsfile",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/comp_01_data_ingestion.py",
    f"src/{project_name}/components/comp_02_prepare_base_model.py",
    f"src/{project_name}/components/comp_03_model_trainer.py",
    f"src/{project_name}/components/comp_04_model_evaluation.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_prepare_base_model.py",
    f"src/{project_name}/pipeline/stage_03_model_trainer.py",
    f"src/{project_name}/pipeline/stage_04_model_evaluation.py",
    f"src/{project_name}/pipeline/stage_05_prediction_pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "terraform/main.tf",
    "terraform/providers.tf",
    "terraform/variables.tf",
    "terraform/outputs.tf",
    "terraform/backend.tf",
    "terraform/bootstrap/bootstrap.tf",
    "terraform/envs/dev.tfvars",
    "terraform/envs/prod.tfvars",
    "terraform/modules/iam/main.tf",
    "terraform/modules/iam/variables.tf",
    "terraform/modules/iam/outputs.tf",
    "terraform/modules/ec2/main.tf",
    "terraform/modules/ec2/variables.tf",
    "terraform/modules/ec2/outputs.tf",
    "terraform/modules/ecr/main.tf",
    "terraform/modules/ecr/variables.tf",
    "terraform/modules/ecr/outputs.tf",
    "config/config.yaml",
    "research/trials.ipynb",
    "research/test_01_data_ingestion.ipynb",
    "scripts/ec2_setup.sh",
    "scripts/run_jenkins_locally_on_ubuntu.sh",
    "templates/index.html",
    "dvc.yaml",
    "main.py",
    "app.py",
    "params.yaml",
    "Dockerfile",
    "docker-compose.yml",
    ".dockerignore",
    "requirements.txt",
    "setup.py",
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
