import json
import pandas as pd
from pandas import json_normalize
from rest_json_apis.api_wrapper import init_api

api_key="5d865fcfc48c413bb0596467c6e8af5f"

api_base_callable = init_api("http://api.football-data.org/v2/",
    api_key=api_key)

def competitions(q={}):
    response_json = api_base_callable("competitions", 
        query=q)
    # transform into something parsable by pandas
    data_json = response_json['competitions']
    # 'flatten' the json and transform to pandas
    dataframe = json_normalize(data_json, max_level=2)
    return dataframe

def matches(q={}):
    response_json = api_base_callable("matches", 
        query=q)
    # transform into something parsable by pandas
    data_json = response_json['matches']
    # 'flatten' the json and transform to pandas
    data = json_normalize(data_json, max_level=2)
    return data

def teams(q={}):
    response_json = api_base_callable("teams", 
        query=q)
    # transform into something parsable by pandas
    data_json = response_json['teams']
    # 'flatten' the json and transform to pandas
    data = json_normalize(data_json, max_level=2)
    return data

def areas(q={}):
    response_json = api_base_callable("areas", 
        query=q)
    # transform into something parsable by pandas
    data_json = response_json['areas']
    # 'flatten' the json and transform to pandas
    data = json_normalize(data_json, max_level=2)
    return data
