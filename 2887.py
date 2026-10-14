import pandas as pd

def fillMissingValues(df: pd.DataFrame) -> pd.DataFrame:
    return df.fillna(value={"quantity":0})