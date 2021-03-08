import numpy as np
import pandas as pd


def load(csvpath): 
# loads the csv file in its raw form as a dataframe with no data modifications in case a user wants to view the data with all of its recorded errors.
    try:
        df = pd.DataFrame(pd.read_csv(csvpath))
        return df
    except(FileNotFoundError):
        print("Could not find the file at", csvpath)
    
    
def process(dataframe): 
    # This function has two parts, it cleans the data of errors and renames certain variables for readability
    # Cleans the dataset based on author recommendations:
    # 1. "any date that is before 860 CE or after 2016 are incorrect; these should actually be BCE years.""
    # 2. "a few entries have latitude and longitude of 0N/0E (...). 
    #     Many of these were actually discovered in Antarctica, but exact coordinates were not given. 0N/0E locations should probably be treated as NA."

    pass #TODO
