from .data_loading import load_data
from .config import data_paths

twitter_data = load_data(data_paths['twitter_data'])

print(twitter_data.head())