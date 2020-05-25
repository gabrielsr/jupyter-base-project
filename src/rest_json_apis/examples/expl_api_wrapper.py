# python src/rest_json_apis/examples/test_api_wrapper.py
from __init__ import setup_path
setup_path()

from pandas import json_normalize
from rest_json_apis.api_wrapper import init_api

# create a new api
query = init_api("http://api.football-data.org/v2/",
    api_key="5d865fcfc48c413bb0596467c6e8af5f")
x = query("competitions")
df = json_normalize(x["competitions"], max_level=2)

print(df)
