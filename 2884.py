import pandas as pd

def modifySalaryColumn(df: pd.DataFrame) -> pd.DataFrame:
    df["salary"]=2*df["salary"]
    return df