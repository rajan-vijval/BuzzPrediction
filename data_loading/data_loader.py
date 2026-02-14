import pandas as pd

def load_data(filepath: str, col_names: list[str]) -> pd.DataFrame:
    return pd.read_csv(filepath,
                       sep=',',
                       header=None,
                       names=col_names)