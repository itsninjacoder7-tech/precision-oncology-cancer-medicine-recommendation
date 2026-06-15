import pandas as pd

def save_results(
    data,
    path
):

    pd.DataFrame(data).to_csv(
        path,
        index=False
    )