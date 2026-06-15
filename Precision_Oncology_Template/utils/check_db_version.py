import os

def check_version():

    folder = "data/latest_db"

    print(
        "Database exists:",
        os.path.exists(folder)
    )