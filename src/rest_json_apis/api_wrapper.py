
import requests
import pandas as pd
from urllib.parse import urlencode, quote

def init_api(uri, api_key=None):
    headers = None
    if(api_key is not None):
        headers = {
            'User-Agent': 'apiclient',
            'X-Auth-Token': f'{api_key}'
        }
    def queryFnc(path, query=None, transformer=lambda input:input):
        # dic to a query string (i.e '?id=1')
        query_encoded = f'?{urlencode(query)}' if query is not None  else ''
        # uri = http://api.com
        # path = object
        # query = '?id=1'
        # >url = 'http://api.com/object?id=1'
        url = f'{uri}{path}{query_encoded}'
        # request
        response = requests.get(url, headers=headers)
        # status_code >= 400 is http errors
        if(response.status_code>=400):
            msg = f'GET:{url}\
            RESPONSE:\
            , code:{response.status_code} \
            , message:{response.text}'
            raise Exception(msg)
        json = response.json()
        # transform into string and parsed by pandas
        return json
    return queryFnc






