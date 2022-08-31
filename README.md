# timesheet-experiment


# This uses Docker Remote VSCode container
https://code.visualstudio.com/docs/remote/containers-tutorial
and
https://github.com/microsoft/vscode-dev-containers


## General commands
`ts 830 snappy 123`

Add an entry to my timesheet that means I am starting to work on the snappy project and story card 123 at 08:30 am using today's date.

`ts 1000 snappy stu`
Add an entry to my timesheet that means I am starting to work on the snappy project story card STU (Stand Up Meeting) at 10:00 am. Implied is that I have stopped working on Snappy 123 at 10:00 am.

`ts 1200 lunch`
Lunch starts at 12:00 pm

`ts 1230 snappy 123`
We are continuing to work on card 123 after lunch

`ts 1700 end`
End of the day is 5:00 pm


## Extended commands
`ts monday 830 snappy 123`  - If it's Tuesday and I forgot to enter something on Monday

## Summary commands
`ts -s --summary` 
 Pivot table and display the results?

## Backing store - data storage 

    1. A csv file named for the friday of the week. (e.g. 2022_01_21.csv)
    1. Columns :
      - Date
      - Day of week
      - Time
      - Project name
      - Story card number 
      

## What to work on next
  1. If there is nothing on sys.argv, print out the current timesheet
  1. Capitalize the project name


## Done
  1. Switch to getopt so I can get the data as sys.argv
  1. Sort the CSV when writing it out

# Bibliography
https://medium.com/analytics-vidhya/pandas-pivot-table-with-examples-c174501fa9a1
  