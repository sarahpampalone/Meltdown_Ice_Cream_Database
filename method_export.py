import datetime
import pandas as pd

def write_to_excel(fullinventory, fullsales):
    data = {
        'Name' : fullinventory,
        'Units Sold' : fullsales
    }

    df = pd.DataFrame(data)
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H-%M-%S")  # Choose a format that suits your needs
    df.to_excel('salesrecord.xlsx', sheet_name=formatted_time, index=False)