"""
This module contains the code for the Log variable.

Note: Old built-in logger replaced with Tamga Logger (another open-source project by me).
"""

# Import necessary modules
from modules import (
    CUSTOM_LOGGER,  # Importing the custom logger configuration
    LOG_FILE_ROOT,  # Importing the LOG_FILE_ROOT variable from modules
    LOG_FOLDER_ROOT,  # Importing the LOG_FOLDER_ROOT variable from modules
    LOG_TO_FILE,  # Importing the LOG_TO_FILE variable from modules
    Tamga,  # Importing Tamga Logger
    exists,  # Importing the exists function from modules
    mkdir,  # Importing the mkdir function from modules
)

# Checking if LOG_FOLDER_ROOT directory exists
match exists(LOG_FOLDER_ROOT):
    case False:  # If LOG_FOLDER_ROOT doesn't exist
        mkdir(LOG_FOLDER_ROOT)  # Create LOG_FOLDER_ROOT directory

# 수정된 코드 (정상 작동)
Log = Tamga(
    file_output=LOG_TO_FILE,
    console_output=CUSTOM_LOGGER,
    file_path=LOG_FILE_ROOT
)

