import json

def save_list(data_list, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data_list, file)
        print(f"Data successfully saved to '{file_path}'.")
    except IOError as e:
        print(f"Error: Unable to save data to '{file_path}'. {e}")

def load_list(file_path):
    try:
        with open(file_path, 'r') as file:
            data_list = json.load(file)
        print(f"Data successfully loaded from '{file_path}'.")
        return data_list
    except IOError as e:
        print(f"Error: Unable to load data from '{file_path}'. {e}")
        return []