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
`ts monday 830 snappy 123`



## Backing store - data storage 

    1. A csv file named for the friday of the week. (e.g. 2022_01_21.csv)
    1. Columns :
      - Date
      - Time
      - project name
      - story card number 

