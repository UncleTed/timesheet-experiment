

from os.path import exists
from datetime import date, timedelta
import calendar
from tokenize import String
import argparse
import pandas as pd
import numpy as np


columns_headers=['Date', 'Day', 'Time', 'Project', 'Story Card']


def linearInterpolation():
    fluxData = 0
    # origin is fluxData
    # dest = top of color bar
    # origin + amt*(dest-origin)

def get_friday() -> String: 
    today = date.today()
    weekday_index = today.weekday()
    friday = today + timedelta(days=4 - weekday_index)
    return friday.strftime("%Y_%m_%d")+".csv"

def create_csv_if_not_exists() -> pd.DataFrame:
    file_name = get_friday() 
    if(not exists(file_name)):
        pd.DataFrame([],columns=columns_headers).to_csv(file_name, index=False)
    return pd.read_csv(file_name)

def uppercase_first_letter(name) -> str:
    return name.capitalize()

def main() -> None:
    timesheet_data_frame = create_csv_if_not_exists()
    parser = argparse.ArgumentParser()
    parser.add_argument("time", type=int, help='the time')
    parser.add_argument("project_name", type=str, help='the project name')
    parser.add_argument("storycard_number", type=str, help='story card number')
    args =  parser.parse_args()
    print(args)

    newEntry = pd.DataFrame([[date.today(),calendar.day_name[date.today().weekday()],args.time, uppercase_first_letter(args.project_name), args.storycard_number]],
        columns=['Date', 'Day', 'Time', 'Project', 'Story Card'])

    # print(df)
    timesheet_data_frame = pd.concat([ timesheet_data_frame, newEntry], ignore_index=True)
    # print(timesheet_data_frame)

    # timesheet_data_frame.sort_values(inplace=True, by=['Date', 'Time'])
    timesheet_data_frame.to_csv(get_friday(), index=False)
    #print(timesheet_data_frame)

    pivot_table = pd.pivot_table(timesheet_data_frame, values='Time', columns=['Day'] , index=['Day'], aggfunc=np.sum, fill_value=23)
    print(pivot_table)

if __name__ == '__main__':
    main()
