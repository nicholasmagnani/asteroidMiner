import pandas as pd

def preprocess_data(filepath):
    data = pd.read_csv(filepath)
    data = data.dropna()  # Example preprocessing step
    return data


def preprocess_data(df):
    """Preprocess the dataset."""
    # Example preprocessing steps
    df = df.dropna()  # Remove missing values
    df = df.reset_index(drop=True)  # Reset index after dropping rows
    return df

if __name__ == "__main__":
    # Load and preprocess Asterank data
    data_file = "data/asterank_data.csv"
    df = load_data(data_file)
    df = preprocess_data(df)
    df.to_csv("data/processed_asterank_data.csv", index=False)
