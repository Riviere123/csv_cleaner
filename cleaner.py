import csv
import argparse

class Cleaner:
    def __init__(self, file, columns, rows, strip) -> None:
        self.file = open(f"{file}")
        self.columns = columns
        self.rows = rows
        self.data = csv.reader(self.file)
        self.strip = strip
        self.cleaned_data = self.data
        self.clean()
    
    def clean(self):
        self.remove_rows()
        self.remove_columns()

        self.write_file()

    def write_file(self):
        self.cleaned_data = "\n".join(self.cleaned_data)
        f = open("cleaned_data.csv", "w")
        f.write(self.cleaned_data)
        f.close()

    def remove_rows(self):
        cleaned_row_data = []
        row_count = -1
        for row in self.cleaned_data:
            row_count += 1
            if row_count in self.rows:
                continue
            cleaned_row_data.append(row)
        self.cleaned_data = cleaned_row_data
    
    def remove_columns(self):
        cleaned_column_data = []

        for row in self.cleaned_data:
            cleaned_column = []
            column_count = -1
            for column in row:
                column_count += 1
                if column_count in self.columns:
                    continue
                if self.strip:
                    cleaned_column.append(column.strip())
                else:
                    cleaned_column.append(column)
            cleaned_column_data.append(",".join(cleaned_column))
        
        self.cleaned_data = cleaned_column_data

parser = argparse.ArgumentParser(description='parameters for cleaning a csv file')

parser.add_argument(
    '--columns', 
    type=int,
    nargs="+",
    default=[], 
    help="The columns to remove. Usage: --rows 0 1 10 25",
)

parser.add_argument(
    '--file',
    type=str,
    default=None,
    help="The csv file path/name.",
)
parser.add_argument(
    '--rows',
    type=int,
    nargs="+",
    default=[],
    help="Rows to remove."
)
parser.add_argument(
    '--strip',
    action="store_true",
    help="Remove all leading and trailing white spaces."
)

args = parser.parse_args()

if __name__ == "__main__":
    cleaner = Cleaner(args.file, args.columns, args.rows, args.strip)