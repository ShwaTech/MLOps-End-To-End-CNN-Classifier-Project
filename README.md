# MLOps-End-To-End-CNN-Classifier-Project

An End-To-End MLOps Project Based on DL implementing a complete pipeline from data ingestion to model evaluation. It integrates DVC for data/version control, MLflow for experiment tracking, TensorFlow for model training, Terraform for IAC, CI/CD with Jenkins, and automated deployment on AWS, ensuring scalability, reliability, and reproducibility.

## Prject Structure

```bash
├── config/
│   └── config.yaml
│
├── src/
│   └── cnnClassifier/
│       ├── __init__.py
│       │
│       ├── components/
│       │   ├── __init__.py
│       │   └── comp_01_data_ingestion.py
│       │
│       ├── utils/
│       │   └── __init__.py
│       │
│       ├── config/
│       │   ├── __init__.py
│       │   └── configuration.py
│       │
│       ├── pipeline/
│       │   ├── __init__.py
│       │   └── stage_01_data_ingestion.py
│       │
│       ├── entity/
│       │   └── __init__.py
│       │
│       └── constants/
│           └── __init__.py
│
├── research/
│   ├── trials.ipynb
│   └── test_01_data_ingestion.ipynb
│
├── templates/
│   └── index.html
│
├── dvc.yaml
├── params.yaml
├── main.py
├── requirements.txt
└── setup.py
```

## Workflows

1. Update ---> config.yaml
2. Update ---> params.yaml
3. Update ---> the entity
4. Update ---> the configuration manager in src config
5. Update ---> the components
6. Update ---> the pipeline
7. Update ---> the main.py
8. Update ---> the dvc.yaml
