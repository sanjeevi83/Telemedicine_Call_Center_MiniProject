import pandas as pd # type: ignore

def load_data(file_path):
    """
    Loads the telemedicine call dataset from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data
