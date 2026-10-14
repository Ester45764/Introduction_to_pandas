import pandas as pd

def findHeavyAnimals(df: pd.DataFrame) -> pd.DataFrame:
     k= df[df["weight"]>100]
     return k.sort_values(by=["weight"], ascending=False)[["name"]]
     