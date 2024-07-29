# import ezsheets
import pandas as pd
import glob
from decimal import Decimal

# I want to try something different
# This program will only need to read .csv files and divide them into a user-defined amount
# Only issue is I'm lazy, and I don't want to rename the csv file every time I want to upload ( i.e = myfile.csv, myfile (1).csv, myfile (2).csv ... )
# I like glob. It's not as performant as os, but these files are only a couple hundred rows

folder = glob.glob("./*.csv")

# read csv file from the glob and append it to a list
def read_data():
    frame = []
    try:
        for spreadsheet in folder: 
            temp_df = pd.read_csv(spreadsheet, dtype={"Phone 1": str}, index_col=False)
            temp_df = temp_df.fillna('-')
            frame.append(temp_df)
        df = pd.concat(frame)
        return df

    except OSError:
        print("Error reading the file... Please try again.")



# divide and chunk leads by number of sales reps
def chunk_leads(df):
    try:
        count = int(input("Enter number of sales support reps assigned to this spreadsheet: "))
        result = len(df) / count
        result = int(result)
        for x in range(0, len(df), result):
            df.groupby('Date Created')
            
          
    except ZeroDivisionError:
        print("Must be a number greater than zero.")
    except ValueError: 
        print("Must be a valid number only.")





def main():
    data = read_data()
    chunk_leads(data)





if __name__ == "__main__":
    main()