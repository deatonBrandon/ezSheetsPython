# import ezsheets
from db import read_data
import random


# I want to try something different
# This program will only need to read .csv files and divide them into a user-defined amount
# Only issue is I'm lazy, and I don't want to rename the csv file every time I want to upload ( i.e = myfile.csv, myfile (1).csv, myfile (2).csv ... )
# I like glob. It's not as performant as os, but these files are only a couple hundred rows


# split df and chunk leads by number of sales reps
def split_the_spreadsheet(frame):
    try:
        chunks = []   
        temp_lst = []

        chunk_size = int(input("Enter number of sales support reps assigned to this spreadsheet: "))    
        result = len(frame) // chunk_size
        remainder = len(frame) % chunk_size
        print("RESULT: ",result)
        print("REMAINDER: ", remainder)

        for bucket in range(0, len(frame), result):
            chunks.append(frame[bucket:bucket + result])

        print("CHUNKS AMENDED: ", len(chunks))

        if remainder:
            for i in range(1, remainder + 1):        
                random_int = random.randint(0, len(chunks) - 2)

                while remainder != 0:
                    if random_int not in temp_lst:
                        temp_lst.append(random_int) 
                        remainder -= 1
                    else:  
                        random_int = random.randint(0, len(chunks) - 2)
                        continue
            print("TEMP LIST: ", temp_lst)
            print("REMAINING CHUNK: ", chunks[-1])
            
            for x in temp_lst:
                popped = chunks[-1].pop()
                chunks[x].append(popped)
            chunks.pop()
        else:
            print("ALL REPS HAVE EQUAL LEADS")



        for x in range(len(chunks)):
            print("FINAL CHUNK LENGTH: ", len(chunks[x])) 
            print(chunks[x])
        
    except ValueError:
        print("Incorrect type of value. Must be numeric.")

def main():
    frame = read_data()
    try:
        split_the_spreadsheet(frame)
        # print("Successfully created a cleaned spreadsheet!")

    except ValueError:
        print("Must be a valid number only...")






if __name__ == "__main__":
    main()