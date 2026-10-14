import pandas as pd

def changeDatatype(df: pd.DataFrame) -> pd.DataFrame:
     df["grade"]=df["grade"].map(int)
     return df