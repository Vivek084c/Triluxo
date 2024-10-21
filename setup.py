import os

# Define directories and files
directories = ['src', 'utils', 'research', 'pipeline', 'stage', 'config']
files = ['app.py', '.env', 'params.yaml']

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)  # exist_ok=True ensures no error if directory already exists

# Create files
for file_name in files:
    with open(file_name, 'w') as f:
        pass  # Create empty files
    print(f'Created file: {file_name}')

print("Directory structure and files created successfully.")