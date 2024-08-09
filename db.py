import csv
import glob 

DIR = glob.glob("./*.csv")

# read csv file from the glob and append it to a list
def read_data():
    frame = []
    try:
        for spreadsheet in DIR:
            with open(spreadsheet, "r") as infile:
                reader = csv.reader(infile)
                next(reader)
                for rows in reader:
                    frame.append(rows)
                print(len(frame))
                return frame

    except FileNotFoundError:
        print("No .csv files exist in this directory. Please try uploading the correct file format.")
    except FileExistsError:
        print("This file doesn't exist in this directory. Please try again later.")
    except OSError:
        print("Something went wrong... Please try again later.")