import requests
import pandas as pd

def fetch_asterank_data(url):
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv('asterank_data.csv', index=False)
    return df
