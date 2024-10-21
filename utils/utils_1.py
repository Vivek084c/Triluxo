import os 
from box.exceptions import BoxValueError
import yaml

import json


from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml (str) : path like input

    Raises:
        Valueerror: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
# Function to save text to a file
def save_to_file(filename, text):
    try:
        # Open the file in write mode ('w') - it will create the file if it doesn't exist
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

# Function to read text from a file
def read_from_file(filename):
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error reading file: {e}")