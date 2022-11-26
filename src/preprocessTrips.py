from database.load_db import get_connection, close_connection

import pandas as pd


#------------------------------------------GET RID OF UNUSUAL TRIPS-----------------------------------------

def get_stop_times(): 
    query = ("select st.stop_sequence, st.stop_id, tr.trip_id"
        " from trips tr" 
        " inner join stop_times st on st.trip_id = tr.trip_id")

    connection = get_connection()
    data = pd.read_sql(query,con= connection)
    close_connection(connection)
    return data


def format_dict(): 
    occurence_dict={}
    data = get_stop_times()
    indexes= data.loc[data.stop_sequence == 1].index
    for i in range(1, len(indexes)): 
        key = data.trip_id.loc[indexes[i]]
        value = data.stop_id.loc[indexes[i-1]:indexes[i]]
        occurence_dict[key] = value
    return occurence_dict

format_dict()

def count_occurences():
    sub_data = format_dict()
    count =0
    for elem in sub_data.values(): 
        print(sum(map((elem).__eq__, sub_data.values())))
        
    
count_occurences()
