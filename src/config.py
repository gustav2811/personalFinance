# src/config.py

import os

# Project settings
PROJECT_NAME = "Personal finance budgeting tool"
VERSION = "1.0.0"

# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
EXTERNAL_DATA_DIR = os.path.join(DATA_DIR, "external")

# Model settings
MODEL_DIR = os.path.join(BASE_DIR, "..", "models")
MODEL_NAME = "budgeting_model"
MODEL_VERSION = "v1.0"

# Logging settings
LOGGING_LEVEL = "INFO"
LOG_FILE = os.path.join(BASE_DIR, "..", "logs", "app.log")

# API settings
API_HOST = "0.0.0.0"
API_PORT = 8000
API_DEBUG_MODE = True

# Database settings (if any)
DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "..", "data", "database.db")

# Feature settings
FEATURES = ["income", "expenses", "savings", "investments"]

# Training settings
TRAINING_EPOCHS = 100
BATCH_SIZE = 32
LEARNING_RATE = 0.001

# Misc settings
RANDOM_SEED = 42


# Function to create necessary directories
def create_directories():
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    os.makedirs(EXTERNAL_DATA_DIR, exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "..", "logs"), exist_ok=True)


# Ensure directories are created
create_directories()

# Tesseract OCR settings specific to macOS
TESSDATA_PREFIX = "/opt/homebrew/share/tessdata"

# Setting the environment variable for Tesseract OCR
os.environ["TESSDATA_PREFIX"] = TESSDATA_PREFIX
