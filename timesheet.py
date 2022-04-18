import sys
from datetime import date, timedelta
import calendar
import pandas as pd
from os.path import exists


columns_headers=['Date', 'Day', 'Time', 'Project', 'Story Card']
def getFriday(): 
    today = date.today()
    weekday_index = today.weekday()
    friday = today + timedelta(days=4 - weekday_index)
    return friday.strftime("%Y_%m_%d")+".csv"

def create_csv_if_not_exists():
    file_name = getFriday() 
    if(not exists(file_name)):
        pd.DataFrame([],columns=columns_headers).to_csv(file_name, index=False)
    return pd.read_csv(file_name)




def main() -> None:
    timesheet_data_frame = create_csv_if_not_exists()
    i = input().split(' ')
    df = pd.DataFrame([[date.today(),calendar.day_name[date.today().weekday()],*i]],
        columns=['Date', 'Day', 'Time', 'Project', 'Story Card'])
    all = pd.concat([timesheet_data_frame, df], ignore_index=True)
    all.to_csv(getFriday(), index=False)
    print(all)


if __name__ == '__main__':
    main()
