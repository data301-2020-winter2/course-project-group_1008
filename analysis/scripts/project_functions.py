import numpy as np
import pandas as pd


def load(csvpath): 
# loads the csv file in its raw form as a dataframe with no data modifications in case a user wants to view the data with all of its recorded errors.
    try:
        df = pd.DataFrame(pd.read_csv(csvpath)).rename(columns={'name':'Name', 'id':'ID', 'recclass':'Class',
                                                                'mass':'Mass (g)', 'year':'Year', 'fall':'Fall',
                                                                'nametype':'Status', 'reclat':'Latitude', 'reclong':'Longitude'}
                                                                ).replace({'Fall':'Fell',}, 'Observed'
                                                                ).replace({'Status':'relict'}, 'Degraded')
        return df
    except(FileNotFoundError):
        print("Could not find the file at", csvpath)
    

def wrangle(dataframe):
# Cleans the dataset based on author recommendations:
 # 1. "any date that is before 860 CE or after 2016 are incorrect; these should actually be BCE years.""
 # 2. "a few entries have latitude and longitude of 0N/0E (...). 
 #     Many of these were actually discovered in Antarctica, but exact coordinates were not given. 0N/0E locations should probably be treated as NA."
    
    df = dataframe.replace({'Latitude': 0.0, 'Longitude':0.0}, np.nan)
    df.loc[(df['Year'] < 860)|(df['Year'] > 2016)] = np.nan
    df = df.dropna().reset_index().drop(columns=['index']) #drops all NA values in the dataframe
    
    return df


#test
# df = wrangle(load("data/raw/meteorite-landings.csv"))
# print(df)