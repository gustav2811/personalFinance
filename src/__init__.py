# src/__init__.py

"""
Personal finance budgeting tool package.
"""

# Package-level constants
PROJECT_NAME = "Personal finance budgeting tool"
VERSION = "1.0.0"

# Initialization code
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

__all__ = [
    "data_loader",
    "data_preprocessor",
    "data_extractor",
    "model",
    "train_model",
    "evaluate_model",
    "logger",
    "helper",
    "visualisation",
    "app",
    "routes",
]
