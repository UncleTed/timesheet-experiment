from os.path import exists
from datetime import date, timedelta
import calendar
from tokenize import String
import argparse
import pandas as pd
import numpy as np

    
columns_headers=['Date', 'Day', 'Time', 'Project', 'Story Card']





def print_series(series:pd.Series):
    print(series)

def create_csv_if_not_exists() -> pd.DataFrame:
    file_name = "test.csv"
    if(not exists(file_name)):
        pd.DataFrame([],columns=columns_headers).to_csv(file_name, index=False)
    return pd.read_csv(file_name)

 
def main():
    timesheet_data_frame = create_csv_if_not_exists()
    print(timesheet_data_frame)
    pivot_table = pd.pivot_table(timesheet_data_frame, values='Day', 
        columns=['Day'] , 
        index=['Time'], 
        aggfunc=np.sum, 
        fill_value='-')
    print(pivot_table)

if __name__ == '__main__':
    main()

