# csv_cleaner
A python script for cleaning CSV files. Remove rows, columns, and/or white spaces and yields a new cleaned csv file.

## arguments
#### --file: the file path/name to clean.
Example: "--file data.csv" will pull the data from "./data.csv".
Note: the path is relative to where you are running the script.

#### --rows: this will remove the rows you designate.
Example: "--rows 0 1 23" this will remove rows 0, 1, and 23.

#### --columns: this will remove the columns you designate.
Example: "--columns 2 4 12" this will remove columns 2, 4, 12.

#### --strip: this will remove all the leading and trailing white spaces from the data.
Example: "--strip"

## Usage
### Below are some examples of a full command

>python cleaner.py --file my_data.csv --columns 0 1 --rows 5 8 --strip

>python cleaner.py --file my_data.csv --columns 0

>python cleaner.py --file my_data.csv --rows 1

>python cleaner.py --file my_data.csv --strip
