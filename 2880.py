import pandas as pd

def selectData(df: pd.DataFrame) -> pd.DataFrame:
    new_df=df[df["student_id"]==101]
    return new_df[["name","age"]]
    