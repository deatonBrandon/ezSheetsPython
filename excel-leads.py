# import ezsheets
import csv
import numpy as np
import glob 

# I want to try something different
# This program will only need to read .csv files and divide them into a user-defined amount
# Only issue is I'm lazy, and I don't want to rename the csv file every time I want to upload ( i.e = myfile.csv, myfile (1).csv, myfile (2).csv ... )
# I like glob. It's not as performant as os, but these files are only a couple hundred rows

folder = glob.glob("./*.csv")

# read csv file from the glob and append it to a list
def read_data():
    try:
        for spreadsheet in folder:
            with open(spreadsheet, "r") as infile:
                frame = []
                for rows in csv.reader(infile):
                    frame.append(rows)
                return frame

        # for spreadsheet in folder: 
        #     temp_df = pd.read_csv(spreadsheet, dtype={"Phone 1": str}, index_col=False)
        #     temp_df = temp_df.fillna('-')
        #     frame.append(temp_df)
        # df = pd.concat(frame)
        # return df
    except FileNotFoundError:
        print("No .csv files exist in this directory. Please try uploading the correct file format.")
    except OSError:
        print("Something went wrong... Please try again later.")



# Writing data has to be its own function, regardless of being a one-liner
# def write_data(df):
#     df.to_csv('ezleads.csv', index=False)



# split df and chunk leads by number of sales reps
def split_dataframe(frame):
    chunks = []   
    chunk_size = int(input("Enter number of sales support reps assigned to this spreadsheet: "))
    
    result = len(frame) // chunk_size + (1 if len(frame) % chunk_size else 0)
        
    for bucket in range(0, len(frame), result):
        chunks.append(frame[bucket:bucket + result])

    print(len(frame))
    print(chunks)




def main():
    frame = read_data()
    while True:
        try:
            split_dataframe(frame)
            # print("Successfully created a cleaned spreadsheet!")
            break

        except ValueError:
            print("Must be a valid number only...")
            continue






if __name__ == "__main__":
    main()