import json
import pandas as pd
from pandas import json_normalize
from rest_json_apis.api_wrapper import init_api

API_URI = 'https://data.opendatasoft.com/api/records/1.0/search/'

api_base_callable = init_api(API_URI)

def world_population(q={}):
    baseQuery = {'dataset': 'world-population@kapsarc', 'rows': 10000}
    query = {**baseQuery, **q}
    response_json = api_base_callable('', query=query)
    # transform into something parsable by pandas
    data_json = response_json['records']
    # 'flatten' the json and transform to pandas
    df = json_normalize(data_json, max_level=2)
    
    # rename columns, drop columns
    df = df.rename(
        columns={ 
            'fields.country_name' : 'country_name',
            'fields.value' : 'value',
            'fields.year' : 'year'
        }).drop(columns=['record_timestamp', 'datasetid'])
    # convert type
    df = df.set_index('recordid')
    df['value'] = df['value'].astype(int)
    return df