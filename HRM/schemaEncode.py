#A universal query and sensor aggregation framework
    #get time synced data chunks that are aggregated


    #users:
        #will query and aggregate sensor data as well as metadata and models
        #they will be training new models and creating new data structures

    #the DB will basically have a graphQL layer to query data


    #RAW data will be encoded into binary chunks for efficent storage, retrival and encryption

    #the database will have ingormation about what data streams, data, metadata and models are available and their hashes




    raw data layer
        - stores historical data
        - should be able to return arbitratily small units of data and be quired for time while still encrypted
        - MVP with just plain unecrypted data

    retrival API
        - handles encryption and addressing
        - primarily are workers that go into the data, chop up the files and return the time synced data for each type

    GraphQL
        - track the availibility of data
        - query data streams, metadata streams, models from time to time

    pipe that data and those models into python to operate on

    send processed data back to be stored


