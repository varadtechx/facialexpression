import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='%(asctime)s :  %(message)s : ')

project_name = 'facial_expression'

list_of_folders = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
                ]

for filepath in list_of_folders:
    path = Path(filepath)
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"created {path.parent}")
    if not path.exists():
        path.touch()
        logging.info(f"created {path}")


