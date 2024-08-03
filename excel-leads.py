# import ezsheets
import csv
import glob 
import random
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN


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
                reader = csv.reader(infile)
                next(reader)
                for rows in reader:
                    frame.append(rows)
                return frame

    except FileNotFoundError:
        print("No .csv files exist in this directory. Please try uploading the correct file format.")
    except OSError:
        print("Something went wrong... Please try again later.")



# Takes a list of lists and iterates through to return a flat list
def flatten_list(lst):
    return [x for xs in lst for x in xs]


# split df and chunk leads by number of sales reps
def split_dataframe(frame):
    try:
        chunks = []   

        chunk_size = int(input("Enter number of sales support reps assigned to this spreadsheet: "))    
        result = len(frame) / chunk_size
        result = Decimal(result)

        print(result)

        if (math.ceil(result) > result):
            result = result.quantize(Decimal("1"), ROUND_HALF_UP)
        else:
            result = result.quantize(Decimal("1"), ROUND_HALF_DOWN)

        result = int(result)

        for bucket in range(0, len(frame), result):
            chunks.append(frame[bucket:bucket + result])

        longest_straw = random.randrange(0, len(chunks) - 1)
        if (chunks[-1] != 0):
            test = chunks.pop()
            popped = flatten_list(test)
            chunks[longest_straw].append(popped)

        for x in range(len(chunks)):
            print(len(chunks[x]))
            print(chunks[x])
    except ValueError:
        print("Incorrect type of value. Must be numeric.")

def main():
    frame = read_data()
    try:
        split_dataframe(frame)
        # print("Successfully created a cleaned spreadsheet!")

    except ValueError:
        print("Must be a valid number only...")






if __name__ == "__main__":
    main()