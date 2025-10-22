# MLOps-End-To-End-CNN-Classifier-Project

An End-To-End MLOps Project Based on DL implementing a complete pipeline from data ingestion to model evaluation. It integrates DVC for data/version control, MLflow for experiment tracking, TensorFlow for model training, Terraform for IAC, CI/CD with Jenkins, and automated deployment on AWS, ensuring scalability, reliability, and reproducibility.

## Prject Structure

```bash
├── config/
│   └── config.yaml
│
├── src/
│   └── <project_name>/
│       ├── __init__.py
│       │
│       ├── components/
│       │   └── __init__.py
│       │
│       ├── utils/
│       │   └── __init__.py
│       │
│       ├── config/
│       │   ├── __init__.py
│       │   └── configuration.py
│       │
│       ├── pipeline/
│       │   └── __init__.py
│       │
│       ├── entity/
│       │   └── __init__.py
│       │
│       └── constants/
│           └── __init__.py
│
├── research/
│   └── trials.ipynb
│
├── templates/
│   └── index.html
│
├── dvc.yaml
├── params.yaml
├── requirements.txt
└── setup.py
```
